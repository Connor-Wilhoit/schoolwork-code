from collections import defaultdict

class Graph:
	""" Needs to be useful for future labs of arbitrary requirements.

	self._edges is a dict of all possible next nodes
	e.g. {'X': ['A', 'B', 'C', 'E'], ...}

	self._weights has all of the weights between two nodes, with the two nodes using a
	tuple as the key
	e.g. {('X', 'A'): 7, ('X', 'B'): 2, ...}

	"""
	self._edges = defaultdict(list)
	self._weights = {}

	def add_edge(self, from_node, to_node, weight):
		# assumes edges are bi-directional (doubly-linked list???)
		self._edges[from_node].append(to_node)
		self._edges[to_node].append(from_node)
		self._weights[(from_node, to_node)] = weight
		self._weights[(to_node, from_node)] = weight

	def dijsktra(self, initial, end):
		# shortest path is a dictionary of nodes,
		# whose value is a tuple of: (previous node, weight)
		shortest_paths = {initial: (None, 0)}
		current_node = initial
		visited = set()

		while current_node != end:
			visited.add(current_node)
			destinations = self._edges[current_node]
			weight_to_current_node = shortest_paths[current_node][1]
			
			for next_node in destinations:
				weight = self._weights[(current_node, next_node)] + weight_to_current_node
				if next_node not in shortest_paths:
					shortest_paths[next_node] = (current_node, weight)
				else:
					current_shortest_weight = shortest_paths[next_node][1]

