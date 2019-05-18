#!/usr/local/bin/python3.6
# I honor Parkland's core values by affirming that I have
# followd all academic integrity guidelines for this work.
#
# Connor Wilhoit
from avl_tree import AVLTreeMap
import cgi,cgitb
cgitb.enable()
print("Content-type: text/html\n\n")


def print_title():
	print("<head><title>Spell Checker Lab </title></head>")
	print("<body align='center'>###########################################<br />")
	print("<br />")
	print("<b> Spell Checker Using Maps </b>")
	print("<br />")
	print("<br />###########################################</body>")
	print("<br />")

def make_textarea():
	print("<body><hr></hr><form method='POST'><table><tr>")
	print("<td align='center'>Enter Your Words To Be Spellchecked:</td></tr><tr>")
	print("<td align='center'><textarea rows='10' cols='55' name='user-vals'>")
	print("</textarea></td></tr><tr><td colspan='2' align='center'><br />")
	print("<input type='submit' name='go' value='Spellcheck Words' /></td></tr></table>")
	print("</form></body>")

def output_avltree(avltree):
	print("<td align='center' width='35%' valign='top'>")
	print("<table bgcolor='cyan' align'center' border='2'>")
	print("<tbody><tr><th colspan='8'> AVLTree </th></tr>")
	j = 0
	for k,v in avltree.items():
		if j % 5 == 0:
			print("</tr><tr>")
		print("<td align='center'> {}  {}  </td>".format(k,v))
		j += 1
	print("</table>")


def process_textarea():
	form = cgi.FieldStorage()
	if form.getvalue('user-vals') == None:
		print("I can't spellcheck non-existent words! <br />")
		return
	spellcheck_words(form)

def spellcheck_words(cgi_form):
	raw_data = cgi_form.getvalue('user-vals')
	word_list = ''.join(raw_data).split()
	filename = "/home/staff/kurban/public/lists/web2.txt"
	dictfile = open(filename, "r")
	dictlist = [word.strip() for word in dictfile]
	avltree = AVLTreeMap()

	i = 0
	for word in dictlist:
		avltree[word] = i
		i += 1

	mispelled_words = [w for w in word_list if w not in avltree.keys()]
	if len(mispelled_words) == 0:
		print("<td align='center' width='35%' valign='top'>")
		print("<table bgcolor='yellow' align='center' border='2'>")
		print("<tbody><tr><th colspan='8'> No Incorrect Spellings! </th></tr>")
		print("<td align='center'> Congratulations! </td>")
		print("</table>")
	else:
		j = 0
		print("<td align='center' width='75%' valign='top'>")
		print("<table bgcolor='cyan' align='center' border='2'>")
		print("<tbody><tr><th colspan='8'> Mispelled Words </th></tr>")
		for word in mispelled_words:
			if j % 5 == 0:
				print("</tr><tr>")
			print("<td align='center'> {} </td>".format(word))
		print("</table>")



if __name__ == '__main__':
	print_title()
	make_textarea()
	process_textarea()
