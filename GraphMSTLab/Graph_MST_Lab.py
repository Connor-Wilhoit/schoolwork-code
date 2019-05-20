#!/usr/local/bin/python3.6
# I honor Parkland's core values by affirming that I have
# followed all academic integrity guidelines for this work.
#
# Connor Wilhoit
import cgi, cgitb
from graph import Graph
from mst import MST_PrimJarnik,MST_Kruskal
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
	print("<head><title> Graph MST </title></head>")
	print("<body align='center'>###########################################<br />")
	print("<br />")
	print("<b> Minimum-Spanning-Tree Algorithm Implementation </b>")
	print("<br />")
	print("<br />############################################</body>")


def make_textarea():
	print("<body><hr></hr>")
	print("<form method='POST'>")
	print("<table><tr><td align='center'>Enter Graph Info Here</td></tr><tr>")
	print("<td align='center'><textarea rows='15' cols='55' name='user-vals'>")
	print("</textarea></td></tr><tr><td colspan='2' align='center'>")
	print("<br /><input type='submit' name='go' value='MST'/></td></tr>")
	print("</table></form></body>")


def print_graph(graph):
	print("<table id='graphs' rowspan='4'><tr><th>VERTEX NAME</th><th>OUTGOING EDGES")
	print("</th></tr>")
	for vertex in graph.vertices():
		print("<tr>")
		print("<td>{}</td>".format(vertex))
		for edge in graph.incident_edges(vertex):
			print("<td>{}</td>".format(edge.endpoints()[1]))
		print("</tr>")
	print("</table>")

def print_mst_graph(graph):
	print("<table id='graphs'><tr><th>VERTEX NAME</th><th>OUTGOING EDGES<th>WEIGHT")
	print("</th></tr>")
	for item in graph:
		print("<tr>")
		print("<td>{}</td><td>{}</td><td>{}</td>"
				.format(item.endpoints()[0], item.endpoints()[1], item.element()))
		print("</tr>")
	print("</table>")


def process_input():
	form = cgi.FieldStorage()
	if form.getvalue('user-vals') == None:
		print("No data input == no spanning tree algo execution! <br />")
		return

	graph = Graph(directed=False)
	raw_data = form.getvalue('user-vals')
	data_list = ''.join(raw_data).split()
	edge_begin = raw_data.find("#end")
	
	# Setup a list of the vertices 
	vertex_list = []
	for vertex in data_list:
		if vertex == "#end": break
		else: vertex_list.append(vertex)
	
	#  Insert newly parsed vertices from "vertex_list" into a dictionary, "verts"
	verts = {}
	for vertex in vertex_list:
		verts[vertex] = graph.insert_vertex(vertex)
	vertex_edge_list = raw_data[edge_begin+4:].split()

	ve_list = []
	for item in vertex_edge_list:
		if item[-1] == ",": ve_list.append(item.replace(",", ""))
		else: ve_list.append(item)
	
	for i in range(0, len(ve_list), 3):
		vertex = ve_list[i]
		edge   = ve_list[i+1]
		weight = ve_list[i+2]
		graph.insert_edge(verts[vertex], verts[edge], weight)

	total_tree_weight_pj = []
	total_tree_weight_k = []
	prim_jarnik_graph = MST_PrimJarnik(graph)
	kruskal_graph     = MST_Kruskal(graph)

	print("Prim-Jarnik Creation: <br />")
	for item in prim_jarnik_graph:
		print(item.endpoints()[0],
				"-->", item.endpoints()[1], " : ", item.element(), "<br />")
		total_tree_weight_pj.append(float(item.element()))

	print("<br />Kruskal Creation: <br />")
	for item in kruskal_graph:
		print(item.endpoints()[0],
				"-->", item.endpoints()[1], " : ", item.element(), "<br />")
		total_tree_weight_k.append(float(item.element()))
	
	result_pj = 0
	for weight in total_tree_weight_pj:
		result_pj += weight
	result_k = 0
	for weight in total_tree_weight_k:
		result_k += weight
	
	print("Total Weight of the Kruskal Tree: {} <br />".format(result_k))
	print("Total Weight of the Prim-Jarnik Tree: {} <br />".format(result_pj))

	print("<br />Default Graph:<br />")
	print_graph(graph)
	print("<br />Kruskal MST Graph -- Total Weight:{} <br />".format(result_k))
	print_mst_graph(kruskal_graph)
	print("<br />Prim-Jarnik MST Graph -- Total Weight:{}<br />".format(result_pj))
	print_mst_graph(prim_jarnik_graph)





if __name__ == '__main__':
	print_title()
	pretty_tables()
	make_textarea()
	process_input()
