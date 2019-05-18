#!/usr/local/bin/python3.6
# I honor Parkland's core values by affirming that I have
# followed all academic integrity guidelines for this work.
#
# Connor Wilhoit
import cgi, cgitb
from graph import Graph
from shortest_paths import shortest_path_lengths, shortest_path_tree
#from shortest_paths import *
cgitb.enable()
print("Content-type: text/html\n\n")



def pretty_tables():
	html_style = """ 
				<style>
					#graphs {
					font-family: 'Trebuchet MS', Arial, Helvetica, sans-serif;
					border-collapse: collapse;
					width: 60%;
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
	print("<head><title>Graph Dijkstra </title></head>")
	print("<body align='center'>###########################################<br />")
	print("<br />")
	print("<b> Shortest Path-Finding of a Graph, using Dijkstra's Algorithm </b>")
	print("<br />")
	print("<br />############################################</body>")



def make_textarea():
	print("<body><hr></hr>")
	print("<form method='POST'>")
	print("<table><tr><td align='center'>Enter Graph Info Here</td></tr><tr>")
	print("<td align='center'><textarea rows='15' cols='55' name='user-vals'>")
	print("</textarea></td></tr><tr><td colspan='2' align='center'>")
	print("<br /><input type='submit' name='go' value='Dijkstra'/></td></tr>")
	print("</table></form></body>")

def print_graph(graph):
	print("<table id='graphs' rowspan='8'>")
	print("<tr><th>VERTEX NAME</th><th>OUTGOING EDGES</th><th>Weight</th><tr>")
	#print("</th></tr>")
	for vertex in graph.vertices():
		print("<tr>")
		print("<td>{}</td>".format(vertex))
		for edge in graph.incident_edges(vertex):
			print("<td>{}</td>".format(edge.endpoints()[1]))
			print("<td>{}</td>".format(edge.element()))
			print("</tr>")
	print("</table>")



def process_input():
	form = cgi.FieldStorage()
	if form.getvalue('user-vals') == None:
		print("Dijkstra can't find the shortest path if there is no path at all! <br />")
		return

	graph = Graph(directed=True)
	raw_data = form.getvalue('user-vals')
	data_list = ''.join(raw_data).split()
	edge_begin = raw_data.find("#end")

	vertex_list = []
	for vertex in data_list:
		if vertex == "#end": break
		else: vertex_list.append(vertex)

	verts = {}
	for vertex in vertex_list:
		verts[vertex] = graph.insert_vertex(vertex)

	velist = raw_data[edge_begin+4:].split()
	ve_list = []
	for item in velist:
		if item[-1] == ",":
			ve_list.append(item.replace(",", ""))
		else:
			ve_list.append(item)

	s_verts = {}
	for i in range(0, len(ve_list), 3):
		vertex = ve_list[i]
		edge = ve_list[i+1]
		weight = ve_list[i+2]
		graph.insert_edge(verts[vertex], verts[edge], weight)
		s_verts[vertex] = weight
		print("Vertex: {}  Edge: {}  Weight: {} <br />".format(vertex, edge, weight))

	print_graph(graph)



	spl = shortest_path_lengths(graph, 'v8')
	#spl = shortest_path_lengths(graph, 'place2')
	#spl = shortest_path_lengths(graph, s_verts['place2'])
	#spl = shortest_path_lengths(graph, verts['place2'])
	print("Shortest Path Lengths:<br />")
	for k,v in spl.items():
		print(k, " -- ", v, "<br />")
	print("Shortest Path Tree:<br />")
	#spt = shortest_path_tree(graph, 'place2', spl)
	spt = shortest_path_tree(graph, 'v1', spl)
	#spt = shortest_path_tree(graph, 'v8', spl)
	#tps = shortest_path_tree(graph, 
	for k,v in spt.items():
		print(k, " -- ", v, "<br />")



if __name__ == '__main__':
	print_title()
	pretty_tables()
	make_textarea()
	process_input()
