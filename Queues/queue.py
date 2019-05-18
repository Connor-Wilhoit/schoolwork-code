# Queue [FIFO] array-based implementation:

class Queue:
	""" FIFO Queue impl. using a list as the underlying data structure.

		[most code from textbook, just slightly modified as needed]
	"""
	DEFAULT_CAPACITY = 10

	def __init__(self):
		""" Create an empty queue. """
		self._data  = [None] * Queue.DEFAULT_CAPACITY
		self._size  = 0
		self._front = 0


	def __len__(self):
		return self._size




	def is_empty(self):
		""" Return true if the queue is empty """
		return self._size == 0









	def first(self):
		""" Return (but do NOT remove) the element at the front of the queue.

			Raise Empty exception if the queue is empty.
		"""
		if self.is_empty():
			raise Empty("Queue is empty")
		return self._data[self._front]


	def dequeue(self):
		""" Remove AND return the first element of the queue (i.e.,FIFO)

			Raise 'Empty' exception if the queue is empty.
		"""
		if self.is_empty():
			raise Empty("Queue is empty")
		answer = self._data[self._front]
		self._data[self._front] = None			# help garbage collection
		self._front = (self._front + 1) % len(self._data)
		self._size -= 1
		return answer





	def enqueue(self, e):
		""" Add an element to the BACK of the queue (i.e., FIFO) """
		if self._size == len(self._data):
			self._resize(2 * len(self._data))	# double size of underlying array

		avail             = (self._front + self._size) % len(self._data)
		self._data[avail] = e
		self._size       += 1



	def _resize(self, cap):
		old = self._data
		self._data = [None] * cap
		walk = self._front
		for k in range(self._size):
			self._data[k] = old[walk]
			walk = (1 + walk) % len(old)
		self._front = 0
