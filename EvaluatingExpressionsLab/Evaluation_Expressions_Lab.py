#!/usr/local/bin/python3.6
# I honor Parkland's core values by affirming that I have
# followed all academic integrity guidelines for this work.
#
# Connor Wilhoit
from miniceptions import UndefinedVar,PopFromEmpty,AccessFromEmpty
import cgi, cgitb
cgitb.enable()
print("Content-type: text/html\n\n")

def print_title():
	print("<head><title>Mini Language V2 </title></head>")
	print("<body align='center'>################################<br />")
	print("<br />")
	print("<b> Mini Language Impl.V2</br> [Evaluating Multiple Assignments] </b>")
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

def parse_data(clist):
	vlist = []			# clean_list    [do not modify]
	vdict = {}			# variable_list [free to modify as needed]
	excs = [UndefinedVar, PopFromEmpty, AccessFromEmpty]

	for i in range(0, len(clist)):
		item = clist[i]				# get value of current index pos.
		if item == "=":				# we currently have an assignment operator
			rhs = clist[i+1]		# get right hand side of = sign
			lhs = clist[i-1]		# get left hand side of = sign

			if rhs[0] == "(":									# we have start of possible valid expression
				nxt = clist[i+2]
				if nxt[0].isdigit():							# begin evaluation
					symbol = clist[i+3]							# get mathematical operator
					num  = clist[i+4]							# get # on right hand side of operator
					if symbol[0] == "+":						# we have addition
						value = int(nxt) + int(num)
						if lhs in vdict:
							vdict[lhs] = value
						else:
							vdict[lhs] = vdict.get(lhs, value)
					elif symbol[0] == "/":						# we have division
						value = int(nxt) / int(num)
						if lhs in vdict:
							vdict[lhs] = value
						else:
							vdict[lhs] = vdict.get(lhs, value)
					elif symbol[0] == "*":						# we have multiplication, using a star *
						value = int(nxt) * int(num)
						if lhs in vdict:
							vdict[lhs] = value
						else:
							vdict[lhs] = vdict.get(lhs, value)
					elif symbol[0] == "x":						# we have multiplication, using an x
						value = int(nxt) * int(num)
						if lhs in vdict:
							vdict[lhs] = value
						else:
							vdict[lhs] = vdict.get(lhs, value)
					elif symbol[0] == "-":						# we have subtraction
						value = int(nxt) - int(num)
						if lhs in vdict:
							vdict[lhs] = value
						else:
							vdict[lhs] = vdict.get(lhs, value)

				elif nxt[0] == "(":								# we have multiple parenthesis!
					nxt2 = clist[i+3]
					if nxt2[0].isdigit():						# begin evalution
						symbol2 = clist[i+4]
						num2 = clist[i+5]
						nxtsym = clist[i+7]						# get symbol outside parenthesis
						nxtval = clist[i+8]						# get value outside parenthesis
						if symbol2[0] == "+":					# we have addition
							tmpval = int(nxt2) + int(num2)
							if nxtsym[0] == "/":
								value2 = int(tmpval) / int(nxtval)
								if lhs in vdict:
									vdict[lhs] = value2
								else:
									vdict[lhs] = vdict.get(lhs, value2)
							elif nxtsym[0] == "*":
								value2 = int(tmpval) * int(nxtval)
								if lhs in vdict:
									vdict[lhs] = value2
								else:
									vdict[lhs] = vdict.get(lhs, value2)
							elif nxtsym[0] == "+":
								value2 = int(tmpval) + int(nxtval)
								if lhs in vdict:
									vdict[lhs] = value2
								else:
									vdict[lhs] = vdict.get(lhs, value2)
							elif nxtsym[0] == "-":
								value2 = int(tmpval) - int(nxtval)
								if lhs in vdict:
									vdict[lhs] = value2
								else:
									vdict[lhs] = vdict.get(lhs, value2)
							elif nxtsym[0] == "x":
								value2 = int(tmpval) * int(nxtval)
								if lhs in vdict:
									vdict[lhs] = value2
								else:
									vdict[lhs] = vdict.get(lhs, value2)
						elif symbol2[0] == "*":					# we have multiplication, using a star *
							tmpval = int(nxt2) * int(num2)
							if nxtsym[0] == "/":
								value2 = int(tmpval) / int(nxtval)
								if lhs in vdict:
									vdict[lhs] = value2
								else:
									vdict[lhs] = vdict.get(lhs, value2)								
							elif nxtsym[0] == "*":
								value2 = int(tmpval) * int(nxtval)
								if lhs in vdict:
									vdict[lhs] = value2
								else:
									vdict[lhs] = vdict.get(lhs, value2)
							elif nxtsym[0] == "+":
								value2 = int(tmpval) + int(nxtval)
								if lhs in vdict:
									vdict[lhs] = value2
								else:
									vdict[lhs] = vdict.get(lhs, value2)
							elif nxtsym[0] == "-":
								value2 = int(tmpval) - int(nxtval)
								if lhs in vdict:
									vdict[lhs] = value2
								else:
									vdict[lhs] = vdict.get(lhs, value2)
							elif nxtsym[0] == "x":
								value2 = int(tmpval) * int(nxtval)
								if lhs in vdict:
									vdict[lhs] = value2
								else:
									vdict[lhs] = vdict.get(lhs, value2)
						elif symbol2[0] == "/":					# we have division
							tmpval = int(nxt2) / int(num2)
							if nxtsym[0] == "/":
								value2 = int(tmpval) / int(nxtval)
								if lhs in vdict:
									vdict[lhs] = value2
								else:
									vdict[lhs] = vdict.get(lhs, value2)								
							elif nxtsym[0] == "*":
								value2 = int(tmpval) * int(nxtval)
								if lhs in vdict:
									vdict[lhs] = value2
								else:
									vdict[lhs] = vdict.get(lhs, value2)
							elif nxtsym[0] == "+":
								value2 = int(tmpval) + int(nxtval)
								if lhs in vdict:
									vdict[lhs] = value2
								else:
									vdict[lhs] = vdict.get(lhs, value2)
							elif nxtsym[0] == "-":
								value2 = int(tmpval) - int(nxtval)
								if lhs in vdict:
									vdict[lhs] = value2
								else:
									vdict[lhs] = vdict.get(lhs, value2)
							elif nxtsym[0] == "x":
								value2 = int(tmpval) * int(nxtval)
								if lhs in vdict:
									vdict[lhs] = value2
								else:
									vdict[lhs] = vdict.get(lhs, value2)
						elif symbol2[0] == "x":					# we have multiplication, using x
							tmpval = int(nxt2) * int(num2)
							if nxtsym[0] == "/":
								value2 = int(tmpval) / int(nxtval)
								if lhs in vdict:
									vdict[lhs] = value2
								else:
									vdict[lhs] = vdict.get(lhs, value2)								
							elif nxtsym[0] == "*":
								value2 = int(tmpval) * int(nxtval)
								if lhs in vdict:
									vdict[lhs] = value2
								else:
									vdict[lhs] = vdict.get(lhs, value2)
							elif nxtsym[0] == "+":
								value2 = int(tmpval) + int(nxtval)
								if lhs in vdict:
									vdict[lhs] = value2
								else:
									vdict[lhs] = vdict.get(lhs, value2)
							elif nxtsym[0] == "-":
								value2 = int(tmpval) - int(nxtval)
								if lhs in vdict:
									vdict[lhs] = value2
								else:
									vdict[lhs] = vdict.get(lhs, value2)
							elif nxtsym[0] == "x":
								value2 = int(tmpval) * int(nxtval)
								if lhs in vdict:
									vdict[lhs] = value2
								else:
									vdict[lhs] = vdict.get(lhs, value2)
						elif symbol2[0] == "-":					# we have subtraction
							tmpval = int(nxt2) - int(num2)
							if nxtsym[0] == "/":
								value2 = int(tmpval) / int(nxtval)
								if lhs in vdict:
									vdict[lhs] = value2
								else:
									vdict[lhs] = vdict.get(lhs, value2)								
							elif nxtsym[0] == "*":
								value2 = int(tmpval) * int(nxtval)
								if lhs in vdict:
									vdict[lhs] = value2
								else:
									vdict[lhs] = vdict.get(lhs, value2)
							elif nxtsym[0] == "+":
								value2 = int(tmpval) + int(nxtval)
								if lhs in vdict:
									vdict[lhs] = value2
								else:
									vdict[lhs] = vdict.get(lhs, value2)
							elif nxtsym[0] == "-":
								value2 = int(tmpval) - int(nxtval)
								if lhs in vdict:
									vdict[lhs] = value2
								else:
									vdict[lhs] = vdict.get(lhs, value2)
							elif nxtsym[0] == "x":
								value2 = int(tmpval) * int(nxtval)
								if lhs in vdict:
									vdict[lhs] = value2
								else:
									vdict[lhs] = vdict.get(lhs, value2)

					
					
					
			elif rhs[0].isdigit():	# typical case (a number)
				if lhs in vdict:			# key already exists in dictionary
					vdict[lhs] = rhs		# basic key-> value setting
				else:
					vdict[lhs] = vdict.get(lhs, rhs)	# insert key->value into dict
			elif rhs[0].isalpha():						# not-so-typical of a case
				if rhs in vdict:						# var. exists; legal assignment
					vdict[lhs] = vdict[rhs]
				else:
					print("Error: {} not defined <br />".format(rhs))
					break


		elif item == "DUMP":
			if len(vdict) == 0:
				print("Error: no variables in memory! <br />")
				return -1
			else:
				print("<td align='center' width='35%' valign='top'>")
				print("<table bgcolor='cyan' align='center' border='2'>")
				print("<tbody>")
				print("<tr>")
				print("<th colspan='8'>Printing all variables: </th>")
				print("</tr>")
				for k,v in vdict.items():
					print("<td align='center'> {}  {} </td>".format(k,v))
					print("</tr><tr>")
				print("</table>")
				print("<br /><br />")
		elif item == "NAME":
			print("<td align='center' width='35%' valign='top'>")
			print("<table bgcolor='yellow' align='center' border='2'>")
			print("<tbody><tr><th colspan='8'>Connor Wilhoit</th></tr></table><br />")





if __name__ == '__main__':
	print_title()
	make_form()
	process_form()
