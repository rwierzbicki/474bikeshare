import csv

import os.path
import math
import time


"""spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
...     for row in spamreader:
...         print(', '.join(row))
"""
##
tripcount = [[0 for i in range(32)] for j in range(13)]

with open("201608_trip_data.csv") as csvfile:
    testreader = csv.reader(csvfile)
    test = "9/2/2015"
    ##print(test.split('/')[1])
    #tripcount = [][]
    sample = ""
    count = 0
    ##while day
    for row in testreader:
        temp = next(testreader)[2][:9].split('/')
        day = int(temp[1])
        month = int(temp[0])
        print(day)

        tripcount[month][day] =1+tripcount[month][day]


    for i in range(13):
        print(tripcount[i])

    while sample!=test:
        sample = next(testreader)[2][:8]
        #print("yea")
        count = count+1

    print(count)
    for x in range(1, 5):
        ##print(x)
        ##print(testreader.__next__())
        print(int(next(testreader)[2][:9].split('/')[1]))
        ##testreader.__next__()