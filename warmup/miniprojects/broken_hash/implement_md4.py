from array import array
from string import join
from struct import pack, unpack

#Functions to convert between different encodings
_DECODE = lambda x, e: list(array('B', x.decode(e)))
_ENCODE = lambda x, e: join([chr(i) for i in x], '').encode(e)
hex_to_bytes = lambda x: _DECODE(x, 'hex')
txt_to_bytes = lambda x: hex_to_bytes(x.encode('hex'))
bytes_to_hex = lambda x: _ENCODE(x, 'hex')
bytes_to_txt = lambda x: bytes_to_hex(x).decode('hex')
#Step1- The message is padded(extended) such that its length is congruent to 448 modulo 512. 
#		If the message is already congruent tp 448 modulo 512, then 512 more bits are added. Padding- Single '1' and rest '0's
#Step2- 64 bit representation of the length of the message is appended to the padded message 
def pad_message(msg):
	n = len(msg)
	bit_len = n * 8
	index = (bit_len >> 3) & 0x3fL
	pad_len = 120 - index
	if index < 56:
		pad_len = 56 - index
	padding = '\x80' + '\x00'*63
	padded_msg = msg + padding[:pad_len] + pack('<Q', bit_len)
	return padded_msg
#We define the following functions to be used in Step4
def _left_rotate(n, b):
	return ((n << b) | ((n & 0xffffffff) >> (32 - b))) & 0xffffffff
def _f(x, y, z): return x & y | ~x & z
def _g(x, y, z): return x & y | x & z | y & z
def _h(x, y, z): return x ^ y ^ z

def _f1(a, b, c, d, k, s, X): return _left_rotate(a + _f(b, c, d) + X[k], s)
def _f2(a, b, c, d, k, s, X): return _left_rotate(a + _g(b, c, d) + X[k] + 0x5a827999, s)
def _f3(a, b, c, d, k, s, X): return _left_rotate(a + _h(b, c, d) + X[k] + 0x6ed9eba1, s)
class MD4:
	#Step3- We use four 32 bit word buffers to compute the message digest. We initialize each of the buffers to the following hex values. 
	def __init__(self):
		self.A = 0x67452301
		self.B = 0xefcdab89
		self.C = 0x98badcfe
		self.D = 0x10325476
	def update(self, message_string):
		msg_bytes = txt_to_bytes(pad_message(message_string))
		for i in range(0, len(msg_bytes), 64):
			self._compress(msg_bytes[i:i+64])
	#Step4- Process message in 16 bit word blocks. We use the previously defined functions in three rounds of compression(hashing).
	# 		We use sqrt(2) as round 2 constant and sqrt(3) as round three constant.
	def _compress(self, block):
		#We save the initial state of the buffers 
		a, b, c, d = self.A, self.B, self.C, self.D  
		x = []
		for i in range(0, 64, 4):
			x.append(unpack('<I', bytes_to_txt(block[i:i+4]))[0])
		#Round 1- Do following 16 operations 
		a = _f1(a,b,c,d, 0, 3, x)
		d = _f1(d,a,b,c, 1, 7, x)
		c = _f1(c,d,a,b, 2,11, x)
		b = _f1(b,c,d,a, 3,19, x)
		a = _f1(a,b,c,d, 4, 3, x)
		d = _f1(d,a,b,c, 5, 7, x)
		c = _f1(c,d,a,b, 6,11, x)
		b = _f1(b,c,d,a, 7,19, x)
		a = _f1(a,b,c,d, 8, 3, x)
		d = _f1(d,a,b,c, 9, 7, x)
		c = _f1(c,d,a,b,10,11, x)
		b = _f1(b,c,d,a,11,19, x)
		a = _f1(a,b,c,d,12, 3, x)
		d = _f1(d,a,b,c,13, 7, x)
		c = _f1(c,d,a,b,14,11, x)
		b = _f1(b,c,d,a,15,19, x)
		#Round 2- Do following 16 operations 
		a = _f2(a,b,c,d, 0, 3, x)
		d = _f2(d,a,b,c, 4, 5, x)
		c = _f2(c,d,a,b, 8, 9, x)
		b = _f2(b,c,d,a,12,13, x)
		a = _f2(a,b,c,d, 1, 3, x)
		d = _f2(d,a,b,c, 5, 5, x)
		c = _f2(c,d,a,b, 9, 9, x)
		b = _f2(b,c,d,a,13,13, x)
		a = _f2(a,b,c,d, 2, 3, x)
		d = _f2(d,a,b,c, 6, 5, x)
		c = _f2(c,d,a,b,10, 9, x)
		b = _f2(b,c,d,a,14,13, x)
		a = _f2(a,b,c,d, 3, 3, x)
		d = _f2(d,a,b,c, 7, 5, x)
		c = _f2(c,d,a,b,11, 9, x)
		b = _f2(b,c,d,a,15,13, x)
		#Round 3- Do following 16 operations 
		a = _f3(a,b,c,d, 0, 3, x)
		d = _f3(d,a,b,c, 8, 9, x)
		c = _f3(c,d,a,b, 4,11, x)
		b = _f3(b,c,d,a,12,15, x)
		a = _f3(a,b,c,d, 2, 3, x)
		d = _f3(d,a,b,c,10, 9, x)
		c = _f3(c,d,a,b, 6,11, x)
		b = _f3(b,c,d,a,14,15, x)
		a = _f3(a,b,c,d, 1, 3, x)
		d = _f3(d,a,b,c, 9, 9, x)
		c = _f3(c,d,a,b, 5,11, x)
		b = _f3(b,c,d,a,13,15, x)
		a = _f3(a,b,c,d, 3, 3, x)
		d = _f3(d,a,b,c,11, 9, x)
		c = _f3(c,d,a,b, 7,11, x)
		b = _f3(b,c,d,a,15,15, x)

		# We add the initial states of the buffers back to the respective buffers
		self.A = (self.A + a) & 0xffffffff
		self.B = (self.B + b) & 0xffffffff
		self.C = (self.C + c) & 0xffffffff
		self.D = (self.D + d) & 0xffffffff
		#Step5- The message digest produced as output is ABCD(the buffers), starting with lower order byte of A and ending with higher order byte of D
	def digest(self):
		return bytes_to_hex(txt_to_bytes(pack('<IIII', self.A, self.B, self.C, self.D)))
#driver function
if __name__ == '__main__':

	def md4(msg):
		m = MD4()
		m.update(msg)
		print m.digest() 
	print "Hash of blank message- ",
	md4("")
	print "Plaintext- a\nHash- ",
	md4("a")
	print "Plaintext- abc\nHash- ",
	md4("abc")
	print "Plaintext- abcdefghijklmnopqrstuvwxyz\nHash- ",
	md4("abcdefghijklmnopqrstuvwxyz")
	print "Plaintext- ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789\nHash- ",
	md4("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
	print "Plaintext- NITK\nHash- ",
	md4("NITK")
	print "Plaintext- md4\nHash- ",
	md4("md4")
	message=raw_input("Enter text to be encoded- ")
	print "Hashed message- ",
	md4(message)