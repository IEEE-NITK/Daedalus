#Coppersmith's attack

#Input: 
#1. The message (msg)
#2. The number of parties to which the encrypted message is to be sent (num_parties)

#Possible Errors/Exceptions:
#1. If the modular inverse does not exist
#2. If the inputs to the Chinese Remainder Theorem function are not pairwise coprime (encrypted message, n from the public key)

#Results:
#1. The public key
#2. The encrypted message
#3. Solutions to the Chinese Remainder Theorem
#4. The hacked message

import random

errors=[]

def isPrime(i):
    '''
    Tests to see if a number is prime.
    '''
    for j in range(2,i):
        if i%j==0:
            return False
    return True

def Prime():
    '''
    generates random prime numbers
    '''
    primes = [i for i in range(3,1000) if isPrime(i)]
    r = random.choice(primes)
    return r

def Modulus(p, q):
    n = p * q
    return n

def EulerTotientFn(p,q):
    z = (p-1) * (q-1)
    return z

def gcd(a,b):
    """Returns the greatest common divisor of a and b
    If a and b are positive, result is always positive.
    Sign maybe positive or negative otherwise.
    """
    if(a < b):
        a,b=b,a
    while(b != 0):
        a,b = b,a%b
    return a

def modinv(e, z):
    '''
    Euclid's extended algorithm for finding the multiplicative inverse of two numbers
    '''
    g, x, y = extended_gcd(e, z)
    if(g!= 1):
        try:
            raise Exception("modular inverse does not exist")
        except Exception as e:
            globals()['errors'].append(e)
    else:
        return x % z
        
def encrypt(m,n,e):
    '''
    computes message^e mod n
    '''
    return (m ** e)%n

def extended_gcd(a, b):
    """Return (r, s, d) where a*r + b*s = d and d = gcd(a,b)"""
    x,y = 0, 1
    lastx, lasty = 1, 0

    while b:
        a, (q, b) = b, divmod(a,b)
        x, lastx = lastx-q*x, x
        y, lasty = lasty-q*y, y

    return (lastx, lasty, a)


def chinese_remainder_theorem(items):
  """Solve the chinese remainder theorem
  Given a list of items (a_i, n_i) solve for x such that x = a_i (mod n_i)
  such that 0 <= x < product(n_i)
  Assumes that n_i are pairwise co-prime.
  """

  # Determine N, the product of all n_i
  N = 1
  for a, n in items:
    N *= n

  # Find the solution (mod N)
  result = 0
  for a, n in items:
    m = N//n
    r, s, d = extended_gcd(n, m)
    if(d!= 1):
        try:
            raise Exception("Input not pairwise co-prime")
        except Exception as e:
            globals()['errors'].appends(e)
    result += a*s*m

  # Make sure we return the canonical solution.
  return result % N

def attack(inputs):
  results={}
  e=3
  cipher=[]
  N = []
  m = 1
  C = 0


  #print "Input a message"
  message = inputs[0]

  #print "Enter number of parties you wish to send encrypted message."
  No_parties = inputs[1]

  for party in range (0,No_parties):
      while(1):
          p = Prime()
          q = Prime()
          while (p==q):
              p=Prime()
              q=Prime()

          n = Modulus(p, q)
          z = EulerTotientFn(p,q)
          if(gcd(e,z)==1):
              break;

        
      publicKey=[e,n]
      results["Public key"]= publicKey
      en= encrypt(message,n,e)
      cipher.append(en)
      N.append(n)
      results["encrypted message "]=cipher[party]

  items=[]
  for i in xrange(0,No_parties):
      items.append((cipher[i],N[i]))

  C=chinese_remainder_theorem(items)
  hacked_message = C ** (1/3.0)
  results["hacked message"]=hacked_message
  print hacked_message

  return {'errors': globals()['errors'], 'results': results}
inputs=[14,7]


attack(inputs)
