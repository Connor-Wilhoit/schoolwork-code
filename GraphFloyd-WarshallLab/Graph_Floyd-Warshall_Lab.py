#!/usr/local/bin/python3.6
# I honor Parkland's core values by affirming that I have
# followed all academic integrity guidelines for this work.
#
# Connor Wilhoit
import cgi, cgitb
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
	print("<head><title> Graph Floyd-Marshall </title></head>")
	print("<body align='center'>###########################################<br />")
	print("<br />")
	print("<b> Floyd-Marshall Transitive Closure Algorithm Implementation </b>")
	print("<br />")
	print("<br />############################################</body>")


def make_textarea():
	print("<body><hr></hr>")
	print("<form method='POST'>")
	print("<table><tr><td align='center'>Enter Graph Info Here</td></tr><tr>")
	print("<td align='center'><textarea rows='15' cols='55' name='user-vals'>")
	print("</textarea></td></tr><tr><td colspan='2' align='center'>")
	print("<br /><input type='submit' name='go' value='Floyd-Marshall'/></td></tr>")
	print("</table></form></body>")

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


def process_input():
	form = cgi.FieldStorage()
	if form.getvalue('user-vals') == None:
		print("No data input == no Floyd-Marshall algo execution! <br />")
		return

	graph = Graph(directed=True)
	raw_data = form.getvalue('user-vals')
	data_list = ''.join(raw_data).split()
	edge_begin = raw_data.find("#end")
	print("raw_data: ", raw_data, "<br />")
	print("data_list: ", data_list, "<br />")






if __name__ == '__main__':
	print_title()
	pretty_tables()
	make_textarea()
	process_input()
