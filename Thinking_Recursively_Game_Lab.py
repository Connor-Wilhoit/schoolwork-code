#!/usr/local/bin/python3.6
# I honor Parkland's core values by affirming that I have
# followed all academic integrity guidelines for this work.
#
# Connor Wilhoit
from queue import Queue
import cgi, cgitb
cgitb.enable()
print("Content-type: text/html\n\n")


def game_board(alist):
	print("Game Board:<br />")
	for i in alist:
		print(i, end=' ')
	print("<br />")


def winning_path(integer_list):
	print("Winning Path:<br />")
	for i in integer_list:
		print(i, " --> ", end=' ')
	print("Win")
	print("<br />")


def print_form():
	print("<form method='POST'>")
	print("Enter list of space-separated integers:<input type='text' name='nums'>")
	print("Press [Enter] when finished")
	print("</form>")

def process_form():
	form    = cgi.FieldStorage()
	numbers = []

	# Quick error-checking:
	if form.getvalue('nums') == None:
		print("Please input some numbers!")
	else:
		numbers.append(form.getvalue('nums'))
		numstr = ''.join(numbers).split()

		recursive_solution(numstr)		# solve game


def recursive_solution(alist):
	int_list = [0] * len(alist)
	for i in range(0, len(alist)):
		int_list[i] = int(alist[i])

	game_board(int_list)				# print out the game board

	end_position     = len(int_list)-1
	end_value        = int_list[-1]
	current_position = 0 
	current_value	 = int_list[current_position]

	boolean_visited_positions = [False] * len(int_list)

	visited_positions = []

	visited_positions.append(current_position)
	game_won = False
	
	#######################################################################
	# The following block of code is the actual "solving" code.           #
	#                                                                     #
	#                                                                     #
	#######################################################################

	if int_list[0] == 0 and len(int_list) == 1:
		print("<br />")
		winning_path(visited_positions)

	elif int_list[0] == 0 and len(int_list) > 1:
		print("<br />")
		print("We have an un-solvable game.... :(")

	elif current_position == end_position and current_value == end_value:
		print("<br />")
		winning_path(visited_positions)

	else:
		next_position = current_position
		next_value    = current_value
		# Recursive Algorithm
		try:
			win_loss = 	solve(int_list, visited_positions, boolean_visited_positions,
					end_value, end_position, next_value, next_position, game_won)
			print("win_loss: {} <br />".format(win_loss))
			if win_loss:
				winning_path(visited_positions)
			else:
				print("<br /> Un-winnable game :( <br />")
				print("<br /><br />")
		except:
			print("<br /><br />")
			print("<br />Un-winnable game :(<br />")




def solve(int_list, visited_list, visited_bools, e_val, e_pos, n_val, n_pos, game_won):
	#  [1]
	if n_pos == e_pos and n_val == e_val:
		game_won = True
		return True
	#  [2]
	elif n_pos + n_val == e_pos:
		visited_list.append(n_pos+n_val)
		game_won = True
		return True
	#  [3]
	elif n_pos != e_pos and n_val == 0:
		game_won = False
		return False
	#  [4]
	elif n_pos + n_val >= len(int_list):
		# recur left
		n_pos -= n_val
		visited_list.append(n_pos)
		visited_bools[n_pos] = True
		n_val = int_list[n_pos]
		return solve(int_list, visited_list, visited_bools, e_val, e_pos, n_val, n_pos, game_won)
	#  [5]
	elif n_pos - n_val <= 0:
		# recur right
		n_pos += n_val
		visited_list.append(n_pos)
		visited_bools[n_pos] = True
		n_val = int_list[n_pos]
		return solve(int_list, visited_list, visited_bools, e_val, e_pos, n_val, n_pos, game_won)
	#  [6]
	else:
		#  [7]
		if visited_bools[n_pos+n_val]:
			# We've already been at the possible position to the right, therefore:
			# recur left
			n_pos -= n_val
			visited_list.append(n_pos)
			visited_bools[n_pos] = True
			n_val = int_list[n_pos]
			return solve(int_list, visited_list, visited_bools, e_val, e_pos, n_val, n_pos,
					game_won)
		#  [8]
		else:
			# The only option we have left is to recur right
			n_pos += n_val
			visited_list.append(n_pos)
			visited_bools[n_pos] = True
			n_val = int_list[n_pos]
			return solve(int_list, visited_list, visited_bools, e_val, e_pos, n_val, n_pos,
					game_won)




if __name__ == '__main__':
	print_form()
	process_form()
