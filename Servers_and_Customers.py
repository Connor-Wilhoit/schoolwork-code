#!/usr/local/bin/python3.6
# I honor Parkland's core values by affirming that I have
# followed all academic integrity guidelines for this work.
#
# Connor Wilhoit
from queue import Queue
from stack import Stack
import cgi, cgitb
cgitb.enable()
print("Content-type: text/html\n\n")

def print_outline():
	print("<head><title> Servers and Customers </title></head>")
	print("<body align='center'>##########################################<br />")
	print("<b> Server-Stacks & Customer-Queues </b>")
	print("<br />##########################################</body>")


def make_form():
	""" From the assingment PDF:
		hints & ideas:
		  Make a form w/2 text areas and 1 submit.
	"""
	print("<body>")
	print("<table width='100%'>")
	print("<tr><td align='center' colspan='2'>")
	print("<h1>Server Stacks</h1>")
	print("<h6>    and      </h6>")
	print("<h3>Customer Queues</h3>")
	print("<hr></td></tr></hr></table>")
	print("<form method='POST'>")
	print("<table>")
	print("<tr>")
	print("<td align='center'>Enter server below in the form<br />Name #Served</td>")
	print("<td align='center'>Enter customers below in the form<br />Name #Present</td>")
	print("</tr>")
	print("<tr>")
	print("<td align='center'>")
	print("<textarea rows='25' cols='20' name='servers'></textarea>")
	print("<h2>Entry/Exit</h2></td>")
	print("<td align='center'>")
	print("<textarea rows='25' cols='20' name='customers'></textarea>")
	print("<h2>Exit</h2></td>")
	print("</tr>")
	print("<tr>")
	print("<td colspan='2' align='center'>")
	print("<input type='submit' name='selection' value='Open for the evening' /></td>")
	print("</tr>")
	print("</table>")
	print("</form>")
	print("</body>")



def process_form():
	form = cgi.FieldStorage()

	if form.getvalue('servers') == None and form.getvalue('customers') is not None:
		print("Please get me some servers!")
	elif form.getvalue('customers') == None and form.getvalue('servers') is not None:
		print("We have over-hired for this shift... Go get me some customers!")
	elif form.getvalue('customers') == None and form.getvalue('servers') == None:
		print("Oh boy....Are we open? I see no servers OR customers....")
	else:
		s = [form.getvalue('servers')]
		c = [form.getvalue('customers')]

		s_str_list = ''.join(s).split()
		c_str_list = ''.join(c).split()
		#s_str_list.reverse()
		
		print("Servers[list]: {}<br />".format(s_str_list))
		print("Custos [list] : {}<br />".format(c_str_list))
		
		process_data(s_str_list, c_str_list)


def process_data(server_form, customer_form):
	servers = Stack()
	customers = Queue()
	testing_servers = Stack()
	testing_customers = Queue()

	names = []
	serv_nums = []
	for i in reversed(server_form):
		if i.isdigit():
			serv_nums.append(int(i))
		else:
			names.append(i)

	ss = [ [names], [serv_nums] ]

	custos = []
	cust_nums = []
	for i in customer_form:
		if i.isdigit():
			cust_nums.append(int(i))
		else:
			custos.append(i)
	cc = [ [custos], [cust_nums] ]

	rev_names = names.copy()
	rev_serv_nums = serv_nums.copy()
	rev_names.reverse()
	rev_serv_nums.reverse()
	#for name,num in zip(names,serv_nums):
	for name,num in zip(rev_names,rev_serv_nums):
		servers.push(dict([(name,num)]))
		testing_servers.push(dict([(name,num)]))

	for custo,num in zip(custos,cust_nums):
		customers.enqueue(dict([(custo,num)]))
		testing_customers.enqueue(dict([(custo,num)]))


	print("<br /><br />")
	count = 1
	print("Servers[stack]:<br />")
	while testing_servers:
		S = list(testing_servers.top().keys())
		N = list(testing_servers.top().values())
		print("<br /><br />")
		print("Server #{}:  Name: {}  Serve-Count: {}".format(count, S[0], N[0]))
		print("<br /><br />")
		testing_servers.pop()
		count += 1
	c_count = 1
	print("Customers[queue]:<br />")
	while testing_customers:
		Q = list(testing_customers.first().keys())
		R = list(testing_customers.first().values())
		print("<br /><br />")
		print("Customer #{}:  Name: {}  Paryt-Count: {}".format(c_count, Q[0], R[0]))
		print("<br /><br />")
		testing_customers.dequeue()
		c_count += 1

	"""
	# All this commented-out code works; use it as a reference for how to handle the
	# 'servers' stack and the 'customers' queue
	i = 1
	while servers:
		s = list(servers.top().keys())
		v = list(servers.top().values())
		print("<br /><br />")
		print("Server #{}:  Name: {}  Serve-Count: {}".format(i, s[0], v[0]))
		#print(type(s))
		#print(type(s[0]))
		#print(type(v))
		#print(type(v[0]))
		#print("<br /><br />")
		servers.pop()
		i += 1

	j = 1
	while customers:
		q = list(customers.first().keys())
		r = list(customers.first().values())
		print("<br /><br />")
		print("Customer #{}:  Name: {}  Party-Count: {}".format(j, q[0], r[0]))
		customers.dequeue()
		j += 1
	"""	
	i = 1
	while customers:	# make sure to check if we run out of servers!
		if servers.is_empty():
			print("<br /><br />")
			print("Uh Oh! Looks like we ran out of Servers! <br />")
			break
		s = list(servers.top().keys())			# server-name
		v = list(servers.top().values())		# server-serve-count
		q = list(customers.first().keys())		# customer-name
		r = list(customers.first().values())	# customer-paryt-count
		if v[0] == r[0]:
			print("<br /><br />")
			# server-name, customer-name, server-serve-count, customer-party-count
			print("{} can serve ALL of {} [{} == {}]".format(s[0],q[0],v[0],r[0]))
			servers.pop()
			customers.dequeue()

		elif v[0] > r[0]:
			print("<br /><br />")
			# server-name, customer-name, server-serve-count, customer-party-count
			print("{} can serve MORE people than {} has [{} > {}]<br />"
					.format(s[0],q[0],v[0],r[0]))
			print("Removing {} party of {} from their queue location<br />"
					.format(q[0],r[0]))
			difference = v[0] - r[0]   # find how many customers current server can serve
			customers.dequeue()			   # remove customer
			# server-name, remaining-serve-count
			print("{} can serve {} more customers<br />".format(s[0],difference))
			print("<br /><br />")
			v[0] = difference		# see if I can eliminate the need for the temp. var.
			update_dict = dict([(s[0],v[0])])
			servers.top().update(update_dict)
			
		elif v[0] < r[0]:
			print("<br /><br />")
			# server-name, customer-name, server-serve-count, customer-party-count
			print("{} can serve LESS people than {} has [{} < {}]<br />"
					.format(s[0],q[0],v[0],r[0]))
			# server-name, customers-from-current-party-they-served, customer-name
			print("Removing {}, who served {} customers from party {} <br />"
					.format(s[0],v[0],q[0]))
			party = r[0] - v[0]		# get how many people are left in current customer
			servers.pop()
			# customer-name, remaining-party-count-to-be-served
			print("{} has {} people left to be served <br />".format(q[0],party))
			r[0] = party
			new_dict = dict([(q[0],r[0])])
			customers.first().update(new_dict)

		else:
			print("Hit the else statement --> Popping Current server and customer<br />")
			print("Popping Server: {} --> {} <br />".format(s[0], v[0]))
			print("Dequeueing Customer: {} --> {} <br />".format(q[0], r[0]))
			servers.pop()
			customers.dequeue()


		if customers.is_empty():
			print("<br /> All customers have been served! <br />")
			print("<br /> Au Revoir! <br />")











if __name__ == '__main__':
	print_outline()
	make_form()
	process_form()
