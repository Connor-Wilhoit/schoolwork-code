# I honor Parkland's core value by affirming that I have
# followed all academic integrity guidelines for this work.
#
# Connor Wilhoit

from point import Point
from color import Color
class Rectangle:
	def __init__(self, thepoint, width, height, fill):
		""" Notes about the parameters called in the above line:
		--> 'thepoint': is a 'Point' object from my point.py file
		--> 'width'   : is an integer
		--> 'height'  : is an integer
		--> 'fill'    : is a 'Color' object from my color.py file
		"""
		self._upperleft = thepoint
		self._width		= width
		self._height	= height
		self._fill		= fill



	def SVG(self):
			return "<rect x={} y={} height={} width={} style='fill:{};stroke-width=2;stroke:rgb(0,0,0)'/>".format(
						self.get_upperleft().get_x(),
						self.get_upperleft().get_y(),
						self.get_height(),
						self.get_width(),
						self.get_fill())


	# Getters:
	def get_upperleft(self):
		return self._upperleft

	def get_fill(self):
		return self._fill.SVG()

	def get_height(self):
		return self._height

	def get_width(self):
		return self._width

	# Setters:
	def set_upperleft(self, upperleft):
		self._upperleft = upperleft

	def set_fill(self, fill):
		self._fill = fill

	def set_height(self, height):
		self._height = height

	def set_width(self, width):
		self._width = width


# Testing code:
if __name__ == '__main__':
	t_point = Point()
	t_point.set_x(10)
	t_point.set_y(10)
	t_color = Color()
	t_rect = Rectangle(t_point, 115, 75, t_color)
	svg_vals = t_rect.SVG()
	print(svg_vals)

	w = 110
	h = 55
	t_point.set_coordinates(105, 65)
	t_color.set_colors(100, 50, 100)
	t_rect.set_upperleft(t_point)
	t_rect.set_fill(t_color)
	t_rect.set_width(w)
	t_rect.set_height(h)
	svg_vals2 = t_rect.SVG()
	print(svg_vals2)
