import matplotlib.pyplot as plt
import numpy as np
import sys
import csv


print(sys.version)
filename = "201608_trip_data.csv"


def tripcounter(datafile):
    tripcount = [[0 for i in range(0, 100, 1)] for j in range(0, 100, 1)]
    with open(datafile) as csvfile:
        testreader = csv.reader(csvfile)

        print(next(testreader))
        for row in testreader:
            start_terminal = int(row[4])
            end_terminal = int(row[7])
            tripcount[start_terminal][end_terminal] =1+tripcount[start_terminal][end_terminal]


        for i in range(1,100):
            print(i)
            print(tripcount[i])


    for i in range(1,100):
        print(i)
        print(tripcount[i])
        # print max(tripcount[i]) #max 3500

    # image = np.random.rand(30, 30)
    plt.imshow(tripcount, cmap=plt.cm.gray)
    plt.colorbar()
    plt.show()

tripcounter(filename)

