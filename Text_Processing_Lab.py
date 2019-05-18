#!/usr/local/bin/python3.6
# I honor Parkland's core values by affirming that I have
# followed all academic integrity guidelines for this work.
#
# Connor Wilhoit
import cgi, cgitb
from string_parse import isletter 
cgitb.enable()


print("Content-type: text/html\n\n")

def print_form():
	print("<form method='POST'>")
	print("Enter some stuff:")
	print("<textarea name='paragraph' row='15' cols='45'>")

	print("</textarea>")
	print("<input type='submit'>")



	print("</form>")



def table_output():
	form = cgi.FieldStorage()
	temp = []		# List to append chars to, until a space is found,
				# then it's cleared.

	split_words = []	# This list will hold the parsed & sorted words
	#big_words = ''.join(w for w in form.getvalue('paragraph') if w.isalpha())
	#  The above line is a useful tactic; future use forsure.
	if form.getvalue('paragraph') == None:
		print("Please input some words!")
	else:
		#print(len(form.getvalue('paragraph')))	
		for value in form.getvalue('paragraph'):
			if value.isalpha():
				temp.append(value)
			else:
				word = ''.join(temp)
				split_words.append(word)
				temp.clear()
		big_words = ''.join(temp)
		split_words.append(big_words)
		split_words.sort()

		display_columns = 10
		display_count   = 0
		max_words       = 400
		word_count      = len(split_words)
		total_chars     = 0
		for word in split_words:
			total_chars += len(word)
		average_word_length = total_chars / word_count

		print("Total Characters: {}<br />".format(total_chars))
		print("Number of Total Words: {}<br />".format(word_count))
		print("Avg Length [exact]: {:.2f} chars<br />".format(average_word_length))
		print("Avg [rounded]: {} chars<br />".format(int(average_word_length)))
		print("<table>")
		print("<tr>")
		if word_count <= 400:
			print("Here's your words!<br />")
			for word in split_words:
				print("<td>{}</td>".format(word))
				display_count += 1
				if display_count % display_columns == 0:
					print("</tr>")
					print("<tr>")
			print("</tr>")
			print("</table>")
		else:		# more than 400 words in list, so printing ONLY first 400
			print("WOW! Too many words! Here's your first 400:<br />")
			for word in split_words[0:400]:
				print("<td>{}</td>".format(word))
				display_count += 1
				if display_count % display_columns == 0:
					print("</tr>")
					print("<tr>")
			print("</tr>")
			print("</table>")




if __name__ == '__main__':
	print_form()
	table_output()
