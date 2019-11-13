#########################################################################
#	Person.py								
#	Version: 1.0														
#	Date: 11/02/2019													
#	Description:	This module holds the Person class which hold all 
#					the desired information about the individual		
#########################################################################

class Person:
	'''
	The Person module holds the contact information for each individual.
	It may contain their name, phone number, email, residential 
	address or birthday. It also stores information such as if they
	are a favorite contact member.
	'''

	def __init__(self, name, phone, email, address, birthday, favorites):
		'''
		This is the constructor. We define and declare all of the values
		which are supposed to contained within a contact
		'''
		self.name = name
		self.phone = phone
		self.email = email
		self.address = address
		self.birthday = birthday
		self.fav = True if favorites=='yes' else False

	def get_name(self):
		'''
		The get_name function is used to acess the individuals name.
		Returns: 	name of individual
		'''
		return self.name

	def get_phone(self):
		return self.phone

	def get_email(self):
		return self.email

	def get_add(self):
		return self.address
	
	def get_birthday(self):
		return self.birthday

	def get_fav(self):
		'''
		The get_fav function is used to access the if the individual
		is on the favorites list.
		Returns: boolean True/False
		'''
		return self.fav

<<<<<<< HEAD

	def display_info(self):
=======
	def get_info(self):
>>>>>>> 8b324ee26dd3cd9c32204c7d1617ef40c2e63399
		'''
		This method will display all of the information which is contained
		about the person
		Parameters: none
		Returns: all info in a list
		'''
		return [self.name,self.phone,self.email,self.address,self.birthday, 'yes' if self.fav==True else 'no']
		