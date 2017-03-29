import sys
load("attacks/wieners.sage")
load("attacks/common_modulus_attack.sage")
load("attacks/partial_message_exposure.sage")

class Daedalus():
	def __init__(self):
		self.n = None
		self.e = None 
		self.d = None
		self.ciphertext = None
		self.knowntext = None
		self.results = None
		self.errors  = None

	def load_ciphertext(self, args, option):
		if(option == 'file'):
			f = open(args,"r")
			self.ciphertext = int(f.readline())
			f.close()
		else:
			self.ciphertext = args

	def loadpubkey(self, args, option):
		if(option == "file"):
			f = open(args, 'r')
			self.n = int(f.readline())
			self.e = int(f.readline())
			f.close()
		else:
			self.n = args[0]
			self.e = args[1]
	
	def loadprivkey(self, args, option):
		if (option == 'file'):
			f = open(args, 'r')
			self.d = int(f.readline())
			f.close()
		else:
			self.d = args[0]
	
	def load_known_plaintext(self, args, option):
		if(option == 'file'):
			f = open(args,"r")
			self.knowntext = int(f.readline())
			f.close()
		else:
			self.knowntext = args
	
	def attack(self, code):
		if code == 'wieners':
			out = wieners_attack({'N':self.n,'e':self.e})
			print "results: d=" ,
			print out['results']
			print "errors: " ,
			print out['errors']
		elif code=='common_mod':
			out = common_modulus_attack({'n':self.n,'e':self.e})
			print "results" ,
			print out['results']
			print "errors" ,
			print out['errors']
			#Do Something
		elif code == "partial_message_exposed":
			out = partial_message_exposure({'N':self.n, 'e':self.e, 'known_plaintext':self.knowntext, 'C':self.ciphertext})
			print "results - "
			print out['results']
			print "Errors"
			print out['errors']

def shell():
	entered = ''
	while(entered != 'quit'):
		entered = raw_input('>>').strip()
		if(entered == 'quit'):
			sys.exit(0)
		elif(entered == "help"):
			print '''
Welcome to Daedalus, the unified RSA attacker!
Command                      		Purpose
-------                      		-------
help attacks                 		List all supported attacks
r = Daedalus()               		Create new instance of Daedalus
r.loadpubkey((n,e,),"number")         	Load pubkey as (n,e,)
r.loadpubkey(path, 'file')  	 	Load pubkey from file
r.loadprivkey((d,))          		Load privkey as (d,)
r.loadprivkey(path)          		Load privkey from file
r.attack(code)               		Run attack corresponding to code (see help attacks)
						'''
		elif entered == 'help attacks':
			print '''
Attack                         Code
------                         ----
Wieners Attack                wieners
Common Modulus		      common_mod
				'''
		else:
			try:
				exec(entered)
			except:
				print "Unexpected error", sys.exc_info()[0], sys.exc_info()[1]
				print "Wrong Usage"
				print "Try - help or help attacks"

if __name__ == '__main__':
	print '''
     _                _       _           
  __| | __ _  ___  __| | __ _| |_   _ ___ 
 / _` |/ _` |/ _ \/ _` |/ _` | | | | / __|
| (_| | (_| |  __/ (_| | (_| | | |_| \__ \\
 \__,_|\__,_|\___|\__,_|\__,_|_|\__,_|___/
 '''
	shell()
