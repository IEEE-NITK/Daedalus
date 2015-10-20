#!/usr/bin/python2

import random
#Step 1:
#generate two prime numbers preferrably differing by a few digits.
#let the prime numbers be p and q

print "Please wait. Initialising..."

def SieveOfEratosthenes(n):
    not_prime = []
    prime = []
    for i in xrange(2, n+1):
        if i not in not_prime:
            prime.append(i)
            for j in xrange(i*i, n+1, i):
                not_prime.append(j)
    return prime
    
primes = SieveOfEratosthenes(1000)

#Selecting two random primes p and q
p = random.choice(primes)
q = random.choice(primes)


#Ensuring p != q
while(p == q):
	q = random.choice(primes)

#computing n	
n = p * q

#computing Euler's Totient for n

def EulerTotientOfPrime(x):
	return x-1

TotientOfN = EulerTotientOfPrime(p) * EulerTotientOfPrime(q)

#selecting an e within [1,TotientOfN]

e = random.choice(range(1,TotientOfN))

def gcd(x,y):
	if x < y:
		x,y = y,x
	
	while(y != 0):
		x,y = y,x%y
		
	return x
	
#ensuring e and TotientOfN are co - prime
while(gcd(e,TotientOfN) != 1):
	e = random.choice(range(1,TotientOfN))

#preparing decrypt key
d = 0

#calculating modular inverse of e (mod TotientOfN)
for num in range(2,TotientOfN):
	if((num*e)%TotientOfN == 1):
		d= num
		break

PublicKey = [n,e]
PrivateKey = [d]

print "Input a message to be Encrypted."
message = raw_input()

def encrypt(m,n,e):
	return (m ** e)%n

def decrypt(c,n,d):
	return (c ** d)%n
	
#encrypting character by character
encryptedmessage = ""
#print "character", "ascii value", "encrypted value", "decrypted value"
for character in message:
	temp = ord(character)
	encryptedmessage += str(encrypt(temp,n,e))+" "
	
print "Encrypted Message:"
print encryptedmessage	

string = ""
decryptedmessage = ""
for character in encryptedmessage:
	if(character == " "):
		num = (int)(string)
		decryptedmessage += chr(decrypt(num,n,d))
		string = ""
	else:
		string += character		
	
print "Decrypted Message:"
print decryptedmessage
print "public key: ", PublicKey
print "private key: ", PrivateKey
	
