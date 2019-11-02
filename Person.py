#########################################################################
#								Person.py								#
#	Version: 1.0														#
#	Date: 11/02/2019													#
#	Description:	This module holds the Person class which hold all 	#
#					the desired information about the individual		#
#########################################################################

class Person:
	'''
	The Person module holds the contact information for each individual.
	It may contain their name, phone number, email, residential 
	address or birthday. It also stores information such as if they
	are a favorite contact member.
	'''

	def __init__(self, name, phone, email, address, birthday, favorites):
		self.name = name
		self.phone = phone
		self.email = email
		self.address = address
		self.birthday = birthday
		self.fav = favorites

	def get_name(self):
		'''
		The get_name function is used to acess the individuals name.
		
		Returns: 	name of individual
		'''
		
		return self.name
