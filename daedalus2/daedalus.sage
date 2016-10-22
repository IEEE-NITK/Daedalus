import sys

class Daedalus():
	def __init__(self):
		self.n = None
		self.e = None 
		self.d = None 
		self.results = None
		self.errors  = None

	def loadpubkey(self, args, type=None):
		if (type == 'file'):
			f = open(args, 'r')
			self.n = int(f.readline())
			self.e = int(f.readline())
		else:
			self.n = args[0]
			self.e = args[1]
	
	def loadprivkey(self, args, type=None):
		if (type == 'file'):
			f = open(args, 'r')
			self.d = int(f.readline())
		else:
			self.d = args[0]

def shell():
	entered = ''
	while(entered != 'quit'):
		entered = raw_input('>>')
		if(entered == 'quit'):
			sys.exit(0)
		elif(entered == "help"):
			print "help"
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
