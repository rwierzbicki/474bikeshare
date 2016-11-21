
import csv
import time
import numpy as np
from sklearn.naive_bayes import MultinomialNB
#from sklearn.linear_model import LinearRegression

emptytime = [[0 for i in range(0, 13, 1)] for j in range(0, 100, 1)]

start_time = time.time()
filename = "201608_status_data.csv"

row_count = 589079 # int(35517186)
x_train = [[0,0,0] for j in range(row_count)] # day of week, hour, station #
yBike_train = [0 for j in range(row_count)] # bikes avail
yDock_train = [0 for j in range(row_count)] # docks avail
def timeWithNumberOfBikes(datafile, numBikes=3):

    with open(datafile) as csvfile:
        testreader = csv.reader(csvfile)
        print ("Starting")
        print(next(testreader))
        # row_count = sum(1 for row in testreader)
        # print ("Counted", row_count)
        
        count = 0
        print ("loop")
        for row in testreader:
            # print ("lol")
            # print (row[0])
            mins = int(row[3].split('/')[2].split(' ')[1].split(':')[1])
            if(mins==0):
                count+=1
                # print(count)
                stationNumber = int(row[0])
                month = int(row[3][:9].split('/')[0])
                day = int(row[3][:9].split('/')[1])
                year = int(row[3].split('/')[2].split(' ')[0])
                hour = int(row[3].split('/')[2].split(' ')[1].split(':')[0])
                mins = int(row[3].split('/')[2].split(' ')[1].split(':')[1])
                # print (month, day, year, hour, mins)

                bikesAvail = int(row[1])
                docksAvail = int(row[2])
                x_train[count][0] = weekDay(year,month,day)
                x_train[count][1] = hour
                x_train[count][2] = stationNumber

                yBike_train[count] = bikesAvail
                yDock_train[count] = docksAvail

                # if bikesAvail<=numBikes:
                #     emptytime[stop][month] +=1
                if count%100000==0:
                        print(count)
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
# x_test = [[1,9,4],[4,6,4]]
# print (x_test[0])
timeWithNumberOfBikes(filename)

clf = MultinomialNB()
clf.fit(x_train, yBike_train)
x_test = [[1,9,4],
    [4,18,4],
    [5,17,13],
    [3,1,1],
    [6,20,52],
    [7,12,62],
    [1,16,91],
    [2,10,16]
]

# print (x_train[0:2][0])
# print (x_test[0])
MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)
print(clf.predict(x_test))
clf2 = MultinomialNB()
clf2.fit(x_train, yDock_train)
x2_test = [[1,9,4],
    [4,18,4],
    [5,17,13],
    [3,1,1],
    [6,20,52],
    [7,12,62],
    [1,16,91],
    [2,10,16]
]
MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)
print(clf2.predict(x2_test))
