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
from tempfile import mkstemp
from shutil import move
import os

people_list = []

def sort_contacts():
	pass

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

def find_person():
	pass

def display():
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
		sort_contacts()
		find_person().display_info()
	elif user_in.lower() == 'c':
		pass
	else:
		print('Invalid input please try again')
		display()

def add_contact():
	'''
	This function will add the contact to the already created list
	of people and append the new contact member to the contacts.txt 
	file.
	Parameter:
	Return:
	'''
	pass

def replace(file_path, pattern, subst, start = 0):
	#Create temp file
	fh, abs_path = mkstemp()
	ctr =0
	with os.fdopen(fh,'w') as new_file:
		with open(file_path) as old_file:
			for line in old_file:
				if ctr>=start:
					new_file.write(line.replace(pattern, subst))
				else:
					new_file.write(line)
				ctr+=1
    #Remove original file
	os.remove(file_path)
    #Move new file
	move(abs_path, file_path)

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
	print('Here is the list of contacts:\n')
	for x,ele in enumerate(names,start=0):
		print(x,ele)
	user_in = input('\nWhich one contact you like to edit: ').strip()
	person = people_list[int(user_in)]
	print('Enter in new chances. Leave empty if no change.')
	new_name = input('\n\nName: ').strip()
	new_phone = input('\nPhone Number: ').strip()
	new_email = input('\nEmail: ').strip()
	new_address = input('\nAddress: ').strip()
	new_birthday = input('\nBirthday: ').strip()
	new_fav = input('\nFavorites(yes/no): ').strip().lower()

	start = int(user_in)*6

	dir_path = os.path.dirname(os.path.realpath(__file__))
	os.chdir(dir_path)
	file_path = os.path.abspath("contacts.txt")
	if new_name!='':
		replace(file_path,person.get_name(),new_name,start)
	if new_phone!='':
		replace(file_path,person.get_phone(),new_phone,start)
	if new_email!='':
		replace(file_path,person.get_email(),new_email,start)
	if new_address!='':
		replace(file_path,person.get_add(),new_address,start)
	if new_birthday!='':
		replace(file_path,person.get_birthday(),new_birthday,start)
	if new_fav!='':
		fav = 'yes' if person.get_fav()==True else 'no'	
		replace(file_path,fav,new_fav,start)

	parse_file()

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
			display()
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
	global people_list
	people_list = []
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
