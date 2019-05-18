#!/usr/local/bin/python3.6
from graph import Graph
from graph_examples import *

g = figure_14_3()
v = g.insert_vertex("CMI")
#g.insert_edge(v, v, 20)
g.insert_edge(v, v)
g1 = Graph()
g2 = Graph(directed=True)

if __name__ == '__main__':
	print("Vertex Count: ", g.vertex_count(), "\n")

	# print all the vertices:
	for vertex in g.vertices():
		print("Vertex: {}".format(vertex))

	# print all the edges:
	for edge in g.edges():
		print("Edge: {}".format(edge))


	for vertex in g.vertices():
		print("Vertex: {}".format(vertex))
		for edge in g.incident_edges(vertex):
			print("\tEdges: {}".format(edge))
		print("\n")


	graph = Graph(directed=True)
	vertex_str = "vertex1"
	edge   = "vertex2"
	vertex = graph.insert_vertex(vertex_str)
	graph.insert_edge(vertex, edge)
	for vertex in graph.vertices():
		print("Vertex: {}\t".format(vertex))
		for edge in graph.incident_edges(vertex):
			print("Edges: {}".format(edge))
		print("\n")
