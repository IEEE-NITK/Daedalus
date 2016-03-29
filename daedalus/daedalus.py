#!/usr/bin/python
import sys
import attacks.wieners
import attacks.common_modulus_attack
class Daedalus():
	def __init__(self):
		self.n = None
		self.e = None
		self.d = None
		self.results = None
		self.errors = None

	def loadpubkey(self, args, type=None):
		if type=='file':
			try:
				f = open(args, 'r')
			except:
				print "File not found"
		else:
			# Assuming input is of the form (n,e,)
			self.n = args[0]
			self.e = args[1]

	def loadprivkey(self, args, type=None):
		if type=='file':
			try:
				f = open(args, 'r')
			except:
				print "File not found"
		else:
			# Assuming input is of the form (d,)
			self.d = args[0]
	def attack(self, code):
		if code == 'wieners':
			out=attacks.wieners.attack({'n':self.n,'e':self.e})
			print "results: d=" ,
			print out['results']
			print "errors" ,
			print out['errors']
		elif code=='common_mod':
			out=attacks.common_modulus_attack.attack({'n':self.n,'e':self.e})
			print "results" ,
			print out['results']
			print "errors" ,
			print out['errors']
			#Do Something

		elif code=='pollard_rho':
			out=attacks.pollard_rho_algorithm.attack({'n':self.n,'e':self.e})
			print "results" ,
			print out['results']
			print "errors" ,
			print out['errors']
			#Do Something

			# Call the appropriate attack module
			
		pass
def shell():
	entered = ''
	while entered != 'quit':
		entered = raw_input('>> ')
		if entered == 'quit':
			sys.exit(0)
		elif entered == 'help':
			print '''
Welcome to Daedalus, the unified RSA attacker!
Command                      Purpose
-------                      -------
help attacks                 List all supported attacks
r = Daedalus()               Create new instance of Daedalus
r.loadpubkey((n,e,))         Load pubkey as (n,e,)
r.loadpubkey(path, 'file')   Load pubkey from file
r.loadprivkey((d,))          Load privkey as (d,)
r.loadprivkey(path)          Load privkey from file
r.attack(code)               Run attack corresponding to code (see help attacks)
			'''
		elif entered == 'help attacks':
			print '''
Attack                         Code
------                         ----
Wieners Attack                wieners
Pollard Rho Algorithm 	      pollard_rho
Common Modulus		      common_mod
'''
		else:
			exec(entered)   


if __name__ == '__main__':
	print '''
     _                _       _           
  __| | __ _  ___  __| | __ _| |_   _ ___ 
 / _` |/ _` |/ _ \/ _` |/ _` | | | | / __|
| (_| | (_| |  __/ (_| | (_| | | |_| \__ \\
 \__,_|\__,_|\___|\__,_|\__,_|_|\__,_|___/
 '''
	shell()


