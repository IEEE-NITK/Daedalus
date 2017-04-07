import time
from Crypto.Util.number import bytes_to_long, long_to_bytes 

debug = False

# display matrix picture with 0 and X
def matrix_overview(BB, bound):
    for ii in range(BB.dimensions()[0]):
        a = ('%02d ' % ii)
        for jj in range(BB.dimensions()[1]):
            a += '0' if BB[ii,jj] == 0 else 'X'
            a += ' '
        if BB[ii, ii] >= bound:
            a += '~'
        print a

def coppersmith_howgrave_univariate(pol, modulus, beta, mm, tt, XX):
    
    dd = pol.degree()
    nn = dd * mm + tt

    
    # Coppersmith revisited algo for univariate polynomials 

    # change ring of pol and x
    polZ = pol.change_ring(ZZ)
    x = polZ.parent().gen()

    # compute polynomials
    gg = []
    for ii in range(mm):
        for jj in range(dd):
            gg.append((x * XX)**jj * modulus**(mm - ii) * polZ(x * XX)**ii)
    for ii in range(tt):
        gg.append((x * XX)**ii * polZ(x * XX)**mm)
    
    # construct lattice B
    BB = Matrix(ZZ, nn)

    for ii in range(nn):
        for jj in range(ii+1):
            BB[ii, jj] = gg[ii][jj]

    # display basis matrix
    if debug:
        matrix_overview(BB, modulus^mm)

    # LLL
    BB = BB.LLL()

    # transform shortest vector in polynomial    
    new_pol = 0
    for ii in range(nn):
        new_pol += x**ii * BB[0, ii] / XX**ii

    # factor polynomial
    potential_roots = new_pol.roots()
    print "potential roots:", potential_roots

    # test roots
    roots = []
    for root in potential_roots:
        if root[0].is_integer():
            result = polZ(ZZ(root[0]))
            if gcd(modulus, result) >= modulus^beta:
                roots.append(ZZ(root[0]))

    return roots

# RSA gen options (for the demo)
length_N = 1024  # size of the modulus
Kbits = 200      # size of the root
e = 3

# RSA gen (for the demo)
p = next_prime(2^int(round(length_N/2)))
q = next_prime(p)
N = p*q
ZmodN = Zmod(N)

# Create problem (for the demo)
plaintext = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
#known_plaintext = "dolore magna aliqua."
#K = Integer(bytes_to_long(known_plaintext))
#Kdigits = K.digits(2)
#M = [0]*Kbits + [1]*(length_N-Kbits); 
#for i in range(len(Kdigits)):
#    M[i] = Kdigits[i]
#M = ZZ(M, 2)
#print "plaintext"
#print K
#print bytes_to_long(plaintext)
#print "M"
#print M
M = Integer(bytes_to_long(plaintext))
unknown = Integer(str(M.digits()[-40:]))
known = Integer(str(M.digits()[0:len(M.digits())-40]))
print M
print unknown
print known
C = ZmodN(M)^e

# Problem to equation (default)
P.<x> = PolynomialRing(ZmodN) #, implementation='NTL')
pol = (2^length_N - 2^Kbits + x)^e - C
dd = pol.degree()

# Tweak those
beta = 1                                # b = N
epsilon = beta / 7                      # <= beta / 7
mm = ceil(beta**2 / (dd * epsilon))     # optimized value
tt = floor(dd * mm * ((1/beta) - 1))    # optimized value
XX = ceil(N**((beta**2/dd) - epsilon))  # optimized value

# Coppersmith
start_time = time.time()
roots = coppersmith_howgrave_univariate(pol, N, beta, mm, tt, XX)

# output
print "\n# Solutions"
print "we want to find:",str(K)
print "we found:", str(roots)
print("in: %s seconds " % (time.time() - start_time))
print "\n"
print roots," as plaintext ", long_to_bytes(int(''.join(map(str,roots))))
