#pollard rho algorithm of integer factorization

import random
import math


def gcd(a,b):
    if a<=0:
        return b
    return gcd(b%a,a)

def pollard_rho(number,x,y):
    d = 1
    while d is 1:
        x = (x**2+1)%number
        for i in range(0,2,1):
            y = (y**2+1)%number
        if x>y:
            z = x-y
        else:
            z=y-x
        d = gcd(z,number)
    return d

def attack(input={}):
    #initialising x and y values
    x=2
    y=2
    errors=[]
    try:
        number = input['n']
    except TypeError as e:
        errors.append(e)
    factor1 = pollard_rho(number,x,y)
    while factor1 is  1:
        x = x+1
        y = y+1
        factor1 = pollard_rho(number,x,y)
    factor2 = int(number/factor1)
    results ={'p':factor1,'q':factor2}
    return {'errors':errors,'results':results}

