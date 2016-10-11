r"""program to compute time taken for key generation, enecryption, decrytion with and without CRT"""

from time import time

def ModExp(a,x,n):
	r"""
	Calculates a^x mod n using right-to-left binary method
	"""

	R=IntegerModRing(n)
	prod=R(1)
	a=R(a)
	
	x=ZZ(x) #integer ring
	#in sage, <type 'int'> and <type 'sage.rings.integer.Integer'> are different 
	x_bin=x.bits() #Return the bits in x as a list, least significant first
	x_bin_len=x.nbits() #number of bits; a faster way to compute len(x.bits())
	
	for i in xrange(x_bin_len):
		if(x_bin[i]==1):
			prod=prod*a
		a=a*a
	
	return prod


def KeyGen():
	r""" Generates all the parameters in the private and public key """
	
	p=random_prime(2^512-1, proof=None, lbound=2^511)
	q=random_prime(2^512-1, proof=None, lbound=2^511)
	r"""
	Returns a random prime p between lbound and n (i.e. lbound <= p <=
	   n). The returned prime is chosen uniformly at random from the set
	      of prime numbers less than or equal to n.
	INPUT:
	* "n" - an integer >= 2.
	* "proof" - bool or None (default: None) If False, the function
	uses a pseudo-primality test, which is much faster for really big
    numbers but does not provide a proof of primality. If None, uses
    the global default (see "sage.structure.proof.proof")
	* "lbound" - an integer >= 2 lower bound for the chosen primes
	"""
	
	#print "p:\n",p
	#print "q:\n",q
	
	n=p*q
	#print "n:\n",n
	
	phi=(p-1)*(q-1)
	#print "phi:\n",phi
	
	R=IntegerModRing(phi)
	e=65535
	while(gcd(e,phi)!=1):	
		e=random_prime(phi-1)
	#print "e:\n",e
	e=R(e) #e=e(mod phi)
	
	d=1/e
	#print "d:\n",d
	
	return (n,e,d,p,q)


def EncryptText(m,public_key):
	r""" computes m^e(mod n) """
	(n,e)=public_key
	return ModExp(m,e,n)

def DecryptText(c,private_key):
	r""" computes c^d(mod n) """
	(n,d)=private_key
	return ModExp(c,d,n)

def DecryptTextCRT(c,private_key):
	r"""decryption using CRT"""
	(p,q,n,d)=private_key
	
	dp=d%(p-1)
	dq=d%(q-1)
	
	#print "dp is ",dp
	#print "dq is ",dq
	
	m_p=ZZ(ModExp(c,dp,p)) #converting into IntegerRing is necessary
	m_q=ZZ(ModExp(c,dq,q))
	
	#print type(m_p)
	
	m=CRT(m_p,m_q,p,q)
	r""" Here m=m_p(mod p) and m=m_q(mod q)"""
	return m



print "Loop\tKey Generation\tEncryption\t\tDecryption\t\tDecryption CRT"
for i in range(10):
	
	start_gen=time()
	(n,e,d,p,q)=KeyGen()
	end_gen=time()
	
	public_key=(n,e)
	private_key=(p,q,n,d)
	#message=int(random()*100000)
	message=random_prime(2^128,False,2^127)
	
	start_enc=time()
	cipher_text=EncryptText(message,public_key)
	end_enc=time()
	
	start_dec=time()
	dec=DecryptText(cipher_text,(n,d))
	end_dec=time()
	
	start_dec_crt=time()
	decrypted_text=DecryptTextCRT(cipher_text,private_key)
	end_dec_crt=time()
	
	r"""print "Message is: "
	print message
	print "Encrypted text: "
	print cipher_text
	print "Decrypted text: "
	print decrypted_text
	"""
	
	print i,"\t",end_gen-start_gen,"\t",end_enc-start_enc,"\t",end_dec-start_dec,"\t",end_dec_crt-start_dec_crt
