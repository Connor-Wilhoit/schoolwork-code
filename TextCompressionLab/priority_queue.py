import positional_list
from exceptions import Empty


class PriorityQueueBase:
	""" Abstract base class for a priority queue """
	class _Item:
		""" Lightweight composite to store priority-queue items """
		__slots__ = '_key', '_value'

		def __init__(self, k, v):
			self._key = k
			self._value = v

		def __lt__(self, other):
			""" compare items based on their keys """
			return self._key < other._key
		# End of _Item nested class

	# Back to priority_queue_base class definition code:
	def is_empty(self):
		""" Return True if the priority queue is empty.

			-this function is based on a presumed __len__ implmentation
		"""
		return len(self) == 0


""" Table of comparisons between slow and fast priority queues:
	Operation:		Slow(unsorted list):		Fast(sorted list):
	len				O(1)						O(1)
	is_empty		O(1)						O(1)
	add				O(1)						O(n)
	min				O(n)						O(1)
	remove_min		O(n)						O(1)

"""


class PriorityQueue(PriorityQueueBase):
	""" minimum-oriented priority queue using a sorted list. """
	def __init__(self):
		self._data = positional_list.PositionalList()

	def __len__(self):
		return len(self._data)

	def add(self, key, value):
		newest = self._Item(key,value)
		walk = self._data.last()
		while walk is not None and newest < walk.element():
			walk = self._data.before(walk)
		if walk is None:
			self._data.add_first(newest)	# new key is smallest
		else:
			self._data.add_after(walk,newest)

	def min(self):
		""" Return but do NOT remove (k,v) tuple w/minimum key """
		if self.is_empty():
			raise Empty("Priority Queue is empty!")
		p = self._data.first()
		item = p.element()
		return (item._key, item._value)

	def remove_min(self):
		if self.is_empty():
			raise Empty("Priority Queue is empty!")
		item = self._data.delete(self._data.first())
		return (item._key, item._value)
