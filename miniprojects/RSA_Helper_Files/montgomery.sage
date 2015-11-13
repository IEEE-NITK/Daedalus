""" Counts the number of digits in the binary form of the number """
def count_digits(number):
    return (len(bin(number))-2)

"""helps compute r, where  r>m,r is coprime to m and is a power of two"""
def finding_r(m):
    power_of_two=count_digits(m)
    r=2**power_of_two
    return r

""" computes u, for given a,b and modulo m, u=abr(mod m)"""
def compute_u(t,mdash,m,r):
    u = (t +((t*mdash)%r)*m)//r
    if(u>=m):
        return u-m
    else:
        return u

"""computes modulo of a product"""
def compute_mod(number,r,m):
    return (number*r)%m

def strip_powers_of_two(c, p, q, gamma, delta):
    c=c/2
    if (p % 2 == 0) and (q % 2 == 0):
        p, q = p//2, q//2
    else:
        p, q = (p + delta)//2, (q - gamma)//2
    return c, p, q

"""Extended binary GCD.
    Given input a, b the function returns d, s, t such that gcd(a,b) = d = as + bt."""
def ext_bin_gcd(a,b):
    u, v, s, t, r = 1, 0, 0, 1, 0
    while (a % 2 == 0) and (b % 2 == 0):
        a, b, r = a//2, b//2, r+1
    alpha, beta = a, b
    while (a % 2 == 0):
        a, u, v = strip_powers_of_two(a, u, v, alpha, beta)
    while a != b:
        if (b % 2 == 0):
            b, s, t = strip_powers_of_two(b, s, t, alpha, beta)
        elif b < a:
            a, b, u, v, s, t = b, a, s, t, u, v
        else:
            b, s, t = b - a, s - u, t - v
    return (2 ** r) * a, s, t

def compute_a_power_n_modm(a,n,m):
    r=finding_r(m)
    print "r is %s"%(r)
    a_bar=compute_mod(a,r,m)
    # b_bar=compute_mod(b,r,m)
    prev=a%m
    dummy,rinv,mdash=ext_bin_gcd(r,m)
    mdash=-mdash
    print "r inverse is %s"%(rinv)
    print "m dash is %s"%(mdash)
    while(n>1):
        prev=(prev*(r%m))%m
        t=a_bar*prev
        u=compute_u(t,mdash,m,r)
        prev=compute_mod(u,rinv,m)
        n=n-1
    print "answer is %s"%prev

a=input("Enter the number")
n=input("Enter the power")
m=input("Enter modulo");
compute_a_power_n_modm(a,n,m)


