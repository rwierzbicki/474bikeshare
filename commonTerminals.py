import csv
# from matplotlib import mpl,pyplot
# import matplotlib
import matplotlib.pyplot as plt
import numpy as np





tripcount = [[0 for i in range(0, 100, 1)] for j in range(0, 100, 1)]

with open("201608_trip_data.csv") as csvfile:
    testreader = csv.reader(csvfile)

    print(next(testreader))
    for row in testreader:
        start_terminal = int(row[4])
        end_terminal = int(row[7])
        tripcount[start_terminal][end_terminal] =1+tripcount[start_terminal][end_terminal]


    for i in range(1,100):
        print(i)
        print(tripcount[i])
        # print max(tripcount[i]) #max 3500

# image = np.random.rand(30, 30)
plt.imshow(tripcount, cmap=plt.cm.gray)
plt.colorbar()
plt.show()