#!/usr/local/bin/python3.6
# I honor Parkland's core values by affirming that I have
# followed all academic integrity guidelines for this work.
#
# Connor Wilhoit
import cgi, cgitb
from graph import Graph
from bfs import BFS, BFS_complete
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


def print_title():
	print("<head><title> Graph BFS </title></head>")
	print("<body align='center'>###########################################<br />")
	print("<br />")
	print("<b> Breadth-First-Search on an unweighted, directed graph </b>")
	print("<br />")
	print("<br />############################################</body>")


def make_textarea():
	print("<body><hr></hr>")
	print("<form method='POST'>")
	print("<table><tr><td align='center'>Enter Graph Info Here</td></tr><tr>")
	print("<td align='center'><textarea rows='15' cols='55' name='user-vals'>")
	print("</textarea></td></tr><tr><td colspan='2' align='center'>")
	print("<br /><input type='submit' name='go' value='Perform BFS'/></td></tr>")
	print("</table></form></body>")


def process_input():
	form = cgi.FieldStorage()
	if form.getvalue('user-vals') == None:
		print("No BFS execution can take place if I have no input data! <br />")
		print("Please input vertices and edges in the textarea <br />")
		return

	graph = Graph(directed=True)
	raw_data = form.getvalue('user-vals')
	data_list = ''.join(raw_data).split()
	edge_begin = raw_data.find("#end")
	
	# get paths to calculate
	paths_list = []
	#for v in data_list:
	#	if v == "START":
	#		paths_list.append(v)
	#	elif v == "#end": break

	# get all vertices into a single list
	vlist = []
	for vertex in data_list:
		if vertex == "#end": break
		else: vlist.append(vertex)

	# cleanup data into a more usable format
	velist = raw_data[edge_begin+4:].split()
	ve_list = []
	for item in velist:
		if item[-1] == ",": ve_list.append(item.replace(",", ""))
		else: ve_list.append(item)
	
	# create a lookup table of all vertices, to be used later when inserting edges
	verts = {}
	for vertex in vlist: verts[vertex] = graph.insert_vertex(vertex)
	for i in range(0, len(ve_list), 2):
		vertex = ve_list[i]
		edge   = ve_list[i+1]
		graph.insert_edge(verts[vertex], verts[edge])

	print_graph(graph)
	print("<br />")
	forest = BFS_complete(graph)
	print("Here is the 'forest' returned by the 'BFS_complete(graph)' Function: <br />")
	for k,v in forest.items():
		print(k, " -- ", v, "<br />")




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


if __name__ == '__main__':
	print_title()
	pretty_tables()
	make_textarea()
	process_input()
