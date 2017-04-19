import sys
load("attacks/wieners.sage")
load("attacks/common_modulus_attack.py")
load("attacks/partial_message_exposure.sage")
load("attacks/partial_key_exposure.sage")
load("attacks/coppersmith_univariate.sage")
load("attacks/hastad_simple.py")

class Daedalus():
	def __init__(self):
		self.n = None
		self.e = None 
		self.d = None
		self.ciphertext = None
		self.knowntext = None
		self.qbar = None
		self.results = None
		self.errors  = None
		self.N=None
		self.E=None
		self.ciphertexts=None

	def load_ciphertext(self, option,*args):
		if(option == 'file'):
			f = open(args[0],"r")
			self.ciphertext = int(f.readline())
			f.close()
		else:
			self.ciphertext = args[0]

	def load_ciphertexts(self,num_ct,option,*args):
		self.ciphertexts=[]
		i=0
		while i < num_ct:
			self.load_ciphertext(option,args[i])
			self.ciphertexts.append(self.ciphertext)
			i=i+1


	def load_partial_key(self, option, *args):
		if(option == 'file'):
			f = open(args[0],"r")
			self.qbar = int(f.readline())
			f.close()
		else:
			self.qbar = args

	def load_pubkey(self, option, *args):
		if(option == "file"):
			f = open(args[0], 'r')
			self.n = int(f.readline())
			self.e = int(f.readline())
			f.close()
		else:
			self.n = args[0]
			self.e = args[1]

	def load_pubkeys(self,num_keys,option,*args):
		self.N=[]
		self.E=[]
		i=0
		if option=="file":
			while i < num_keys:
				self.load_pubkey(option,args[i])
				self.N.append(self.n)
				self.E.append(self.e)
				i=i+1
		else:
			while i < 2*num_keys:
				self.load_pubkey(option,args[i],args[i+1])
				self.N.append(self.n)
				self.E.append(self.e)
				i=i+2

	
	def load_privkey(self, option, *args):
		if (option == 'file'):
			f = open(args[0], 'r')
			self.d = int(f.readline())
			f.close()
		else:
			self.d = args[0]
	
	def load_known_plaintext(self, option, *args):
		if(option == 'file'):
			f = open(args[0],"r")
			self.knowntext = int(f.readline())
			f.close()
		else:
			self.knowntext = args[0]
	
	def attack(self, code):
		if code == 'wieners':
			out = wieners_attack({'N':self.n,'e':self.e})
			print "results: d=" ,
			print out['results']
			print "errors: " ,
			print out['errors']
		elif code=='common_mod':
			out = common_modulus_attack({'N':self.N,'E':self.E,'C':self.ciphertexts})
			print "results" ,
			print out['results']
			print "errors" ,
			print out['errors']
			#Do Something
		elif code == "partial_message_exposure":
			out = partial_message_exposure({'N':self.n, 'e':self.e, 'known_plaintext':self.knowntext, 'C':self.ciphertext})
			print "results - "
			print out['results']
			print "Errors"
			print out['errors']
		elif code == "partial_key_exposure":
			out = partial_key_exposure({'N':self.n, 'qbar':self.qbar})
			print "results - "
			print out['results']
			print "Errors"
			print out['errors']
		elif code == "hastad_simple":
			out = hastad_simple({'N':self.N,'E':self.E,'C':self.ciphertexts})
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
Command                      						Purpose
-------                      						-------
help attacks                 						List all supported attacks
r = Daedalus()               						Create new instance of Daedalus
r.load_pubkey('number',n,e)         					Load pubkey as (n,e,)
r.load_pubkey('file',path)  	 					Load pubkey from file
r.load_pubkeys(n_keys,'number',n1,e1,n2,e2...) 				Load multiple keys
r.load_privkey('number',d)         					Load privkey as (d,)
r.load_privkey('file',path)         					Load privkey from file
r.load_ciphertext('number',c)       					Load ciphertext as c
r.load_ciphertext('file',path)      					Load ciphertext from file
r.load_ciphertexts(n,'number',c1,c2..cn) 				Load multiple ciphertexts
r.load_ciphertexts(n,'file',path-1,path-2...path-n) 			Load multiple ciphertexts from files
r.load_known_plaintext('file'|'number',path|known_plaintext) 		Load known plaintext directly or from file
r.load_partialkey('file'|'number',path|key) 				Load partial key directly or from a file
r.attack(code)               						Run attack corresponding to code (see help attacks)
						'''

		elif entered == 'help attacks':
			print '''
Attack                         Code
------                         ----
Wieners Attack                wieners
Common Modulus		      common_mod
Partial Message Exposure      partial_message_exposure
Partial Key Exposure          partial_key_exposure
Hastad Attack                 hastad_simple


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
