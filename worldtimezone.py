"""
# world clock
###########
#import sys
"""
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
    """
    try:
        content = json.loads(requests.get(url).text)
        with open(dest + "/" + filename, 'w', encoding="utf8") as json_file:
            json_file.write(json.dumps(content, indent=4))
        logger.info("world time zone format json file %s downloaded.", filename)
        logger.debug("downloading url %s, file Destination %s", url, dest)
        return True
    except IOError as ioe:
        logger.error("Error in downloading file: %s", ioe)
        return False

def load_json(file):
    """
    function to load json file.
    """
    try:
        with open(file, 'r', encoding='utf8') as config_file:
            return json.load(config_file)
    except IOError:
        return 0

def print_time(timezoneany, name, logger):
    """
    function to print the time for a particular region
    """
    # now_utc = datetime.now(timezone('UTC'))
    # datetime_any = now_utc.astimezone(timezone(timezoneany))
    try:
        datetime_any = datetime.now(tz=timezone(timezoneany))
        logger.info("%-35s : %-40s", name, datetime_any.strftime('%Y-%m-%d %H:%M:%S %Z %z'))
        return "Success"
    except exceptions.UnknownTimeZoneError:
        return "Fail"

def main():
    """
    Main function to display world time.
    """
    config_file = load_json(_CONFIG_FILE)
    logger = set_logging(config_file['logfilename'], config_file['logformat'])
    parser = argparse.ArgumentParser()
    parser.add_argument("--match", help="Display only information about time zones\
                                         whose values match the string supplied to \
                                            this argument.")
    parser.add_argument("--offset", help="It will only display time zones matching this offset")
    args = parser.parse_args()
    logger.debug("Argument --match %s, --offset %s", args.match, args.offset)
    logger.info("Downloading world time zone format json file")
    download_file(config_file['url'], config_file['download_path'], config_file['filename'], logger)
    logger.info("Loading world time zone format json file")
    json_load = load_json(config_file['download_path']+ '/' +config_file['filename'])
    if (args.match and args.offset) or args.match:
        logger.info("Optional argument --match '%s' --offset %s", args.match.upper(), args.offset)
        matchvalue = list(filter(lambda x: x["value"].lower() == args.match.lower(), json_load))
        logger.info("********************Displaying time **********************************")
        print_time(matchvalue[0]['utc'][0], matchvalue[0]['value'], logger)
        logger.info("**********************************************************************")
    elif args.offset:
        logger.info("Optional argument --offset %s", args.offset)
        offsetlist = list(filter(lambda x: x["offset"] == float(args.offset), json_load))
        logger.info("********************Displaying time **********************************")
        for value in offsetlist:
            print_time(value['utc'][0], value['value'], logger)
        logger.info("**********************************************************************")
    else:
        logger.info("********************Displaying time ***********************************")
        for value in json_load:
            try:
                print_time(value['utc'][0], value['value'], logger)
            except IndexError:
                logger.error("Invalid time zone")
        logger.info("**********************************************************************")



if __name__ == '__main__':
    main()
