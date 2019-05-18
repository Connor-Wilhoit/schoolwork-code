#!/usr/bin/python3
import matplotlib.pyplot as plt
# I honor Parkland's core values by affirming that I have
# followed all academic integrity guidelines for this work.
#
# Connor Wilhoit




# First we need to read in all of the datapoints, place them into arrays,
# split up the strings[lines] by the comma, and finally strip off the '\n' character.

bubble_timer_datapoints      = open("bubble_timer_datapoints.txt", "r")
bubble_touches_datapoints    = open("bubble_touches_datapoints.txt", "r")
insertion_timer_datapoints   = open("insertion_timer_datapoints.txt", "r")
insertion_touches_datapoints = open("insertion_touches_datapoints.txt", "r")

raw_data1 = []
raw_data2 = []
raw_data3 = []
raw_data4 = []
for line in bubble_timer_datapoints:
    raw_data1.append(line)
for line in bubble_touches_datapoints:
    raw_data2.append(line)
for line in insertion_timer_datapoints:
    raw_data3.append(line)
for line in insertion_touches_datapoints:
    raw_data4.append(line)

clean_data1 = [0] * len(raw_data1)
clean_data2 = [0] * len(raw_data2)
clean_data3 = [0] * len(raw_data3)
clean_data4 = [0] * len(raw_data4)

# split up the x,y coordinated, which are comma separated
for i in range(len(raw_data1)):
    clean_data1[i] = raw_data1[i].split(",")
for i in range(len(raw_data2)):
    clean_data2[i] = raw_data2[i].split(",")
for i in range(len(raw_data3)):
    clean_data3[i] = raw_data3[i].split(",")
for i in range(len(raw_data4)):
    clean_data4[i] = raw_data4[i].split(",")




# 'strip' off any trailing newline characters ["\n"]
for i in range(len(clean_data1)):
    clean_data1[i][1] = clean_data1[i][1].strip("\n")
for i in range(len(clean_data2)):
    clean_data2[i][1] = clean_data2[i][1].strip("\n")
for i in range(len(clean_data3)):
    clean_data3[i][1] = clean_data3[i][1].strip("\n")
for i in range(len(clean_data4)):
    clean_data4[i][1] = clean_data4[i][1].strip("\n")


x_1 = []
for i in range(len(clean_data1)):
    x_1.append(int(clean_data1[i][0]))

y_1 = []
for i in range(len(clean_data1)):
    y_1.append(float(clean_data1[i][1]))


x_2 = []
for i in range(len(clean_data2)):
    x_2.append(int(clean_data2[i][0]))

y_2 = []
for i in range(len(clean_data2)):
    y_2.append(int(clean_data2[i][1]))

x_3 = []
for i in range(len(clean_data3)):
    x_3.append(int(clean_data3[i][0]))

y_3 = []
for i in range(len(clean_data3)):
    y_3.append(float(clean_data3[i][1]))

x_4 = []
for i in range(len(clean_data4)):
    x_4.append(int(clean_data4[i][0]))

y_4 = []
for i in range(len(clean_data4)):
    y_4.append(int(clean_data4[i][1]))


if __name__ == '__main__':


    plt.figure(1)
    plt.plot(x_1, y_1, ':', label="BubbleSort-Time", color="red")
    plt.plot(x_3, y_3, '-', label="InsertionSort-Time", color="purple")
    plt.legend(loc='best')
    plt.title("Algorithm Analysis: BubbleSort vs. InsertionSort")
    plt.ylabel("Time Taken by Algorithm [seconds]")
    plt.xlabel("Size of Data [# of elements in list]")




    plt.figure(2)
    plt.plot(x_2, y_2, ':', label="BubbleSort-Steps", color="green")
    plt.plot(x_4, y_4, '-.', label="InsertionSort-Steps", color="blue")
    plt.legend(loc='best')
    plt.title("Algorithm Analysis: BubbleSort vs. InsertionSort")
    plt.ylabel("# of Steps [Array-Touches]")
    plt.xlabel("Size of Data [# of elements in list]")





    plt.show()
