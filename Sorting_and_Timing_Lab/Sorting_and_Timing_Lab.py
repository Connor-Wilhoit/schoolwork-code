#!/usr/local/bin/python3.6
# I honor Parkland's core values by affirming that I have
# followed all academic integrity guidelines for this work.
#
# Connor Wilhoit
# I need four lines, and four functions:
# --> 1) Line timing BubbleSort on n # of elements
# --> 2) Line timeing InsertionSort on n # of elements
# --> 3) Number of visits BubbleSort makes on n # of elements
# --> 4) number of visits InsertionSort makes on n # of elements
#
#
# There needs to be at least 200 different points for each line,
# using sizes like 10000.
#	--> So this means each line needs to sort at least 200 different lists,
#		where each list contains at least 10000 elements.
#
#
#
# The graph's y-axis will show either (a) Time taken or (b) Steps taken
#	--> There will be two lines for both (a) and (b) for each algorithm
# The graph's x-axis will show the # of elements (n elements) [size of data]
#
#
# Write data points out to csv files (1 file for each line initially) w/each line
# treated as an (x,y) coordinate; For example, if using 'bubble_sort' on a list of '10000'
# elements, then write the data points out as:
#			(10000, 201) <-- 201 being time in seconds, or:
#			(10000, 15)  <-- 15 being the # of steps taken
#
#
# One all lines are created, and all four csv files are created, import the csv files
# into a separate Python script, using matplotlib & numpy, and plot the lines graphically.
#
#
#
#
from time import time
from time import clock
from algorithms import bubble_sort
from algorithms import insertion_sort
from os import getrandom
from random import seed
from random import randint


seed(getrandom(256))	# seed PNRG w/256-byte seed


def bubble_timer():
		# This is the function to time(in seconds) the bubble_sort algorithm.
		# Filename: 'bubble_timer_datapoints.txt'
		bp = open("bubble_timer_datapoints.txt", "w")
		#for size in range(1, 201):	# 200 datapoints, each a list of 5000-15000 elements
		#for size in range(1, 2):	# range of 1-11 (10 lists[datapoints]) for testing
		for size in range(1, 51):
				alist = []
				for i in range(randint(5000, 15000)):
						alist.append(randint(1, 1000000))
				print("Starting bubble_sort on list #: {}\n".format(size))
				start_time  = time()
				bubble_sort(alist)
				end_time    = time()
				bubble_time = end_time - start_time
				bp.write("{},{}\n".format(len(alist), bubble_time))
				print("Finished bubble_sort'ing list #: {}\n".format(size))



def insertion_timer():
		# This is the function to time(in seconds) the insertion_sort algorithm.
		# Filename: 'insertion_timer_datapoints.txt'
		ip = open("insertion_timer_datapoints.txt", "w")
		#for size in range(1, 201):
		#for size in range(1, 2):
		for size in range(1, 51):
				alist = []
				for i in range(randint(5000, 15000)):
						alist.append(randint(1, 1000000))
				print("Starting insertion_sort on list #: {}\n".format(size))
				start_time     = time()
				insertion_sort(alist)
				end_time       = time()
				insertion_time = end_time - start_time
				ip.write("{},{}\n".format(len(alist), insertion_time))
				print("Finished insertion_sort'ing list #: {}\n".format(size))



def bubble_touches():
		# This is the function to count the # of steps taken by the
		# bubble_sort algorithm.
		# There are 2 steps(touches [list accesses]) on the comparison line, and
		# there are 4 steps(touches [list accesses]) on the swap line
		# Filename: 'bubble_touches_datapoints.txt'
		bs = open("bubble_touches_datapoints.txt", "w")
		#for size in range(1, 201):
		#for size in range(1, 3):
		for size in range(1, 51):
				alist   = []
				touches = 0
				for i in range(randint(5000, 15000)):
						alist.append(randint(1, 1000000))
				print("Starting bubble_stepper on list #: {}\n".format(size))
				for i in range(len(alist)):
						for j in range(len(alist)-1):
								touches += 2
								if alist[j] > alist[i]:
										touches += 4
										alist[j],alist[i]=alist[i],alist[j]
				# End of bubble-sorting w/touch count
				bs.write("{},{}\n".format(len(alist), touches))
				print("Finished bubble_step'ing of list #: {}\n".format(size))


def insertion_touches():
		# This is the function to count the # of steps taken by the
		# insertion_sort algorithm.
		# Filename: 'insertion_touches_datapoints.txt'
		it = open("insertion_touches_datapoints.txt", "w")
		#for size in range(1, 201):
		#for size in range(1, 3):
		for size in range(1, 51):
				alist = []
				touches = 0
				for i in range(randint(5000, 15000)):
						alist.append(randint(1, 1000000))
				print("Starting insertion_stepper on list #: {}\n".format(size))
				for i in range(1, len(alist)):
						touches += 1
						current_value = alist[i]
						position = i
						touches += 1
						while position > 0 and alist[position-1] > current_value:
								touches += 3
								alist[position] = alist[position-1]
								position -= 1
								alist[position] = current_value
				# End of insertion-sorting w/touch count
				it.write("{},{}\n".format(len(alist), touches))
				print("Finished insertion_step'ing of list #: {}\n".format(size))





if __name__ == '__main__':
		print("Beginning timing of the 'bubble_sort' algorithm\n")
		bubble_timer()
		print("Done timing bubble_sort\n")
		print("Now beginning timing of the 'insertion_sort algorithm\n")
		insertion_timer()
		print("Done timing insertion_sort\n")
		print("Now beginning step-counting of the 'bubble_sort' algorithm\n")
		bubble_touches()
		print("Done counting steps of bubble_sort\n")
		print("Now beginning step-counting of the 'insertion_sort' algorithm\n")
		insertion_touches()
		print("Done counting steps of insertion_sort\n")
		print("All done!\n")
