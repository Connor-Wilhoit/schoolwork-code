#!/usr/local/bin/python3.6
# I honor Parkland's core values by affirming that I have
# followed all academic integrity guidelines for this work.
#
# Connor Wilhoit
import cgi,cgitb
from graph import Graph
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
					#graphs td, #graphs th {
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

#background-color: #4CAF50;  <--- green
#background-color: #C0C0C0;  <--- silver
#background-color: #FF0000;  <--- red
#background-color: #E01195;  <--- purpleish/pinkish
#background-color: #460EE4;  <--- blue

def print_title():
	print("<head><title> Graph IO Lab </title></head>")
	print("<body align='center'>#########################################<br />")
	print("<br />")
	print("<b> Basic Implementation of a Graph Data Structure </b>")
	print("<br />")
	print("<br />########################################</body>")


def make_textarea():
	print("<body><hr></hr>")
	print("<form method='POST'>")
	print("<table><tr><td align='center'>Enter Info Here</td></tr><tr>")
	print("<td align='center'><textarea rows='10' cols='55' name='user-vals'>")
	print("</textarea></td></tr><tr><td colspan='2' align='center'>")
	print("<br /><input type='submit' name='go' value='CreateGraph' /></td></tr></table>")
	print("</form></body>")


def process_input():
	form = cgi.FieldStorage()

	if form.getvalue('user-vals') == None:
		print("No graph shall exist without vertices and edges!<br />")
		print("(please input some data :) )")
		return

	raw_data = form.getvalue('user-vals')
	data_list = ''.join(raw_data).split()
	edge_list = [] 
	graph = Graph(directed=True)
	vertex_list = []

	for vertex in data_list:
		if vertex == "#end": break
		else: vertex_list.append(vertex)

	verts = {}
	for vertex in vertex_list:
		verts[vertex] = graph.insert_vertex(vertex)

	edge_begin = raw_data.find("#end")
	vertex_edge_list = raw_data[edge_begin+4:].split()

	ve_list = []
	for item in vertex_edge_list:
		if item[-1] == ",":
			ve_list.append(item.replace(",", ""))
		else:
			ve_list.append(item)

	for i in range(0, len(ve_list), 2):
		vertex = ve_list[i]
		edge   = ve_list[i+1]
		graph.insert_edge(verts[vertex], verts[edge])




	# Final Output:
	print("<table id='graphs' rowspan='4'><tr><th>VERTEX NAME</th><th>OUTGOING EDGES")
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
