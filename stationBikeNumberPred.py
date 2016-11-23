
import csv
import time
import numpy as np
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import Perceptron, LogisticRegression, LinearRegression
from sklearn import datasets
# from sklearn.cross_validation import train_test_split

emptytime = [[0 for i in range(0, 13, 1)] for j in range(0, 100, 1)]

start_time = time.time()
filename = "201608_status_data.csv"
weatherfilename = "201608_weather_data.csv"

row_count = 589079 # int(35517186), only check once an hour
row_count2 = 610794 # 36647623
x_train = [[0,0,0,0,0,0] for j in range(row_count)] # month, day of week, hour, station #, mean temp, rain? 0:1
yBike_train = [0 for j in range(row_count)] # bikes avail
yDock_train = [0 for j in range(row_count)] # docks avail
x_test = [[0,0,0,0,0,0] for j in range(row_count2)] # month, day of week, hour, station #, mean temp, rain? 0:1
yBike_test = [0 for j in range(row_count2)] # bikes avail
yDock_test = [0 for j in range(row_count2)] # docks avail

def timeWithNumberOfBikes(datafile, weatherfile):

    with open(datafile) as csvfile:
        with open(weatherfile) as csvWeather:
            weatherreader = csv.reader(csvWeather)
            testreader = csv.reader(csvfile)
            print ("Starting")
            print(next(testreader))
            print(next(weatherreader))
            weatherCount =0
            count = 0
            print ("loop")
            lastDay = day = 0
            weatherData = next(weatherreader)
            for row in testreader:
                mins = int(row[3].split('/')[2].split(' ')[1].split(':')[1])
                if(mins==0):
                    
                    count+=1
                    stationNumber = int(row[0])
                    month = int(row[3][:9].split('/')[0])
                    day = int(row[3][:9].split('/')[1])
                    year = int(row[3].split('/')[2].split(' ')[0])
                    hour = int(row[3].split('/')[2].split(' ')[1].split(':')[0])
                    mins = int(row[3].split('/')[2].split(' ')[1].split(':')[1])
                    # print (month, day, year, hour, mins)

                    bikesAvail = int(row[1])
                    docksAvail = int(row[2])
                    x_train[count][0] = month
                    x_train[count][1] = weekDay(year,month,day)
                    x_train[count][2] = hour
                    x_train[count][3] = stationNumber
                    x_train[count][4] = int(weatherData[2])
                    if(weatherData[21]=='Rain'):
                        x_train[count][5] = 1
                    else:
                        x_train[count][5] = 0
                    # print(lastDay,day)
                    
                    if lastDay != day and weatherCount<1829: #and count>1
                        # print(weatherData[0], month, day)
                        weatherData = next(weatherreader)
                        weatherCount+=1 
                    lastDay = day
                    yBike_train[count] = bikesAvail
                    yDock_train[count] = docksAvail
                    
                    if count%100000==0:
                            print(count)


        end = time.time()
        print("time taken ", (end-start_time))
        print("final data count ", count)


def getTestYear3(datafile, weatherfile):
    with open(datafile) as csvfile:
        with open(weatherfile) as csvWeather:
            weatherreader = csv.reader(csvWeather)
            testreader = csv.reader(csvfile)
            print ("Starting")
            print(next(testreader))
            print(next(weatherreader))
            weatherCount =0
            count = 0
            print ("loop")
            lastDay = day = 0
            weatherData = next(weatherreader)
            for row in testreader:
                mins = int(row[3].split('/')[2].split(' ')[1].split(':')[1])
                if(mins==0):
                    
                    count+=1
                    stationNumber = int(row[0])
                    month = int(row[3][:9].split('/')[0])
                    day = int(row[3][:9].split('/')[1])
                    year = int(row[3].split('/')[2].split(' ')[0])
                    hour = int(row[3].split('/')[2].split(' ')[1].split(':')[0])
                    mins = int(row[3].split('/')[2].split(' ')[1].split(':')[1])
                    # print (month, day, year, hour, mins)

                    bikesAvail = int(row[1])
                    docksAvail = int(row[2])
                    x_test[count][0] = month
                    x_test[count][1] = weekDay(year,month,day)
                    x_test[count][2] = hour
                    x_test[count][3] = stationNumber
                    if(weatherData[2]==''):
                        x_test[count][4]=0
                    else:
                        x_test[count][4] = int(weatherData[2])
                    if(weatherData[21]=='Rain'):
                        x_test[count][5] = 1
                    else:
                        x_test[count][5] = 0
                    # print(lastDay,day)
                    
                    if lastDay != day and weatherCount<1829: #and count>1
                        # print(weatherData[0], month, day)
                        weatherData = next(weatherreader)
                        weatherCount+=1 
                    lastDay = day
                    yBike_test[count] = bikesAvail
                    yDock_test[count] = docksAvail
                    
                    if count%100000==0:
                            print(count)

def getTestYear2(datafile, weatherfile):
    with open(datafile) as csvfile:
        with open(weatherfile) as csvWeather:
            weatherreader = csv.reader(csvWeather)
            testreader = csv.reader(csvfile)
            # row_count2 = sum(1 for row in testreader)
            # print(row_count2)
            print ("Starting")
            print(next(testreader))
            print(next(weatherreader))
            weatherCount =0
            count = 0
            print ("loop")
            lastDay = day = 0
            weatherData = next(weatherreader)
            for row in testreader:
                mins = int(row[3].split('-')[2].split(' ')[1].split(':')[1])
                if(mins==0):
                    count+=1
                    stationNumber = int(row[0])
                    year = int(row[3][:9].split('-')[0])
                    month = int(row[3][:9].split('-')[1])
                    day = int(row[3].split('-')[2].split(' ')[0])
                    hour = int(row[3].split('-')[2].split(' ')[1].split(':')[0])
                    mins = int(row[3].split('-')[2].split(' ')[1].split(':')[1])
                    # print (month, day, year, hour, mins)

                    bikesAvail = int(row[1])
                    docksAvail = int(row[2])
                    x_test[count][0] = month
                    x_test[count][1] = weekDay(year,month,day)
                    x_test[count][2] = hour
                    x_test[count][3] = stationNumber
                    # print ("wd3:")
                    # print(weatherData[2])
                    if(weatherData[2]==''):
                        x_test[count][4]=0
                    else:
                        x_test[count][4] = int(weatherData[2])
                    # x_test[count][4] = int(weatherData[2])
                    if(weatherData[21]=='Rain'):
                        x_test[count][5] = 1
                    else:
                        x_test[count][5] = 0
                    # print(lastDay,day)
                    
                    if lastDay != day and weatherCount<1825: #and count>1
                        # print(weatherData[0], month, day, weatherCount)
                        if weatherCount<1824:
                            weatherData = next(weatherreader)
                        weatherCount+=1 
                    lastDay = day
                    yBike_test[count] = bikesAvail
                    yDock_test[count] = docksAvail
                    
                    if count%100000==0:
                            print(count)


def weekDay(year, month, day):
    offset = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    week   = ['Sunday',
              'Monday',
              'Tuesday',
              'Wednesday',
              'Thursday',
              'Friday',
              'Saturday']
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

# Doesnt do much, just ask Cole
def actualAnswer(datafile,testDataArray):
    with open(datafile) as csvfile:
        testreader = csv.reader(csvfile)
        print ("Starting answer checking")
        print(next(testreader))
        for x in testDataArray:
            for row in testreader:
                    mins = int(row[3].split('/')[2].split(' ')[1].split(':')[1])
                    if(mins==0):
                        stationNumber = int(row[0])
                        month = int(row[3][:9].split('/')[0])
                        day = int(row[3][:9].split('/')[1])
                        year = int(row[3].split('/')[2].split(' ')[0])
                        hour = int(row[3].split('/')[2].split(' ')[1].split(':')[0])
                        mins = int(row[3].split('/')[2].split(' ')[1].split(':')[1])
                        # print (month, day, year, hour, mins)
                        bikesAvail = int(row[1])
                        docksAvail = int(row[2])
                        if(x[0]==month)and(x[1]==day)and(x[2]==hour)and(x[3]==stationNumber):
                            print(x,bikesAvail,docksAvail)
                            break


timeWithNumberOfBikes(filename,weatherfilename)
testfilename = "201508_status_data.csv"
testweatherfilename = "201508_weather_data.csv"
getTestYear2(testfilename,testweatherfilename)


# Load some classifiers into a list and initialize them
algs = [
    GaussianNB(), 
    DecisionTreeClassifier(),
    MultinomialNB(),
    BernoulliNB(), 
    Perceptron(), 
    LinearRegression(),
    # LogisticRegression(), 
]

for alg in algs:
    alg = alg.fit(x_train, yBike_train)
    print("Number of bikes available: ")
    # print(alg.predict(x_test))
    # print ((type(alg).__name__, alg.predict(x_test)))
    print (type(alg).__name__, alg.score(x_test, yBike_test))
    alg = alg.fit(x_train, yDock_train)
    print("Number of docks available: ")
    # print(alg.predict(x2_test))
    # print ((type(alg).__name__, alg.predict(x_test)))
    print (type(alg).__name__, alg.score(x_test, yDock_test))

#  Manual testingt
# month, day of week, hour, station #, mean temp, rain?
# x1_test = [[7,1,9,4,60,0],
#     [7,4,18,4,50,1],
#     [7,5,17,13,60,1],
#     [7,3,1,1,70,0],
#     [7,6,20,52,70,1],
#     [7,7,12,62,60,0],
#     [1,1,16,91,50,0],
#     [4,1,16,91,60,1],
#     [7,1,16,91,65,0],
#     [10,1,16,91,65,1],
#     [7,2,10,16,65,0]
# ]
# x2_test = [[7,1,9,4,60,0],
#     [7,4,18,4,50,1],
#     [7,5,17,13,60,1],
#     [7,3,1,1,70,0],
#     [7,6,20,52,70,1],
#     [7,7,12,62,60,0],
#     [1,1,16,91,50,0],
#     [4,1,16,91,60,1],
#     [7,1,16,91,65,0],
#     [10,1,16,91,65,1],
#     [7,2,10,16,65,0]
# ]
# # filename2 = "201608_status_data.csv"
# # actualAnswer(filename2,x_test)
# # Run through each classifier, train them with the training dataset, then test it using the score function
# for alg in algs:
#     alg = alg.fit(x_train, yBike_train)
#     print("Number of bikes available: ")
#     # print(alg.predict(x_test))
#     print ((type(alg).__name__, alg.predict(x1_test)))

#     alg = alg.fit(x_train, yDock_train)
#     print("Number of docks available: ")
#     # print(alg.predict(x2_test))
#     print ((type(alg).__name__, alg.predict(x2_test)))


