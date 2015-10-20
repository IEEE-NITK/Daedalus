import random

def isPrime(i):
    	for j in range(2,i):
        	if i%j==0:
            		return False
	return True

def Prime():
	primes = [i for i in range(3,1000) if isPrime(i)]
	r = random.choice(primes)
	return r

def Modulus(p, q):
	n = p * q
	return n

def EulerTotientFn(p,q):
	z = (p-1) * (q-1)
	return z

def gcd(a,b):
	if(a < b):
		a,b=b,a
	while(b != 0):
		a,b = b,a%b
	return a

def egcd(a, b):
    	if a == 0:
        	return (b, 0, 1)
    	else:
		g, y, x = egcd(b % a, a)
        	return (g, x - (b // a) * y, y)

def modinv(e, z):
    	g, x, y = egcd(e, z)
    	if g != 1:
        	raise Exception('modular inverse does not exist')
    	else:
        	return x % z
    	
def encrypt(m,n,e):
	return (m ** e)%n

def decrypt(c,n,d):
	return (c ** d)%n


p = Prime()
q = Prime()
while (p==q):
	p=Prime()
	q=Prime()

n = Modulus(p, q)
z = EulerTotientFn(p, q)

e=random.choice(range(1,z))

while(gcd(e,z)!=1):
	e=random.choice(range(1,z))

d=modinv(e,z)

publicKey=[e,n]
privateKey=[d,n]

print "Input a message"
message = raw_input()

print "Public key: ", publicKey
print "Private key: ", privateKey

enc = []
dec = []
print "message: ",message
print "encrypted value",
for character in message:
	ch = ord(character)
	en=encrypt(ch,n,e)
	print en,
        de=decrypt(en,n,d)
	dec.append(chr(de))
print " "
decr = ""
for word in dec:
    decr += "" + word
print "decrypted value: ", decr
