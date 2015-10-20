import math
import random
multiples=set() #to hold the set of prime numbers
#To generate prime numbers till n using Sieve of Eratosthenes algo 
def Sieve(n):
    for i in range(2, n+1):
        if i not in multiples:
            yield i
            multiples.update(range(i*i, n+1, i))
    
def EulerTotient_prime(n):
    return n-1

def EulerTotientOfN(p,q):
    return EulerTotient_prime(p)*EulerTotient_prime(q)

def gcd(a,b):
	if(b==0):
	    return a
	return gcd(b,a%b)
	
#generates e
def PublicKey(E):
    e=random.choice(range(1,E))
    while(gcd(e,E)!=1):
        e=random.choice(range(1,E))
    return e

    
#to compute modular multiplicative inverse using Extended Euclid algo
def PrivateKey(n,e,E):
    t=0     
    new_t=1    
    r=E     
    new_r= e    
    while (new_r != 0):
        quotient= r/new_r
        t, new_t = new_t, t - quotient * new_t 
        r, new_r = new_r, r - quotient * new_r
    if r > 1:
        return;
    if t < 0:
        t = t + n
    return t

def encrypt(m,n,e):
	return (m ** e)%n

def decrypt(c,n,d):
	return (c ** d)%n

def _main():
    primes=[]    
    primes=list(Sieve(5000)) #converts the tuple to list and stores a list of prime numbers till 5000

    #To select random prime numbers from the list primes[]
    p=random.choice(primes)
    q=random.choice(primes)

    #while p,q are same, generate a different prime q 
    while(1):
        if(p!=q):
            break
        q=random.choice(primes)

    #Compute n

    n=p*q

    EulerT_N=EulerTotientOfN(p,q)

    Pub_key=PublicKey(EulerT_N)
    Priv_key=PrivateKey(n,Pub_key,EulerT_N)

    msg=raw_input("Enter the message to be encrypted")

    for ch in msg:
        ch_to_int=ord(ch)
        en=encrypt(ch_to_int,n,Pub_key)
        de=decrypt(en,n,Priv_key)
        print ch,'|',en,'|',de
  

_main()

            
        
    
    



