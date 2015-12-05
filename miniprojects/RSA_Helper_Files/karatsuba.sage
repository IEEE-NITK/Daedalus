""" implements karatsuba multiplication for two numbers a and b """
def karatsuba_mult(a,b):
    n=max_digits(a,b)
    #print "max_digits is",n
    if(n>1):
        a2,a1=divide(a,n//2)
        b2,b1=divide(b,n//2)
        z2=karatsuba_mult(a2,b2)
        z1=karatsuba_mult(a1,b1)
        z3=karatsuba_mult(a2+a1,b1+b2)-z2-z1
        power=n//2
        ans=z2*(10**(2*power))+z3*(10**power)+z1
        return ans
    else:
        return a*b

""" partitions a given number into two equal/almost equal parts
    ex: for a=2345, returns 23 and 45, for a=234, returns 23 and 4 """
def divide(a,n):
    a2=a//(10**n)
    a1=a%(10**n)
    return a2,a1

""" returns the number of digits of the bigger number """
def max_digits(a,b):
    counta=len(str(a))
    countb=len(str(b))
    if counta>=countb:
        return counta
    else:
        return countb
a=input("Enter first number")
b=input("Enter second number")
product=karatsuba_mult(a,b)
print product

