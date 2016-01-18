#NITK-IEEE SaS: Cryptography project
#Natasha Y Jeppu
#Implementation of simple RSA cryptosystem in python

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

#function computes inverse modulus: returns pvt key exponent
def inv_mod(a,m):
    x=int(m/a)+1
    while True:
        if (a*x)%m==1:
            return x
        else:
            x=x+1

#to generate public and private keys
def key(a,b):
    p=gen_prime(a,b)
    while True:
        q=gen_prime(a,b)
        if p!=q:
            break
    
    #product of euler-totient of primes to serve as modulus
    n=p*q
    t=(p-1)*(q-1)

    while True:
        e=random.randint(2,t)
        if iscoprime(t,e):
            break

    d=inv_mod(e,t)
    
    #e is public key exponent, d is private key exponent
    return n,e,d
    
def encrypt(x,n,e):
    return (x**e)%n

def decrypt(x,d,n):
    return (x**d)%n


#Function to implement rsa encryption and decryption 
def funct_rsa():
    n,e,d=key(50,70)

    #encrypt(ascii of plaintext,modulus for the keys,public key exponent)
    #taking 86 as an example to chk implementation
    c=encrypt(86,n,e)               
    #encrypt(ciphertext,private key exponent,modulus for the keys)
    d=decrypt(c,d,n)

    #display cipher and plaintext
    print c,d



funct_rsa()
