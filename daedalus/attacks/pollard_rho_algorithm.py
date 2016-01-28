#pollard rho algorithm of integer factorization

import random
import math
from Crypto.PublicKey import RSA

errors = []

def gcd(a,b):
    if a is 0:
        return b
    return gcd(b%a,a)

def pollard_rho(number,x,y):
    try:
        number = int(number)
    except TypeError as n:
        globals()['errors'].append(n)

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


def attack(input={},errors = {},results = {}):
    try :
          number = int(input["key"])
    except TypeError as n:
        globals()['errors'].append(n)

    x=2
    y=2
    factor = pollard_rho(number,x,y)
    while factor is number or 1:
        x = x+1
        y = y+1
        factor = pollard_rho(number,x,y)
    factor2 = int(number/factor)
    results["p "]= factor
    results["q "]= factor2
    return {'errors': globals()['errors'],'results':results}
