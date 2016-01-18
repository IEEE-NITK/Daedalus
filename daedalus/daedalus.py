#!/usr/bin/python
import sys


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
		# For example purposes only! Remove later.
		if code == 'ex':
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
Attack                       Code
------                       ----
Example                      ex
'''
		else:
			try:
				exec(entered)
			except:
				print "Command not found... see 'help'."


if __name__ == '__main__':
	print '''
     _                _       _           
  __| | __ _  ___  __| | __ _| |_   _ ___ 
 / _` |/ _` |/ _ \/ _` |/ _` | | | | / __|
| (_| | (_| |  __/ (_| | (_| | | |_| \__ \\
 \__,_|\__,_|\___|\__,_|\__,_|_|\__,_|___/

 '''
	shell()
