## Python Assignment | Linux Automation
### Description
Program that returns information about the world time zone.

## Getting the code

Prior to running, you should clone this project to a local directory.
`https://github.com/gitrajit/worldtimezone.git`

Directory Structure
-----------
```
rackspace/
├── README.md
├── config
│   └── configuration.json
├── data
│   └── timezones.json
├── requirements.txt
├── test
│   ├── __init__.py
│   └── worldtimezonetest.py
├── worldtimezone.log
└── worldtimezone.py
```
* **config folder**: It contain all the necessary configuration details like url, filename etc.
* **data folder**: Folder to download the JSON file.
* **test folder**: Folder for Unit testing

## Steps to Execute
1) Install all the required packages
```
pip install -r requirements.txt
```

2) Python worldtimezone.py --help
```
usage: worldtimezone.py [-h] [--match MATCH] [--offset OFFSET]

optional arguments:
  -h, --help       show this help message and exit
  --match MATCH    Display only information about time zones whose values match the string supplied to this argument.
  --offset OFFSET  It will only display time zones matching this offset
```
3) Execute Python worldtimezone.py without argument
```
2022-06-01 18:14:13,478  worldtimezone  INFO  Downloading world time zone format json file
2022-06-01 18:14:13,694  worldtimezone  INFO  world time zone format json file timezones.json downloaded.
2022-06-01 18:14:13,696  worldtimezone  INFO  Loading world time zone format json file
2022-06-01 18:14:13,723  worldtimezone  INFO  ********************Displaying time ******************************
2022-06-01 18:14:13,746  worldtimezone  INFO  Dateline Standard Time              : 2022-06-01 00:44:13 -12 -1200
2022-06-01 18:14:13,746  worldtimezone  INFO  UTC-11                              : 2022-06-01 01:44:13 -11 -1100
2022-06-01 18:14:13,747  worldtimezone  INFO  Hawaiian Standard Time              : 2022-06-01 02:44:13 -10 -1000
2022-06-01 18:14:13,749  worldtimezone  INFO  Alaskan Standard Time               : 2022-06-01 04:44:13 AKDT -080
2022-06-01 18:14:13,750  worldtimezone  INFO  Pacific Standard Time (Mexico)      : 2022-06-01 05:44:13 PDT -0700
2022-06-01 18:14:13,751  worldtimezone  INFO  Pacific Daylight Time               : 2022-06-01 05:44:13 PDT -0700
2022-06-01 18:14:13,757  worldtimezone  INFO  Central Standard Time (Mexico)      : 2022-06-01 07:44:13 CDT -0500
2022-06-01 18:14:13,762  worldtimezone  INFO  SA Western Standard Time            : 2022-06-01 08:44:13 AST -0400
2022-06-01 18:14:13,763  worldtimezone  INFO  Pacific SA Standard Time            : 2022-06-01 08:44:13 -04 -0400
2022-06-01 18:14:13,763  worldtimezone  INFO  Newfoundland Standard Time          : 2022-06-01 10:14:13 NDT -0230
2022-06-01 18:14:13,764  worldtimezone  INFO  E. South America Standard Time      : 2022-06-01 09:44:13 -03 -0300
2022-06-01 18:14:13,764  worldtimezone  INFO  Argentina Standard Time             : 2022-06-01 09:44:13 -03 -0300
2022-06-01 18:14:13,841  worldtimezone  INFO  *****************************************************************
```
4) Excecute with arguments:
**--match**
```
gitrajit@DESKTOP-600EAN8:/mnt/d/rackspace$ python3 worldtimezone.py --match "India Standard time"
2022-06-01 18:17:39,900  worldtimezone  INFO  Downloading world time zone format json file
2022-06-01 18:17:40,086  worldtimezone  INFO  world time zone format json file timezones.json downloaded.
2022-06-01 18:17:40,087  worldtimezone  INFO  Loading world time zone format json file
2022-06-01 18:17:40,116  worldtimezone  INFO  Optional argument --match 'INDIA STANDARD TIME' --offset None
2022-06-01 18:17:40,117  worldtimezone  INFO  ********************Displaying time ******************************
2022-06-01 18:17:40,134  worldtimezone  INFO  India Standard Time                 : 2022-06-01 18:17:40 IST +0530
2022-06-01 18:17:40,135  worldtimezone  INFO  ******************************************************************
```
**--offset**
```
gitrajit@DESKTOP-600EAN8:/mnt/d/rackspace$ python3 worldtimezone.py --offset 2
2022-06-01 18:18:38,203  worldtimezone  INFO  Downloading world time zone format json file
2022-06-01 18:18:38,702  worldtimezone  INFO  world time zone format json file timezones.json downloaded.
2022-06-01 18:18:38,704  worldtimezone  INFO  Loading world time zone format json file
2022-06-01 18:18:38,732  worldtimezone  INFO  Optional argument --offset 2
2022-06-01 18:18:38,734  worldtimezone  INFO  ********************Displaying time ***************************
2022-06-01 18:18:38,752  worldtimezone  INFO  W. Europe Standard Time             : 2022-06-01 14:48:38 CEST +020
2022-06-01 18:18:38,753  worldtimezone  INFO  Central Europe Standard Time        : 2022-06-01 14:48:38 CEST +020
2022-06-01 18:18:38,754  worldtimezone  INFO  Romance Standard Time               : 2022-06-01 14:48:38 CEST +020
2022-06-01 18:18:38,755  worldtimezone  INFO  Central European Standard Time      : 2022-06-01 14:48:38 CEST +020
2022-06-01 18:18:38,756  worldtimezone  INFO  Egypt Standard Time                 : 2022-06-01 14:48:38 EET +0200
2022-06-01 18:18:38,757  worldtimezone  INFO  South Africa Standard Time          : 2022-06-01 14:48:38 CAT +0200
2022-06-01 18:18:38,757  worldtimezone  INFO  Libya Standard Time                 : 2022-06-01 14:48:38 EET +0200
2022-06-01 18:18:38,758  worldtimezone  INFO  **************************************************************
gitrajit@DESKTOP-600EAN8:/mnt/d/rackspace$
```
## Pylint result (pylint 2.12.2)
```
pylint worldtimezone.py
--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

pylint test/worldtimezonetest.py
--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
```
## Unit Testing
```
gitrajit@DESKTOP-600EAN8:/mnt/d/rackspace$ python3 -m unittest test/worldtimezonetest.py
----------------------------------------------------------------------
Ran 3 tests in 0.205s

OK
```

License
-------

BSD



