#####################################################################
#	Contact_book.py							
#																	
#	Version: 1.0													
#	Date: 11/02/2019												
#	Description:	This module is the main module which performs	
#					all of the crutial functions in order to		
#					satisfy the users desires 						
#	The Contact book stores information of each individual such	as 	
#		thier name, phone number, email, residential address and	
#		birthday. It will then provide the user with the following	
#		services: 													
#			1. Search for a contact 								
#				a. By name 											
#				b. Favorites 										
#			2. Add a contact 										
#			3. Edit a contact 													
#####################################################################

from Person import Person

people_list = []

def disp_fav():
	'''
	This function will filter out all of the favorite contacts in 
	the list of contacts and display their information.
	parameters: none
	return: none
	'''
	fav_list = list(filter(lambda p: p.get_fav()==True, people_list))
	for f in fav_list:
		f.display_info()

def search():
	'''
	This function will search the individuals name in the list
	by performing a binary search.
	Parameter:
	Return:
	'''
	print('\n\n')
	print("a. Display favorites")
	print('b. Search by name')
	print('c. Go Back')
	user_in = input('\nWhat would you like to do?: ').strip()
	if (user_in.lower() == 'a'):
		disp_fav()
	elif user_in.lower() == 'b':
		pass
	elif user_in.lower() == 'c':
		pass
	else:
		print('Invalid input please try again')
		search()

def add_contact():
	'''
	This function will add the contact to the already created list
	of people and append the new contact member to the contacts.txt 
	file.
	Parameter:
	Return:
	'''
	pass

def edit():
	'''
	This function will perform any edits on an already existing
	contact member and then append it to the contacts.txt file.
	Parameter:
	Return:
	'''
	names = []
	for p in people_list:
		names.append(p.get_name())
	print('\n\n\n')
	print('Here is the list of contacts:')
	print(names)
	print('Which one contact you like to edit: ')

def askInput():
	'''wywy
	This function asks the user which action/service they would like
	to perform.
	Parameter:	None
	Return:	None
	'''
	print('\n\n\n')
	print("1. Search contact")
	print("2. Add contact")
	print("3. Edit contact")
	print("Q  to Quit")
	return input('\nWhat would you like to do?: ').strip()
	print('\n\n')

def run():
	'''
	The run function will be the soul opperator which runs the
	program.
	Parameter: None
	Return:	None2
	'''
	print('\n\n\n')
	print('='*80)
	print("Welcome to the addressbook")
	print('This program stores all of your contacts so you ' \
		+'will never forget them again!')
	print('='*80)

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
			print("Invalid input please try again!")

def parse_file():
	'''
	This function will read the contacts.txt file and then parse
	all of the information about each individual. It will initialize
	each individual with the Person object. Then it will store all
	of the People in a list.
	Parameter:	None
	Return:	None
	'''
	
	with open('contacts.txt', 'r') as f:
		f_contents = f.readlines()
		while(len(f_contents)>5):
			name = f_contents.pop(0).strip()
			phone = f_contents.pop(0).strip()
			email = f_contents.pop(0).strip()
			address = f_contents.pop(0).strip()
			birthday = f_contents.pop(0).strip()
			fav = f_contents.pop(0).strip()
			p = Person(name,phone,email,address,birthday,fav)
			people_list.append(p)

#####################################################################
#	Driver Code								
#####################################################################

if __name__ == '__main__':
	parse_file()
	run()
