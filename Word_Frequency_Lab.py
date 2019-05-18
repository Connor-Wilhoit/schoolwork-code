#!/usr/local/bin/python3.6
# I honor Parkland's core values by affirming that I have
# followed all academic integrity guidelines for this work.
#
# Connor Wilhoit
import cgi,cgitb
cgitb.enable()
print("Content-type: text/html\n\n")

def print_title():
	print("<head><title>Word Frequency Lab</title></head>")
	print("<body align='center'>#######################################<br />")
	print("<br />")
	print("<b> Word Frequency (top 20 words or less!) </b>")
	print("<br />")
	print("<br />######################################</body>")

def make_form():
	print("<body>")
	print("<table width='100%'>")
	print("<tr><td align='center' colspan='2'>")
	print("<hr></td></tr></hr></table>")
	print("<form method='POST'>")
	print("<table><tr><td align='center'>Enter Your Data Below</td></tr>")
	print("<tr><td align='center'>")
	print("<textarea rows='10' cols='55' name='user-vals'></textarea>")
	print("</td></tr><tr><td colspan='2' align='center'>")
	print("<input type='submit' name='go' value='ProcessData' /></td></tr>")
	print("</table></form></body>")

def process_form():
	form = cgi.FieldStorage()
	if form.getvalue('user-vals') == None:
		print("I can't compute word frequencies if you don't give me any words! <br />")
		print("Please input some data! :) <br />")
		return

	output_data(form)

def output_data(cgi_form):
	freq = {}
	raw_data = cgi_form.getvalue('user-vals')
	words = ''.join(raw_data).lower().split()
	for word in words:
		#print("[1]: ", word, "<br />")
		if word in freq:
			freq[word] += 1
		else:
			freq[word] = 1 + freq.get(word, 0)

	freq_output(freq)


def freq_output(hash_table):
	from collections import OrderedDict
	from operator import itemgetter
	if len(hash_table) <= 20:
		inorder = OrderedDict(sorted(hash_table.items(), key=itemgetter(1), reverse=True))
		print("<td align='center' width='35%' valign='top'>")
		print("<table bgcolor='cyan' align='center' border='2'>")
		print("<tbody><tr><th colspan='8'>Top 20 (or less) Words </th></tr>")
		print("<tr><th colspan='8'>Word | Frequency | Hash-Value </th></tr>")
		count = 1
		for k,v in inorder.items():
			h = hash_function(k)
			print("<td align='left'>[{}]: {}</td><td>{}</td><td>{}</td></tr><tr>".format(count,k,v,h))
			count += 1
		print("</table><br />")
		max_count(hash_table)
	else:
		order = OrderedDict(sorted(hash_table.items(), key=itemgetter(1), reverse=True))
		i = 20
		j = 1
		print("<td align='center' width='35%' valign='top'>")
		print("<table bgcolor='cyan' align='center' border='2'>")
		print("<tbody><tr><th colspan='8'>Top 20 Words </th></tr>")
		print("<tr><th colspan='8'>Word | Frequency | Hash-Value </th></tr>")
		for k,v in order.items():
			h = hash_function(k)
			print("<td align='left'>[{}]: {}</td><td>{}</td><td>{}</td></tr><tr>".format(j,k,v,h))
			i -= 1
			j += 1
			if i == 0:
				break
		print("</table><br />")
		max_count(hash_table)



def max_count(hash_table):
	max_word = ''
	max_count = 0
	for (w,c) in hash_table.items():	# (key, value) tuples represent (word, count)
		if c > max_count:
			max_word = w
			max_count = c
	print("<td align='center' width='35%' valign='top'>")
	print("<table bgcolor='yellow' align='center' border='1'>")
	print("<tbody><tr><th colspan='8'>The most frequent word is: {} </th></tr>"
			.format(max_word))
	print("<tbody><tr><th colspan='8'>Its number of occurences is: {} </th></tr>"
			.format(max_count))



def hash_function(str_to_hash):
	tablesize = 19991			# a prime
	result = 0
	for char in str_to_hash:
		result = (result * 256 + ord(char)) % tablesize
		# won't this be 0 + ascii-value % tablesize every single time?
		# --so the hashing is just the ascii-value of the character,
		#   modded by the tablesize prime number 19991???
	return result





if __name__ == '__main__':
	print_title()
	make_form()
	process_form()
