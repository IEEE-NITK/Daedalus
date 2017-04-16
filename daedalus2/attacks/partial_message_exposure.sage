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


def partial_message_exposure(input):
    
    N = input['N']
    e = input['e']
    C = input['C']
    K = input['known_plaintext']
    
    ZmodN = Zmod(N)
    P.<x> = PolynomialRing(ZmodN) 
    pol   = (K+x)^e - C 
    dd    = pol.degree()
    
    beta  = 1.0
    epsilon = beta/7
    mm = ceil(beta**2/(dd*epsilon))
    tt = floor(dd * mm * ((1/beta) - 1))
    XX = ceil(N**((beta**2/dd)-epsilon))
    roots = coppersmith_howgrave_univariate(pol, N, beta, mm, tt, XX)
    result = {};
    result['results'] = roots
    result['errors']  = 'No error'
    if(len(roots)==0):
    	result['errors'] = 'No solution found'
    return result 
	
