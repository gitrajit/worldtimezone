"""
# world clock
###########
#import sys
"""
import sys
import argparse
import json
from datetime import datetime
import logging
import requests
from pytz import timezone, exceptions

_CONFIG_FILE = './config/configuration.json'

def set_logging(logfile, logformat):
    """
    Setting logging configuration
    :param: logfile: <string> log file name
    :param: logformat: format for logging
    :return: logging object
    """
    log = logging.getLogger('worldtimezone')
    log.setLevel(logging.INFO)
    file_handler = logging.FileHandler(logfile)
    log.addHandler(file_handler)
    formatter = logging.Formatter(logformat)
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    log.addHandler(stream_handler)
    stream_handler.setFormatter(formatter)
    return log

def download_file(url, dest, filename, logger):
    """
    Function to download json file.
    :param: url: <string>url to download the file
    :param: dest: <string> path to store
    :param: filename: <string>
    :return: boolean
    """
    try:
        content = json.loads(requests.get(url).text)
        with open(dest + "/" + filename, 'w', encoding="utf8") as json_file:
            json_file.write(json.dumps(content, indent=4))
        logger.info("world time zone format json file %s downloaded.", filename)
        logger.debug("downloading url %s, file Destination %s", url, dest)
        return True
    except ValueError as ioe:
        logger.error("Error in downloading file: %s", ioe)
        return False

def load_json(file):
    """
    function to load json file
    :param: file: <string>filename
    :return: json loaded object
    """
    try:
        with open(file, 'r', encoding='utf8') as config_file:
            return json.load(config_file)
    except IOError:
        return 0

def print_time(timezoneany, name, logger):
    """
    function to print the time for a particular region.
    :param: timezoneany: string
    :param: name: string
    :param: logger: logging object
    :return: print the time zone
    """
    try:
        datetime_any = datetime.now(tz=timezone(timezoneany))
        logger.info("%-35s : %-40s", name, datetime_any.strftime('%Y-%m-%d %H:%M:%S %Z %z'))
        return "Success"
    except (exceptions.UnknownTimeZoneError,IndexError):
        return "Fail"
def arguments():
    """ Parsing Input Arguments.
    return: Parser
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--match",\
                         help="Display only information about time zones\
                            whose values match the string supplied to this argument.")
    parser.add_argument("--offset",\
                        help="It will only display time zones matching this offset")
    return parser.parse_args()

def main():
    """
    Main function to parses the optional arguments and execute to display the world times
    :return: None
    """
    try:
        config_file = load_json(_CONFIG_FILE)
        logger = set_logging(config_file['logfilename'], config_file['logformat'])
        args = arguments()
        logger.debug("Argument --match %s, --offset %s", args.match, args.offset)
        logger.info("Downloading world time zone format json file")
        status = download_file(config_file['url'], config_file['download_path'],\
                                config_file['filename'], logger)
        if status is False:
            sys.exit()
        logger.info("Loading world time zone format json file")
        json_load = load_json(config_file['download_path']+ '/' +config_file['filename'])
        if (args.match and args.offset) or args.match:
            logger.info("Optional argument --match '%s' --offset %s",\
                 args.match.upper(), args.offset)
            matchvalue = list(filter(lambda x: x["value"].lower() == args.match.lower(), json_load))
            logger.info("*" *20 + "%s" + "*" *35, "Displaying time")
            print_time(matchvalue[0]['utc'][0], matchvalue[0]['value'], logger)
            logger.info("*" *70)
        elif args.offset:
            logger.info("Optional argument --offset %s", args.offset)
            offsetlist = list(filter(lambda x: x["offset"] == float(args.offset), json_load))
            logger.info("*" *20 + "%s" + "*" *35, "Displaying time")
            for value in offsetlist:
                print_time(value['utc'][0], value['value'], logger)
            logger.info("*" *70)
        else:
            logger.info("*" *20 + "%s" + "*" *35, "Displaying time")
            for value in json_load:
                try:
                    print_time(value['utc'][0], value['value'], logger)
                except IndexError:
                    logger.error("Invalid time zone")
            logger.info("*" *70)
    except (KeyboardInterrupt, IndexError, ValueError):
        logger.error("Error executing main function, Please check the argument and try.")



if __name__ == '__main__':
    main()
