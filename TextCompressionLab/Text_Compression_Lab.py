#!/usr/local/bin/python3.6
# I honor Parkland's core values by affirming that I have
# followed all academic integrity guidelines for this work.
#
# Connor Wilhoit

from priority_queue import PriorityQueue
from copy import deepcopy
from collections import deque
import cgi, cgitb
cgitb.enable()
print("Content-type: text/html\n\n")

def print_title():
	print("<head><title>Huffman Compression </title></head>")
	print("<body align='center'>################################<br />")
	print("<br />")
	print("<b> Text Compression using Huffman Coding </b>")
	print("<br />")
	print("<br />################################</body>")


def make_form():
	print("<body>")
	print("<table width='100%'>")
	print("<tr><td align='center' colspan='2'>")
	print("<hr></td></tr></hr></table>")
	print("<form method='POST'>")
	print("<table>")
	print("<tr>")
	print("<td align='center'>Enter Your Data Below</td>")
	print("</tr>")
	print("<tr>")
	print("<td align='center'>")
	print("<textarea rows='10' cols='55' name='user-vals'></textarea>")
	print("</td>")
	print("</tr>")
	print("<tr>")
	print("<td colspan='2' align='center'>")
	print("<input type='submit' name='go' value='ProcessData' /></td>")
	print("</tr>")
	print("</table>")
	print("</form>")
	print("</body>")


def process_form():
	form = cgi.FieldStorage()
	if form.getvalue('user-vals') == None:
		print("I can't process any data if you don't give me any!")
		print("<br /> Please input some data! :D <br />")
		return

	process_data(form)


def process_data(cgi_form):
	raw_data = cgi_form.getvalue('user-vals')
	c_data = ''.join(raw_data).split()
	char_lst = [c for c in str(c_data)]
	s = list(c_data[0])
	frequencies = {}
	for c in s:
		frequencies[c] = frequencies.get(c,s.count(c))
	# put this output into an HTML table (vastly cleaner-looking output!)
	print("<td align='center' width='35%' valign='top'>")
	print("<table bgcolor='antiquewhite' align='left' border='2'>")
	print("<tbody>")
	print("<tr>")
	print("<th colspan='8'>Character Frequency</th>")
	print("</tr>")
	i = 0
	print("<tr>")	# <tr> is a row (in a table)
	for key,val in frequencies.items():
		# <td> is a table data/cell
		print("<td align='center'> {} -> {} </td>".format(key,val))
		i += 1
		if i % 4 == 0:
			print("</tr>")
			print("<tr>")
	print("</table>")


	# for the codes dictionary:
	# --the key is the letter
	# --the value is the Huffman binary code in string representation
	codes = {}
	
	pq = PriorityQueue()
	for key,val in frequencies.items():
		pq.add(val,key)
	
	while len(pq) > 1:
		freq1, str1 = pq.remove_min()
		freq2, str2 = pq.remove_min()
		for char in str1:
			if char in codes:
				codes[char] = '0' + codes[char]
			else:
				codes[char] = codes.setdefault(char, "0")
				codes[char] = '0' + codes[char]
		for char in str2:
			if char in codes:
				codes[char] = '1' + codes[char]
			else:
				codes[char] =  codes.setdefault(char, "1")
				codes[char] = '1' + codes[char]


		pq.add(freq1+freq2, str1+str2)

	f,T = pq.remove_min()	# grab last key,val pair

	print("<td align='center' width='35%' valign='top'>")
	print("<table bgcolor='antiquewhite' align='center' border='2'>")
	print("<tbody>")
	print("<tr>")
	print("<th colspan='8'>Huffman Codes</th>")
	print("</tr>")
	j = 0
	print("<tr>")
	for key,val in codes.items():
		print("<td align='center'> {} --> {} </td>".format(key,val))
		j += 1
		if j % 4 == 0:
			print("</tr>")
			print("<tr>")
	print("</table>")
	print("<br /><br />")


	# show the # of bits we have saved (compressed):
	print("<td align='center' width='35%' valign='right'>")
	print("<table bgcolor='antiquewhite' align='left' border='2'>")
	print("<tbody>")
	print("<tr>")
	print("<th colspan='8'>Pre-Compressed Bits</th>")
	print("</tr>")
	jj = 0
	for k,v in frequencies.items():
		print("<td align='center'> {} : {} </td>".format(k, (v*8)))
		jj += 1
		if jj % 4 == 0:
			print("</tr>")
			print("<tr>")
	print("</table>")
	print("<td align='center' width='35%' valign='right'>")
	print("<table bgcolor='antiquewhite' align='center' border='2'>")
	print("<tbody>")
	print("<tr>")
	print("<th colspan='8'>Huffman-Compressed Bits</th>")
	print("</tr>")
	kk = 0
	for k,v in codes.items():
		print("<td align='center'> {} : {} </td>".format(k, len(v)))
		kk += 1
		if kk % 4 == 0:
			print("</tr>")
			print("<tr>")
	print("</table>")
	print("<br /><br />")






if __name__ == '__main__':
	print_title()
	make_form()
	process_form()
