
import csv
import time
import numpy as np
from sklearn.naive_bayes import MultinomialNB
#from sklearn.linear_model import LinearRegression

emptytime = [[0 for i in range(0, 13, 1)] for j in range(0, 100, 1)]

start_time = time.time()
filename = "201608_status_data.csv"

def timeWithNumberOfBikes(datafile, numBikes=3):
    with open(datafile) as csvfile:
        testreader = csv.reader(csvfile)
        row_count = sum(1 for row in testreader)
        x_train = [[0 for i in range(3)] for j in range(row_count)] # day of week, hour, station #
        yBike_train = [0 for j in range(row_count)] # bikes avail
        yDock_train = [0 for j in range(row_count)] # docks avail
        print(next(testreader))
        print("loop now")
        count = 0
        for row in testreader:
            # min = int(row[3].split('/')[2].split(' ')[1].split(':')[1])
            # if(min==0):
            count+=1
            stationNumber = int(row[0])
            month = int(row[3][:9].split('/')[0])
            day = int(row[3][:9].split('/')[1])
            year = int(row[3].split('/')[2].split(' ')[0])
            hour = int(row[3].split('/')[2].split(' ')[1].split(':')[0])
            min = int(row[3].split('/')[2].split(' ')[1].split(':')[1])
            # print month, day, year, hour, min

            bikesAvail = int(row[1])
            docksAvail = int(row[2])
            x_train[0][count] =  weekDay(year,month,day)
            x_train[1][count] = hour
            x_train[2][count] = stationNumber

            yBike_train[count] = bikesAvail
            yDock_train[count] = docksAvail

            # if bikesAvail<=numBikes:
            #     emptytime[stop][month] +=1
            # if count%100000==0:
            #         print(count)
                # print(isinstance(int(row[1]), int ))

    # stopid =0
    # for row in emptytime:
    #     print("stopID is ", stopid)
    #     stopid += 1
    #     print(row)

    end = time.time()
    print("time taken ", (end-start_time))
    print("final data count ", count)

def weekDay(year, month, day):
    offset = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    week   = ['Sunday',
              'Monday',
              'Tuesday',
              'Wednesday',
              'Thursday',
              'Friday',
              'Saturday']
    # week = [1,2,3,4,5,6,7]
    afterFeb = 1
    if month > 2: afterFeb = 0
    aux = year - 1700 - afterFeb
    # dayOfWeek for 1700/1/1 = 5, Friday
    dayOfWeek  = 5
    # partial sum of days betweem current date and 1700/1/1
    dayOfWeek += (aux + afterFeb) * 365
    # leap year correction
    dayOfWeek += aux / 4 - aux / 100 + (aux + 100) / 400
    # sum monthly and day offsets
    dayOfWeek += offset[month - 1] + (day - 1)
    dayOfWeek %= 7
    return dayOfWeek #, week[dayOfWeek]

timeWithNumberOfBikes(filename)
clf = MultinomialNB()
clf.fit(x_train, yBike_train)
x_test = [[1,9,4],[4,6,4]]
MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)
print(clf.predict(x_test))
