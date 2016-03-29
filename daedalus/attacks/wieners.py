
from sys import argv
#Weiner's attack - private key d is small

def check (s,N,e):
    #Code snippet to check for right (k,d) pair which satisfies
    #1.phi(N)=e*d-1/k is a whole number
    #2.d must be odd as phi(N) is even.
    #e,N and known (public key components)
    #N=pq , phi(N)=N-(p+q)+1=(p-1)(q-1)
    #returns d
    D=0
    for (k,d) in s:
        if(k!=0):
            if (d%2!=0 and (e*d-1)%k==0):
                phi=(e*d-1)/k;
                p=find_root(x^2+(phi-N-1)*x+N==0,0,sqrt(N))# quadratic equation with p,q, as roots
                q=find_root(x^2+(phi-N-1)*x+N==0,sqrt(N),N)
                if((p-int(p)<=0.00001) and (q-int(q)<=0.000001)):  #chk if integer roots
                    D=d                                           
                    print "Private key found ! \nFactors of N- "
                print p
                print q
    return D

#function to get continued fractions of the rational number p/q
def contfrac(p,q):
    while q:
        n = p // q
        yield n
        q, p = p - q*n, q

#get convergents of continued fractions cf
def convergents(cf):
    r, s, p, q = 0, 1, 1, 0
    for c in cf:
        r, s, p, q = p, q, c*p+r, c*q+s
        yield p, q

def expmod(m,e,n):
    #Returns c congruent to m power e modulo n.
    c=1
    for i in range(0,e):
        c=(c*m)%n
    return c

def encrypt(m,e,n):
    #Encrypts message m with public key exponent e.
    #To be combined with expmod as the same function.
    return expmod(m,e,n)

def decrypt(c,d,n):
    #Decrypts message using private key d
    return expmod(c,d,n)

def attack(input):
	errors=""
	results=[]
	try:
		N=input['n']
		e=input['e']
	except:
		errors="Wrong input Format"
	d=check(list(convergents(contfrac(e,N))),N,e)
	results.append(d)
	return {'errors': errors, 'results': results}

