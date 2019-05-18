#!/usr/local/bin/python3.6
# I honor Parkland's core values by affirming that I have
# followed all academic integrity guidelines for this work.
#
# Connor Wilhoit

#from miniceptions import UndefinedVar,PopFromEmpty,AccessFromEmpty
import sys
import cgi, cgitb
cgitb.enable()
print("Content-type: text/html\n\n")

def print_outline():
	print("<head><title>Mini Language </title></head>")
	print("<body align='center'>################################<br />")
	print("<br />")
	print("<b> Mini Language Impl. [Assignment Operator ONLY] </b>")
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
	
	output_data(form)


def output_data(cgi_form):
	raw_data = cgi_form.getvalue('user-vals')
	c_data = ''.join(raw_data).split()
	parse_data(c_data)


def parse_data(clist):					# clean_list	[do not modify]
	vlist = []		    				# variable_list	[free to modify as needed]
	vdict = {}		    				# variable_dict [final data structure for output]
	excs = [UndefinedVar, PopFromEmpty, AccessFromEmpty]

	for i in range(0, len(clist)):
		item = clist[i]								# get value of current index pos.
		if item == "=":								# we currently have an operator
			rhs = clist[i+1]						# get right hand side of = sign
			lhs = clist[i-1]						# get left  hand side of = sign
			if rhs[0].isdigit():					# typical case  (a number)
				if lhs in vdict:					# key already exists in dictionary
					vdict[lhs] = rhs				# basic key->value setting
				else:								# key does not exist in dictionary
					vdict[lhs] = vdict.get(lhs, rhs)# must insert key->value into dict.
			elif rhs[0].isalpha():					# not-so-typical of a case
				if rhs in vdict:					# var. exists, so legal assignment
					vdict[lhs] = vdict[rhs]
				else:								# var does not exist, so illegal
					print("Error: {} not defined".format(rhs))
					print("<br /><br />")
					break

		elif item == "DUMP":
			if len(vdict) == 0:
				print("Error: no variables in memory! <br />")
				return -1
			else:
				print("Printing all variables: <br />")
				for k,v in vdict.items():
					print("{}  {} <br />".format(k,v))

		elif item == "NAME":
			print("Connor Wilhoit <br />")

if __name__ == '__main__':
	print_outline()
	make_form()
	process_form()
