# I honor Parkland's core values by affirming that I have
# followed all academic integrity guidelines for this work.
#
# Connor Wilhoit

class Color:
	def __init__(self):
		self._red   = 153	# rgb-red is: (255, 0, 0)
		self._green = 0		# rgb-green is: (0, 255, 0)
		self._blue  = 0		# rgb-blue is: (0, 0, 255)


	# This block is the set&get functions for managing ALL 3 colors at once:
	def set_colors(self, red, green, blue):
		self._red   = red
		self._green = green
		self._blue  = blue

	def get_colors(self):
		return "{} {} {}".format(self._red, self._green, self._blue) 

	def print_colors(self):
		print("(", self._red, ",", self._green, ",", self._blue, ")")

	def SVG(self):
		return "rgb({},{},{})".format(self._red, self._green, self._blue)



	# The rest of the functions are for setting/getting individual color values:
	# Setters:
	def set_red(self, red):
		self._red = red
	def set_green(self, green):
		self._green = green
	def set_blue(self, blue):
		self._blue = blue

	# Getters:
	def get_red(self):
		return self._red
	def get_blue(self):
		return self._blue
	def get_green(self):
		return self._green



# Testing code:
if __name__ == '__main__':
	c = Color()
	col = c.SVG()
	print(col)
	colors = c.get_colors()
	print(colors)
	r = c.get_red()
	g = c.get_green()
	b = c.get_blue()
	print(r)
	print(g)
	print(b)
	c.set_red(111)
	c.set_green(222)
	c.set_blue(121)
	rr = c.get_red()
	gg = c.get_green()
	bb = c.get_blue()
	print(rr)
	print(gg)
	print(bb)
	c.set_colors(100, 55, 75)
	c.print_colors()
