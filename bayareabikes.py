import csv

import os.path
import math
import time


"""spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
...     for row in spamreader:
...         print(', '.join(row))
"""
##
months = ['no', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']


tripcount = [[0 for i in range(0, 32, 1)] for j in range(0, 13, 1)]

with open("201608_trip_data.csv") as csvfile:
    testreader = csv.reader(csvfile)


    for row in testreader:
        temp = next(testreader)[2][:9].split('/')
        day = int(temp[1])
        month = int(temp[0])
        #print(day,month)
        tripcount[month][day] =1+tripcount[month][day]


    for i in range(1,13):
        print(months[i])
        print(tripcount[i])

