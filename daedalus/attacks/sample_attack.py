# This file should serve as a template
# We will be importing all such files into daedalus from which any attack can be then called with required input

###########################################################################
# attack(input={})
# This function will be called from with daedalus.py 
# along with the required input.
# inputs:  A dictionary of parameters containing information
# 		   	about the public key, private key and any other user provided
# 		    information necessary for execution.
# returns: A dictionary consisting of two keys:-
# 	errors:  It should be an array of strings containing all
# 			 errors encountered.
# 	results: It should be a dictionary containing all the results that 
#			 can be derived from the given data.
def attack(input={}, errors=[], results={}):
	return {'errors': errors, 'results': results}