# This file is to hold exceptions which are specific to the
# "Mini Language" Lab.
# It will be called if a variable is attempted to be set equal to a
# non-existent variable.

class UndefinedVar(Exception):
	"""Error attempting to set a variable equal to an undefined
	   variable. """
	pass

class PopFromEmpty(Exception):
	"""Error attempting to pop an element from an empty container."""
	pass

class AccessFromEmpty(Exception):
	"""Error attempting to access an element from an empty container."""
	pass
