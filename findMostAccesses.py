﻿# Most Accesses Finder (v0.1)

import re
import sys

# [INPUT TYPE]
# >>          python task2.py <date> <duration> <resource>
# >> EXAMPLE: python task2.py 03/May/2019:04:59:20 86401 /games/undertale

def is_match(regexType, inputText):
    pattern = re.compile(regexType)
    return pattern.search(inputText) is not None
    
date = str(sys.argv[1])
duration = int(sys.argv[2])
resource = str(sys.argv[3])

date1 = re.split("/", date)
date2 = re.split(":", date1[2])

# Open the input file
file1 = open("log_task2.txt", 'r')
lines = file1.readlines()
file1.close()

# The regex pattern that we created
patternDate = r"\d{1,2}[/](?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[/]\d{1,4}[:]\d{1,2}[:]\d{1,2}[:]\d{1,2}"
patternIP = r"\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}"

months = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}

day = int(date1[0])
month = months[str(date1[1])]
year = int(date2[0])
hour = int(date2[1])
minute = int(date2[2])
second = int(date2[3])

# AccessTime = DD*86400 + MM*2628288 + (YY−1970)*31536000 + hh*3600 + mm*60 + ss
accessTime = day*86400 + month*2628288 + (year-1970)*31536000 + hour*3600 + minute*60 + second

dicIPCount = {}
dicIPFirstAccess = {}

# Collect desired data by checking line by line
count = 0
for line in lines:
    count += 1

    matchIP = re.findall(patternIP, line)
    matchDate = re.findall(patternDate, line)
    currDate1 = re.split("/", matchDate[0])
    currDate2 = re.split(":", currDate1[2])
    currAccessTime = int(currDate1[0])*86400 + months[str(currDate1[1])]*2628288 + (int(currDate2[0])-1970)*31536000 + int(currDate2[1])*3600 + int(currDate2[2])*60 + int(currDate2[3])

    if is_match("GET " + resource, line):
        if accessTime <= currAccessTime < accessTime + duration:
            if str(matchIP[0]) in dicIPCount.keys():
                if dicIPFirstAccess[str(matchIP[0])] > currAccessTime:
                    dicIPFirstAccess[str(matchIP[0])] = currAccessTime
                    dicIPCount[str(matchIP[0])] = dicIPCount[str(matchIP[0])] + 1
                elif dicIPFirstAccess[str(matchIP[0])] <= currAccessTime:
                    dicIPCount[str(matchIP[0])] = dicIPCount[str(matchIP[0])] + 1
            else:
                dicIPCount[str(matchIP[0])] = 1
                dicIPFirstAccess[str(matchIP[0])] = currAccessTime

listIP = [key for key in sorted(dicIPCount, reverse = True)]

# Write all output to file
with open("output_task2.txt", 'w') as fp1:
    for item in listIP:
        fp1.write("%s %s %s\n" % (item, dicIPCount[item], dicIPFirstAccess[item]))
    fp1.close()

"""                         -- EXAMPLE --
[COMMAND] : python task2.py 22/Jan/2019:03:56:32 86400 /games/hollow_knight
[INPUT] : log_task2.txt
5.78.198.52 - - [22/Jan/2019:03:56:32 +0330] "GET /games/hollow_knight HTTP/1.1" ...
5.78.198.52 - - [22/Jan/2019:03:56:32 +0330] "GET /games/hollow_knight HTTP/1.1" ...
2.177.12.140 - - [22/Jan/2019:03:57:32 +0330] "GET /image/shiba.jpg HTTP/1.1" ...
2.177.12.140 - - [23/Jan/2019:03:56:31 +0330] "GET /games/hollow_knight HTTP/1.1" ...
2.177.12.140 - - [23/Jan/2019:03:56:32 +0330] "GET /games/hollow_knight HTTP/1.1" ...

[OUTPUT] : output_task2.txt
5.78.198.52 2 1549807280    → AccessTime(22/Jan/2019:03:56:32)
2.177.12.140 1 1549893679   → AccessTime(23/Jan/2019:03:56:31)
"""
