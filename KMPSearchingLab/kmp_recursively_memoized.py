#  Set of functions as described by Prof. Urban's Paper, implementing a recursive,
#  memoized KMP-Searching algorithm (but in Python of course)
Prefix = list() 
def KMPmatch(pattern, text):
	""" Driver function for KMPmatch
		Specs: Return position of the first occurence of pattern in text (or -1 if
				pattern does not occur in text)
	"""
	Prefix = [0] * len(pattern)+1
	for i in range(0, len(pattern) ):
		Prefix[i] = -1
	# Q holds for n = m = 0
	return match(pattern, 0, text, 0)

def match(pattern, m, text, n):
	""" Internal K-M-P matching function "match":
		Specs: Given that P and Q hold for parameters n and m, return position in text
				of first occurence of pattern (or -1 if pattern does not occur in text).
	"""
	if (m == len(pattern)):			# End of pattern...
		return n-m					# ... a match
	if (n == len(text)):			# End of text...
		return -1					# ... no match
	# S holds
	return match(pattern, extend(pattern, m, text[n]), text, n+1)


# A pair of mutually recursive functions "extend" and "prefix"

def extend(pattern, j, c):
	""" Specs: Given Q and O <= j < #patter, return length of longest prefix of pattern
				that is a suffix of pattern[0..j-1]^c.
	"""
	if (pattern[j] == c):
		return j+1
	if (j == 0):
		return 0
	return extend(pattern, prefix(pattern, j), c)

"""
def prefix(pattern, i):
	if (i == 1):
		return 0
	else:
		return extend(pattern, prefix(pattern, i-1), pattern[i-1])
"""
def prefix(pattern, i):
	"""  Specs: Given Q and O < i < #pattern, return length of longest proper prefix of
				pattern[0..i-1] that is a suffix of pattern[0..i-1].  Also, store
				computed values in array Prefix, in order to maintain Q.
	"""
	
	if (Prefix[i] == -1):
		if (i == 1):
			Prefix[i] = 0
		else:
			Prefix[i] = extend(pattern, prefix(pattern, i-1), pattern[i-1])
	return Prefix[i]


