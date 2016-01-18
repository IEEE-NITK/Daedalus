#!/usr/bin/python


def dummy():
    print "Time to start!"

def shell():
	entered = ''
	while entered != 'quit':
		entered = raw_input('>> ')


if __name__ == '__main__':
	shell()
