
import csv
import time
#from sklearn.linear_model import LinearRegression

emptytime = [[0 for i in range(0, 13, 1)] for j in range(0, 100, 1)]

start_time = time.time()
filename = "201608_status_data.csv"

def timeWithNumberOfBikes(datafile, numBikes=3):
    with open(datafile) as csvfile:
        testreader = csv.reader(csvfile)

        print(next(testreader))
        print("loop now")
        count = 0
        for row in testreader:
            count+=1
            stop = int(row[0])
            month = int(row[3][:9].split('/')[0])
            temp = int(row[1])
            if temp<=numBikes:
                emptytime[stop][month] +=1
            if count%100000==0:
                    print(count)
                # print(isinstance(int(row[1]), int ))

    stopid =0
    for row in emptytime:
        print("stopID is ", stopid)
        stopid += 1
        print(row)

    end = time.time()
    print("time taken ", (end-start_time))
    print("final data count ", count)


timeWithNumberOfBikes(filename)