length_N = 256
p = next_prime(2^int(round(length_N/2)))
q = next_prime(round(pi.n()*p))
N = p*q
e = 3
print "N"
print N
ZmodN = Zmod(N)

M1 = ZZ.random_element(0,2^60)
diff = ZZ.random_element(0,2^6)
M2   =  M1 + diff 
C1   =  ZmodN(M1)^e
C2   =  ZmodN(M2)^e
a = 1 
b = diff 

R.<x> = PolynomialRing(ZmodN)
g1 = x^e - C1
g2 = (x+diff)^e - C2

print g2.gcd(g1)
