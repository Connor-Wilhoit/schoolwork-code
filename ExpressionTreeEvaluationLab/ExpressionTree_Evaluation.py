#!/usr/local/bin/python3.6
# I honor Parkland's core values by affirming that I have
# followed all academic integrity guidelines for this work.
#
# Connor Wilhoit
import cgi,cgitb
from stack import Stack
from queue import Queue
from expression_tree import ExpressionTree
from copy import deepcopy
cgitb.enable()
print("Content-type: text/html\n\n")

def print_title():
	print("<head><title>Mini Language V2 </title></head>")
	print("<body align='center'>################################<br />")
	print("<br />")
	print("<b> Mini Language Impl.V2</br> [Evaluating Multiple Expressions] </b>")
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
	c_data = tokenize(cgi_form)
	mod_c_data = []
	c_data_copy = deepcopy(c_data)
	raw_data = cgi_form.getvalue('user-vals')
	tokenized_list = [line for line in raw_data.splitlines()]
	rev_list = list(reversed(tokenized_list))
	rev_token_list = tokenize_V2(reversed(tokenized_list))
	vdict = {}
	while rev_list:
		expression = rev_list[-1]
		token = tokenize_V2(expression)
		tree = build_expression_tree(token)
		possible_variable = str(tree)
		if possible_variable[0].isalpha():
			if expression[0].isalpha() and expression[0].islower():
				space = expression.find(" ")
				var_name = expression[0:space]
				if possible_variable in vdict:
					vdict[var_name] = vdict[possible_variable]
				elif possible_variable not in vdict:
					print("Error: {} does not exist! [illegal assignment] <br />"
							.format(possible_variable))
					break
		if expression[0].isalpha():
			if expression[0].islower():
				if expression[0] == "v":
					space = expression.find(" ")
					var_name = expression[0:space]
					if var_name in vdict:
						try:
							answer = tree.evaluate()
							vdict[var_name] = answer
						except: pass
					else:
						try:
							answer = tree.evaluate() 
							vdict[var_name] = vdict.get(var_name, answer)
						except: pass
		if expression == "NAME":
			print("<td align='center' width='35%' valign='top'>")
			print("<table bgcolor='yellow' align='center' border='2'>")
			print("<tbody><tr><th colspan='8'>Connor Wilhoit</th></table>")
		if expression == "DUMP":
			print("<td align='center' width='35%' valign='top'>")
			print("<table bgcolor='cyan' align='center' border='2'>")
			print("<tbody><tr><th colspan='8'>Printing all variables: </th></tr>")
			for k,v in vdict.items():
				print("<td align='center'> {}  {}  </td></tr><tr>".format(k,v))
			print("</table>")
		try: results_list.append(tree.evaluate())
		except: pass
		rev_list.pop()
		print("<br />")





def tokenize(raw):
	""" utility to create "tokens" which can be put into an ExpressionTree
		for doing the actual arithmetic.
	"""
	raw_data = raw.getvalue('user-vals')
	c_data = ''.join(raw_data).split()
	return c_data



def tokenize_V2(raw):
	c_data = ''.join(raw).split()
	return c_data




def build_expression_tree(tokens):
	""" Returns an ExpressionTree based upon a tokenized expression. """
	S = []												# use list as a stack
	for t in tokens:
		if t in '+-x*/':								# t is an operator
			S.append(t)									# push the operator symbol
		elif t not in '()':								# consider t to be a literal
			S.append(ExpressionTree(t))					# push trivial tree storing value
		elif t == ')':
			""" compose new tree from 3 constituent parts """
			right = S.pop()								# right subtree as per LIFO
			op = S.pop()								# operator symbol
			left = S.pop()								# left subtree
			S.append(ExpressionTree(op, left, right))	# repush tree
		# ignoring left parenthesis
	return S.pop()



def print_answers_stack(stack):
	print("<td align='left' width='35%' valign='top'>")
	print("<table bgcolor='antiquewhite' align='center' border='2'>")
	print("<tbody>")
	print("<tr>")
	print("<th colspan='8'> Printing all variables: </th>")
	print("</tr>")
	while stack:
		print("<td align='center'> {} </td></tr><tr>".format(stack.pop()))
	print("</table>")

def print_answers_list(answers_list):
	print("<td align='left' width='35%' valign='top'>")
	print("<table bgcolor='antiquewhite' align='center' border='2'>")
	print("<tbody>")
	print("<tr>")
	print("<th colspan='8'> Printing all variables [list]: </th>")
	print("</tr>")
	for result in answers_list:
		print("<td align='center'> {} </td></tr><tr>".format(answers_list))
	print("</table>")



if __name__ == '__main__':
	print_title()
	make_form()
	process_form()
