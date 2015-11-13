import struct

"""
The circular left shift operation S^n(X), where X is a word and n
is an integer with 0 <= n < 32, is defined by

         S^n(X)  =  (X << n) OR (X >> 32-n).

In the above, X << n is obtained as follows: discard the left-most
n bits of X and then pad the result with n zeroes on the right
(the result will still be 32 bits).  X >> n is obtained by
discarding the right-most n bits of X and then padding the result
with n zeroes on the left.  Thus S^n(X) is equivalent to a
circular shift of X by n positions to the left.

Documentation from US SHA1 - RFC 3174 (http://www.ietf.org/rfc/rfc3174.txt)
:P

"""

def circular_left_shift(word,bit):

	return (( word << bit) | ( word >> (32 - bit)))
	
	


def sha1(message):

	#initialsed constants h0, h1, h2, h3, h4
	
	h = [ 0x67452301 , 0xEFCDAB89 , 0x98BADCFE , 0x10325476 , 0xC3D2E1F0 ]
	
	#Message Padding Procedures Commence from here
	
	#one unicode character in string is equal to one byte
	#hence length of message gives the number of bytes
	
	initial_byte_length = len(message)
	
	#One byte = 8 bits
	
	initial_bit_length = initial_byte_length * 8
	
	#Must pad the message with a '1' - Rule
	
	message += b'\x80'
	
	#Padding the remaining block of 512 bits with 0
	
	message += b'\x00' *  ((56 - (initial_byte_length + 1) % 64) % 64)
	
	#b'>Q' is an arguement to struct.pack where b stands for binary packing, > for Big Endian format
	# and Q stands for Unsigned long long .It returns a string
	
	message += struct.pack(b'>Q', initial_bit_length)
	
	#for every block of size 64 bytes i.e 512 bits - a block, starting from 0 to the last block
	
	for block in range(0 , len(message), 64):
	
		#initialising word as a list of 80 "0"s
		
		word = [0] * 80
		
		for piece in range(16):
		
			#b'>I' is an arguement to struct.unpack where b stands for binary unpacking, > for Big Endian format
			# and I stands for Unsigned Int.It returns a tuple even if it returns one item,
			# hence the [0] .
			
			#String splicing is used to to give the correct word slice out of the main string
			
			word[piece] = struct.unpack(b'>I',message[block + piece*4: block + piece*4 + 4])[0]
			
		for piece in range(16,80):
		
			#Pre - defined in SHA1 Algoithm
			
			word[piece] = circular_left_shift(word[piece - 3] ^ word[piece - 8] ^ word[piece - 14] ^ word[piece - 16],1)
		
		#Pre - defined in SHA1 Algoithm
		
		a = h[0]
		b = h[1]
		c = h[2]
		d = h[3]
		e = h[4]
		
		#Pre - defined Sha values and functions
		
		for bit in range(80):
		
			#Pre - defined in SHA1 Algoithm
			
			if 0 <= bit <=19:
			
				f = d ^ ( b & ( c ^ d))
				
				k = 0x5A827999
				
			elif 20 <= bit <= 39:
			
				f = b ^ c ^ d
				
				k = 0x6ED9EBA1
				
			elif 40 <= bit <= 59:
			
				f = (b & c) | (b & d) | (c & d)
				
				k = 0x8F1BBCDC
				
			elif 60 <= bit <= 79:
			
				f = b ^ c ^ d
				
				k = 0xCA62C1D6
				
			#Yet again, predefined by RFC 3174
				
			a,b,c,d,e = (( circular_left_shift(a,5) + f + e + k + word[block]) & 0xffffffff, a, circular_left_shift(b,30) , c, d)
			
		#we AND with 0xffffffff i.e 11111111111111111111111111111111 (32 bit of 1) to prevent overflow
			
		h[0] = ( h[0] + a ) & 0xffffffff
		h[1] = ( h[1] + b ) & 0xffffffff
		h[2] = ( h[2] + c ) & 0xffffffff
		h[3] = ( h[3] + d ) & 0xffffffff
		h[4] = ( h[4] + e ) & 0xffffffff
			
	#after the message digestion return the string consiting of h0,h1,h2,h3,h4
	
	return '%08x%08x%08x%08x%08x' % ( h[0], h[1], h[2], h[3], h[4])
	
#Driver program	
#:D

print "Enter an input string:"
inputstring = raw_input()
print "SHA1 is:"
print sha1(inputstring)
