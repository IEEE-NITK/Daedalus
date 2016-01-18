import random
import math

#generating list of prime numbers
def sieve(size):
    n=int(math.sqrt(size))+1
    primes=[]
    composites=[]

    for i in range(2,n,1):
        temp=i*i

        for j in range(temp,size,i):
            composites.append(j)
    for i in range(2,size,1):
        if i not in composites:
            primes.append(i)
    return primes

# calculating Q(n) by eulerstotient function

def eulerstotientfn(p,q):
    return (p-1)*(q-1)

def gcd(a,b):
    if a is 0:
        return b
    return gcd(b%a,a)

# generating public key
def generating_e(N):
    a=random.randrange(2,N)

    while gcd(a,N) is not 1:
        a=random.randrange(2,N)

    return a

#generating private key exponent
def privatekey_d(e,N):
    d=random.randrange(2,N)

    while (d*e)%N is not 1:
        d=random.randrange(2,N)

    return d

#generating m based on given message M
def generate_m(M,n):
    m=random.randrange(0,n)

    while gcd(m,n) is not 1:
        m=random.randrange(0,n)
    return m

#encrypting the message
def encrypt(m,e,n):
    return (pow(m,e))%n

#decrypting the encrypted message with the help of private key
def decrypt(c,d,n):
    return (pow(c,d))%n

prime = sieve(300)
p=random.choice(prime)
q=random.choice(prime)
print("prime numbers=",p,q)
n=p*q
print("n=",n)

N=eulerstotientfn(p,q)
e = generating_e(N)
print("public key=",e)
d= privatekey_d(e,N)
print("privatekey=",d)
M=90
m=generate_m(M,n)
print("m=",m)
c=encrypt(m,e,n)
print("encrypted message=",c)
m=decrypt(c,d,n)
print("decrypted message = ",m)
