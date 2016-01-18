#!/usr/bin/python

class Daedalus():
	def __init__(self):
		pass

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


def shell():
	entered = ''
	while entered != 'quit':
		entered = raw_input('>> ')
		exec(entered)


if __name__ == '__main__':
	shell()
