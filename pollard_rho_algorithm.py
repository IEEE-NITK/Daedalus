#pollard rho algorithm of integer factorization


def gcd(a,b):
    if a is 0:
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

x=2
y=2
number = 84923983
factor = pollard_rho(number,x,y)
while factor is number or 1:
    x = x+1
    y = y+1
    pollard_rho(number,x,y)
factor2 = int(number/factor)

print(factor,factor2)
