import math
import random

def chkprime(a):
    if a%2==0 & a!=2:
        return False
    for i in range(3,a):
        if a%i==0:
            return False
    return True
        
    
def gen_prime(a,b):
    while True:
        x=random.randint(a,b)
        if chkprime(x):
            return x
def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)

def iscoprime(a,b):
    if gcd(a,b)==1:
        return True
    return False


def inv_mod(a,m):
    x=int(m/a)+1
    while True:
        if (a*x)%m==1:
            return x
        else:
            x=x+1

def key(a,b):
    p=gen_prime(a,b)
    while True:
        q=gen_prime(a,b)
        if p!=q:
            break

    n=p*q
    t=(p-1)*(q-1)

    while True:
        e=random.randint(2,t)
        if iscoprime(t,e):
            break

    d=inv_mod(e,t)
    return n,e,d
    
def encrypt(x,n,e):
    return (x**e)%n

def decrypt(x,d,n):
    return (x**d)%n

def funct():
    n,e,d=key(50,70)

    c=encrypt(86,n,e)                       #encrypt(msg,n,e)...here 86 as example..replace with ascii
    d=decrypt(c,d,n)

    print c,d


funct()
