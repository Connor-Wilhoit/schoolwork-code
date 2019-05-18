def bubble_sort(alist):
    for i in range(len(alist)):
        for j in range(len(alist)-1):
            if alist[j] > alist[i]:
                alist[j],alist[i]=alist[i],alist[j]



def insertion_sort(alist):
    for i in range(1, len(alist)):
        current_value = alist[i]
        position      = i
        while position > 0 and alist[position-1] > current_value:
            alist[position] = alist[position-1]
            position -= 1
            alist[position] = current_value


# The next 3 algorithms are examples of "Prefix Average" algorithms, and each function
# is a different timing-type of algorithm:

# A Quadratic-Time Algorithm:
def prefix_average1(S):
	# Return list such that, for all j, A[j] equals average of S[0], ..., S[j]
	n = len(S)
	A = [0] * n		# create new list of n zeros
	for j in range(n):
		total = 0	# begin computing S[0] + ... + S[j]
		for i in range(j + 1):
			total += S[i]
			A[j] = total / (j+1)		# record the average
	return A




if __name__ == '__main__':
		print("Pre-My-BubbleSort:")
		ilist = [1, 56, 4, 11, 0, 19, 11, 55, 72, 5, 10, 15, 1, 11, 100, 3]
		print(ilist)
		print("Post-My-BubbleSort:")
		bubble_sort(ilist)
		print(ilist)
		print("\n")

		print("Pre-InsertionSort:")
		slist = [1, 56, 4, 11, 0, 19, 11, 55, 72, 5, 10, 15, 1, 11, 100, 3]
		print(slist)
		print("Post-InsertionSort:")
		insertion_sort(slist)
		print(slist)
		print("\n")
