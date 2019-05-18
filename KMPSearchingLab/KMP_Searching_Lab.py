#!/usr/local/bin/python3.6
# I honor Parkland's core values by affirming that I have
# followed all academic integrity guidelines for this work.
#
# Connor Wilhoit
import cgi,cgitb
from find_kmp import find_kmp, compute_kmp_fail
cgitb.enable()
print("Content-type: text/html\n\n")

def print_title():
	print("<head><title>KMP Searching Lab </title></head>")
	print("<body align='center'>###########################################<br />")
	print("<br />")
	print("<b> Searching For Strings Using KMP </b>")
	print("<br />")
	print("<br />###########################################</body>")


def make_textarea():
	print("<body><hr></hr>")
	print("<form method='POST'>")
	print("<table><tr>")
	print("<td align='center'>Enter Lots O' Words Below</td></tr><tr>")
	print("<td align='center'>")
	print("<textarea rows='10' cols='55' name='user-vals'></textarea>")
	print("</td></tr><tr><td colspan='2' align='center'>")
	print("<br>")
	print("Enter search term:<input type='text' name='search-word'>")
	print("<input type='submit' name='go' value='ProcessData' /></td></tr></table>")
	print("</form></body>")

def process_form():
	form = cgi.FieldStorage()
	
	if form.getvalue('user-vals') == None:
		print("Please give me some words to search through!<br>")
		return
	elif form.getvalue('search-word') == None:
		print("Please enter a search term!<br>")
		return

	raw_data = form.getvalue('user-vals')
	search_term = form.getvalue('search-word')
	kmp_result = find_kmp(raw_data, search_term)
	if kmp_result == -1:
		print("{} Not Found <br>".format(search_term))
		return
	print("<td align='center' width='35%' valign='top'>")
	print("<table bgcolor='cyan' align='center' border='1'>")
	print("<tbody><tr><th colspan='8'> KMP Algo's Results: </th></tr>")
	print("<tbody><tr><th colspan='8'>Searched-Term | Position </th></tr>")
	print("<td align='center'> {} </td><td> {} </td>".format(search_term, kmp_result))
	print("</table>")




if __name__ == '__main__':
	print_title()
	make_textarea()
	process_form()
