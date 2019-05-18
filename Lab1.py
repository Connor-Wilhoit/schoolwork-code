#!/usr/local/bin/python3.6
# I honor Parkland's core values by affirming that I have
# followed all academic integrity guidelines for this work.

# Connor Wilhoit

import cgitb
cgitb.enable()

def draw_my_circle():
	print('''
		<circle cx='940' cy='45' r='40'
		style='fill:rgb(153,0,0);stroke-width=2;stroke:rgb(153,0,0)'/>
		''')

def draw_my_rectangle():
	print('''
		<rect x='10' y='10' height='75' width='295'
		style='fill:rgb(51,51,249);stroke-width:8;stroke:rgb(153,0,0)' />
		''')

def print_my_name():
	print("<text x='110' y='50' style='fill:rgb(255,255,255)'>Connor Wilhoit</text>")



print("Content-type: text/html\r\n\r\n")
print("<html>")
print("<title> SVG-CGI-Lab </title>")
print("<head>")
print("</head>")
print("<body>")

print("<svg viewBox='1, 1, 1000, 100'>")
draw_my_circle()
draw_my_rectangle()
print_my_name()
print("</svg>")


print("</body>")
print("</html>")
