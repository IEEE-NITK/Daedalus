#Implementation of RSA 
#This can primarily be divided into 3 steps-
#1. Key Generation
#2. Encryption 
#3. Decryption
import math 
import random
def create_list_primes(sieve_size):
	#Returns a list of primes less than or equal to sieveSize
	sieve=[True]*sieve_size
	sieve[0]=False
	sieve[1]=False 
	#zero and one are not prime
	#creating the sieve 
	for i in range (2,int(math.sqrt(sieve_size))+1):
		pointer=i*2
		while pointer<sieve_size:
			sieve[pointer]=False
			pointer+=i
	#compile list of primes
	primes=[]
	for i in range(sieve_size):
		if sieve[i]==True:
			primes.append(i)
	return primes
def gcd(a, b):
	#Returns the greatest common divisor of two numbers a,b
    while b:
    	a,b=b,a%b
    return a
def extended_euclid(e,n):
	#Returns number d which is the multiplicative inverse of e congruent modulo n.
	d,new_d,r,new_r=0,1,n,e
	while new_r!=0:
		quotient=r/new_r
		d,new_d=new_d,d-quotient*new_d
		r,new_r=new_r,r-quotient*new_r
	if d<0:
		d=d+n
	return d
def expmod(m,e,n):
	#Returns c congruent to m power e modulo n.
	c=1
	for i in range(0,e):
		c=(c*m)%n
	return c
def encrypt(m,e,n):
	#Encrypts message m with public key exponent e.
	#To be combined with expmod as the same function.
	return expmod(m,e,n)
def decrypt(c,d,n):
	#Decrypts message using private key d
	return expmod(c,d,n)
#Key Generation consists of the following steps-
#1. Selecting 2 large distinct prime numbers- p,q at random.
# We use Sieve of Eratosthenes in the create_list_primes function to do this. Can be improved using better Number Field Sieves.
primes=create_list_primes(5000)
p,q=0,0
while p<1000:
	p=random.choice(primes)
while (q<1000 or q==p):
	q=random.choice(primes)	
#2. We calculate n=pq modulus for the public and private
n=p*q
#3. We compute Phi(n)-Number of natural numbers which are less than n and relatively prime to n.
#Since n=pq, Phi(n)=Phi(p)Phi(q)
#If p is any prime, then Phi(p)=p-1
phi_n=p
#4. We choose an arbitrary integer e such that 1<e<Phi(n) and e,Phi(n) are co prime. e is released as the public key exponent
e=q
#5. We compute d- multiplicative inverse of e congruent modulo phi_n. We use Extended Euclidean Algorithm to compute d. d is kept as private key exponent 
d=extended_euclid(e,phi_n)
print "Public Key pair- %d,%d\nPrivate Key-%d\n"%(e,n,d)
#Encryption
#Each byte of the message is encrypted as c=m^e(mod n), where c is the encrypted byte, m is the message byte.
plaintext=raw_input("Enter message to be encrypted- ")
ciphertext=[]
for i in plaintext:
	ciphertext.append(encrypt(ord(i),e,n))
print "Encyrpted Message-",
print ciphertext
#Decryption 
#Each byte of the encrypted message is decrypted using the private key exponent
message=""
for i in ciphertext:
	message=message+chr(decrypt(i,d,n))
print "Decrypted message-",
print message 
