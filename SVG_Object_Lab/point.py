# I honor Parkland's core values by affirming that I have
# followed all academic integrity guidelines for this work.
#
# Connor Wilhoit

class Point:
	def __init__(self):
		self._across = 0
		self._down   = 0

	def set_coordinates(self, x_coordinate, y_coordinate):
		self._across = x_coordinate
		self._down   = y_coordinate

	def get_coordinates(self):
		print("(", self._across, ",", self._down, ")")

	def set_x(self, x_coordinate):
		self._across = x_coordinate

	def set_y(self, y_coordinate):
		self._down = y_coordinate

	def get_x(self):
		return self._across

	def get_y(self):
		return self._down


# Testing code for this class:
if __name__ == '__main__':
	point1 = Point()
	point1.get_coordinates()
	point1.set_coordinates(100, 50)
	point1.get_coordinates()
	x_value = point1.get_x()
	print(x_value)
	y_value = point1.get_y()
	print(y_value)


	point1.set_x(11)
	point1.set_y(22)
	point1.get_coordinates()
	print(point1.get_x())
	print(point1.get_y())

	print("All done!\n")

