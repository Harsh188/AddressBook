#####################################################################
#							Contact_book.py							#
#																	#
#	Version: 1.0													#
#	Date: 11/02/2019												#
#	Description:	This module is the main module which performs	#
#					all of the crutial functions in order to		# 
#					satisfy the users desires 						#
#	The Contact book stores information of each individual such	as 	#
#		thier name, phone number, email, residential address and	#
#		birthday. It will then provide the user with the following	#
#		services: 													#
#			1. Search for a contact 								#
#				a. By name 											#
#				b. Favorites 										#
#			2. Add a contact 										#
#			3. Edit a contact 										#			
#####################################################################

from Person import Person

def parse_file():
	people_list = []
	with open('contacts.txt', 'r') as f:
		f_contents = f.readlines()
		while(len(f_contents)>6):
			name = f_contents.pop(0).strip()
			phone = f_contents.pop(0).strip()
			email = f_contents.pop(0).strip()
			address = f_contents.pop(0).strip()
			birthday = f_contents.pop(0).strip()
			fav = f_contents.pop(0).strip()
			p = Person(name,phone,email,address,birthday,fav)
			people_list.append(p)

def askInput():
	print("Welcome to the addressbook")
	print("1. Search contact")
	print("2. Add contact")
	print("3. Edit contact")
	print("Q to Quit")
	return input().strip()

def search():
	pass

def add_contact():
	pass

def edit():
	pass

def run():
	while(True):
		user_in = askInput()
		if user_in == '1':
			search()
		elif user_in == '2':
			add_contact()
		elif user_in == '3':
			edit()
		elif user_in.lower() == 'q':
			break
		else:
			print("Invalid input please try again")

#####################################################################
#							Driver Code								#
#####################################################################

if __name__ == '__main__':
	parse_file()
	run()


