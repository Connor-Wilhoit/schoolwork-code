#!/usr/local/bin/python3.6
# I honor Parkland's core values by affirming that I have
# followed all academic integrity guidelines for this work.
#
# Connor Wilhoit
import cgi, cgitb
from graph import Graph
from dfs import *
cgitb.enable()
print("Content-type: text/html\n\n")


def pretty_tables():
	html_style = """
				<style>
					#graphs {
					font-family: 'Trebuchet MS', Arial, Helvetica, sans-serif;
					border-collapse: collapse;
					width: 100%;
					}
					#graphs td, #graphs tr {
					border: 1px solid #ddd;
					padding: 8px;
					}
					#graphs tr:nth-child(even){background-color: #f2f2f2;}
					#graphs tr:hover {background-color: #ddd;}
					#graphs th {
					padding-top: 12px;
					padding-bottom: 12px;
					text-align: center;
					background-color: #E01195;
					color: white;
					}
				</style>
				 """
	print(html_style)


def print_graph(graph):
	print("<table id='graphs' rowspan='8'><tr><th>VERTEX NAME</th><th>OUTGOING EDGES")
	print("</th></tr>")
	for vertex in graph.vertices():
		print("<tr>")
		print("<td>{}</td>".format(vertex))
		for edge in graph.incident_edges(vertex):
			print("<td>{}</td>".format(edge.endpoints()[1]))
		print("</tr>")
	print("</table>")


def print_title():
	print("<head><title> Graph w/DFS & Cycles Lab </title></head>")
	print("<body align='center'>########################################<br />")
	print("<br />")
	print("<b> Implementation of Depth-First-Search and Cycles </b>")
	print("<br />")
	print("<br />########################################</body>")


def make_textarea():
	print("<body><hr></hr>")
	print("<form method='POST'>")
	print("<table><tr><td align='center'>Enter Info Here</td></tr><tr>")
	print("<td align='center'><textarea rows='10' cols='55' name='user-vals'>")
	print("</textarea></td></tr><tr><td colspan='2' align='center'>")
	print("<br /><input type='submit' name='go' value='Cyclic vs. Acyclic'/></td></tr>")
	print("</table></form></body>")


def process_input():
	form = cgi.FieldStorage()

	if form.getvalue('user-vals') == None:
		print("Without any vertices or edges, the graph is neither cyclic nor acyclic!")
		print("<br />Please input some vertices and edges! :) <br />")
		return

	graph = Graph(directed=True)
	raw_data = form.getvalue('user-vals')
	data_list = ''.join(raw_data).split()
	edge_begin = raw_data.find("#end")
	vlist = []
	for vertex in data_list:
		if vertex == "#end": break
		else: vlist.append(vertex)
	velist = raw_data[edge_begin+4:].split()
	ve_list = []
	for item in velist:
		if item[-1] == ",": ve_list.append(item.replace(",", ""))
		else: ve_list.append(item)
	verts = {}
	for vertex in vlist: verts[vertex] = graph.insert_vertex(vertex)

	for i in range(0, len(ve_list), 2):
		vertex = ve_list[i]
		edge   = ve_list[i+1]
		graph.insert_edge(verts[vertex], verts[edge])
	forest = DFS_complete(graph)

	visited = {}
	recurring = {}
	is_cyclic = False
	for k in forest.keys():
		visited[k] = False
		recurring[k] = False
	i = 0
	for vertex in graph.vertices():
		visited[vertex] = True
		for edge in graph.incident_edges(vertex):
			newv = edge.endpoints()[1]
			for e in graph.incident_edges(newv):
				opp = e.opposite(newv)
				if visited[opp] == True:
					is_cyclic = True

			opposite = edge.opposite(vertex)
			if visited[opposite] == True:
				is_cyclic = True
		visited[vertex] = False
	
	print("Is the graph cyclic?? ---> {} <br />".format(is_cyclic))
	print("<br />")
	print_graph(graph)




if __name__ == '__main__':
	print_title()
	pretty_tables()
	make_textarea()
	process_input()
