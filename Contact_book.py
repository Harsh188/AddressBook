#####################################################################
#	Contact_book.py							
#	Author: Harshith MohanKumar														
#	Version: 1.0													
#	Date: 11/02/2019												
#	Description:	This module contains all of the backend work done
#			to make the contact book functional. It does the following
#			(1) Retrieves data from txt file
#			(2) Sorts the data in the txt file
#			(3) Performs binary search
#			(4) Edits the data in the txt file							
#####################################################################

# Imports
from Person import Person
from tempfile import mkstemp
from shutil import move
import os

# Global variable
# Stores Person objects
people_list = []

def sort_contacts():
	'''
	This method sorts the txt file based on the 
	individual's name in alphabetical order.
	Parameter: None
	Return: None
	'''
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
				new_file.write(x+'\n')
    #Remove original file
	os.remove(file_path)
    #Move new file
	move(abs_path, file_path)
	parse_file()

def string_format(l_info):
	'''
	This method formats the list into a string
	which can be printed in the GUI
	Parameters: List
	Returns: String (contact information)
	'''
	output = ''
	output+='\n\n'
	output+='\nName: '+l_info[0]
	output+='\nPhone Number: '+l_info[1]
	output+='\nEmail: '+l_info[2]
	output+='\nAddress: '+l_info[3]
	output+='\nBirthday: '+l_info[4][0:2]+'/'+\
		l_info[4][2:4]+'/'+l_info[4][4:len(l_info[4])]
	output+='\nFavorites: '+l_info[5]
	output+='\n\n'
	return output

def disp_fav():
	'''
	This function will filter out all of the favorite contacts in 
	the list of contacts and return their information as a string.
	parameters: none
	return: String (contact information)
	'''
	sort_contacts()
	string_output = ''
	fav_list = list(filter(lambda p: p.get_fav()==True, people_list))
	if len(fav_list)==0:
		return '\n\nYou have no favorite contacts!'
	for f in fav_list:
		string_output = string_format(f.get_info()) 
	return string_output

def search(name):
	'''
	This method determines if the person is in the contact book by
	calling a binary search method and returns the appropriate answer
	Parameters: String (contact name)
	Returns: String (contact information)
	'''
	string_output = ''
	try:
		person = search_name(name)
		string_output = string_format(person.get_info()) 
	except:
		string_output='\n\nCONTACT NOT FOUND! Please try again\n\n'
	return string_output

def search_name(name): 
	'''
	This program will perform a binary search to find
	the person sent in through the parameter
	Parameter: String (contact name)
	Return: if found: Person object
			else: -1
	'''
	sort_contacts()
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
	f = open("contacts.txt","a")
	for x in list_info:
		f.write(x+'\n')
	f.close()
	sort_contacts()

def replace(file_path, pattern, subst, start = 0):
	'''
	Helper method created to edit the file.
	Parameters: file path, pattern to edit, substitute for pattern
				starting line value.
	Return: None
	'''
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
	Parameter: string name, list (contact info)
	Return: none
	'''
	sort_contacts()
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

def get_names(word):
	sort_contacts()
	names = []
	for p in people_list:
		if word.lower() in p.get_name().lower():
			names.append(p.get_name())
	return (names)

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
	pass