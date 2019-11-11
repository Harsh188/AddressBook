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
	parse_file()
	people_list.sort(key=lambda x: x.get_name())

	dir_path = os.path.dirname(os.path.realpath(__file__))
	os.chdir(dir_path)
	file_path = os.path.abspath("contacts.txt")

	#Create temp file
	fh, abs_path = mkstemp()
	with os.fdopen(fh,'w') as new_file:
		for p in people_list:
			info_list = p.get_info()
			for x in info_list:
				new_file.write(x)
    #Remove original file
	os.remove(file_path)
    #Move new file
	move(abs_path, file_path)

def disp_fav():
	'''
	This function will filter out all of the favorite contacts in 
	the list of contacts and display their information.
	parameters: none
	return: none
	'''
	string_output = ''
	fav_list = list(filter(lambda p: p.get_fav()==True, people_list))
	for f in fav_list:
		string_output+='\n\n'
		string_output+='\n'.join(f.get_info())
		string_output+='\n\n'
	return string_output

def search(name):
	person = search_name(name)
	string_output = ''
	string_output+='\n\n'
	string_output+='\n'.join(person.get_info())
	string_output+='\n\n' 
	return string_output

def search_name(name): 
	'''
	This program will perform a binary search to find
	the person sent in through the parameter
	Parameter: String name
	Return: String
	'''
	arr = people_list
	r = len(people_list)-1
	l = 0
	x = name
	while l <= r:
  
		mid = l + (r - l)//2; 
          
        # Check if x is present at mid 
		if arr[mid].get_name() == x:
			return arr[mid]
  
        # If x is greater, ignore left half 
		elif arr[mid].get_name() < x: 
			l = mid + 1
  
        # If x is smaller, ignore right half 
		else:
			r = mid - 1
      
    # If we reach here, then the element 
    # was not present 
	return -1

def add_contact(list_info):
	'''
	This function will add the contact to the already created list
	of people and append the new contact member to the contacts.txt 
	file.
	Parameter: List of info
	Return: none
	'''
	f = open("contacts.txt","w")
	for x in list_info:
		f.write(x)
	f.close()

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

def edit(name,list_info):
	'''
	This function will perform any edits on an already existing
	contact member and then append it to the contacts.txt file.
	Parameter: string name, list of information about contact
	Return: none
	'''
	names = []
	for p in people_list:
		names.append(p.get_name())
	i = names.index(name)
	start = i*6

	dir_path = os.path.dirname(os.path.realpath(__file__))
	os.chdir(dir_path)
	file_path = os.path.abspath("contacts.txt")

	old_info = search_name(name).get_info()
	for indx in range(0,6):
			if list_info[indx] != '':
				replace(file_path,old_info[indx],list_info[indx],start)

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
	# run()
