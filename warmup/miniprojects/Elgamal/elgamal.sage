#NITK-IEEE-SaS
#Elgamal encryption algo implementation

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
            
#function to generate public and private keys
#private key = a
#public key = g^a(mod p)
def key_gen(p,g):
    a=random.randint(1,p-1)
    y=pow(g,a,p)
    return y,a
 
def main():
    p=gen_prime(300,1000) #p is public
    
    #generator production: g is public
    g=random.randint(2,p-2)
    
    #computing public and private keys for alice(a) and bob(b)
    a_pub,a_priv=key_gen(p,g)
    b_pub,b_priv=key_gen(p,g)
    
    s=pow(a_pub,b_priv,p)
    
    #take m as input plaintext
    #m=int(raw_input("Enter the message to be encrypted"))
    
    #using m=64 as an example
    encrypt_msg=(s*64)%p

    #encrpyting done by bob: a_pub and b_priv is available
    #encrypt_msg=(pow(a_pub,b_priv)*63)%p
    
    #decrypting done by alice: b_pub,encrpyt_msg,a_priv available
    decrypt_msg=(encrypt_msg*pow(b_pub,p-1-a_priv))%p
    
    print encrypt_msg
    print decrypt_msg
    
main()
