#!/usr/local/bin/python3.6
# I honor Parkland's core values by affirming that I have
# followed all academic integrity guidelines for this work.

# Connor Wilhoit

# The next 3 lines are to import my classes (each in its own .py file)
from point import Point
from color import Color
from rectangle import Rectangle

import cgi, cgitb
import random
from os import getrandom	# for seeding PRNG

random.seed(getrandom(256))	# seed PRNG w/256-byte value (from /dev/urandom)

cgitb.enable()			# enables use of methods such as 'cgi.FieldStorage()'

def nl():
	print("<br />")


if __name__ == '__main__':
	# create a list of 1000 random rectangles, and generate the SVG code that will
	# display the rectangles on a web page:
	print("Content-type: text/html\r\n\r\n")
	print("Version 1 --> Where's all the rectangles though?\n")
	print("<br />")



	# Here is we create a list of 1000 Rectangles:
	
	rectangle_list = []
	for rect in range(0, 1000):
		width  = random.randint(1, 100)
		height = random.randint(1, 100)
		x_cord = random.randint(1,1000)
		y_cord = random.randint(1,1000)
		pnt    = Point()
		pnt.set_coordinates(x_cord, y_cord)
		col    = Color()
		rect   = Rectangle(pnt, width, height, col)
		rectangle_list.append(rect)

	print("<br />")
	print("All done creating list of random Rectangles")
	print("<br />")
	print(len(rectangle_list))
	print("<br />")

	print("<svg viewBox='1, 1, 1500, 300'>")
	''' The single-line-commented-out lines work, except for the color is black,
	    default, instead of my assigned color, which is red [rgb(153,0,0)]
	'''
	for rectangle in rectangle_list:
			svg_vals = rectangle.SVG()
			print(svg_vals)
	print("</svg>")
