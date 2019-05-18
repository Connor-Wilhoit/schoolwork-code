# Stack [LIFO] array-based implementation:

class Stack:
	""" LIFO Stack impl. using a list as the underlying data structure.

		[most code from textbook, just slightly modified as needed]
	"""
	def __init__(self):
		""" Create an empty stack """
		self._data = []

	def __len__(self):
		""" Return # of elements in the stack """
		return len(self._data)
	




	def is_empty(self):
		""" Return true if stack is empty """
		return len(self._data) == 0






	def push(self, e):
		""" Add element 'e' to the top of the stack """
		self._data.append(e)				# new item stored at end of list






	def top(self):
		""" Return (but do NOT remove) the element at the top of the stack.

			Raise Empty exception if the stack is empty.
		"""
		if self.is_empty():
			raise Empty("Stack is empty")
		return self._data[-1]				# the last element in the list
















	def pop(self):
		""" Remove and return the element from the top of the stack (i.e., LIFO)

			Raise 'Empty' exception from 'exceptions.py' if stack is empty.
		"""
		if self.is_empty():
			raise Empty("Stack is empty")
		return self._data.pop()				# remove last item from list
