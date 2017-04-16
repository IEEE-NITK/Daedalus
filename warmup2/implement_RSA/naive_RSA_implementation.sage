def modexp(a, b, n):
	a_power_b_mod_n = 1
	for i in list(Integer.binary(b)):
		a_power_b_mod_n = mod(a_power_b_mod_n*a_power_b_mod_n, n)
		if(Integer(i)==1):
			a_power_b_mod_n = mod(a_power_b_mod_n*a, n)
	return Integer(a_power_b_mod_n)

def generate_keys():
	prime1 = random_prime(2^1025-1,False,2^1024)
	prime2 = random_prime(2^1025-1,False,2^1024)
	print "prime1- " + str(prime1)
	print "prime2- " + str(prime2)
	N = prime1*prime2
	phi_N = (prime1-1)*(prime2-1)
	e = 0x10001
	print "modulus N- " + str(N)
	print "public key exponent e- " + str(e)
	bezout = xgcd(e, phi_N)
	d = Integer(mod(bezout[1], phi_N))
	print "private key exponent d- " + str(d)
	return [N,e,phi_N,d]

##message = Integer(raw_input("Enter message(max length 2048 bits)- "))
##key_list = generate_keys()
##print "message- " + str(message)
##N = key_list[0]
##e = key_list[1]
##phi_N = key_list[2]
#d = key_list[3]
#
##Encryption
#ciphertext = modexp(message, e, N)
#print "ciphertext- " + str(ciphertext)
#
##Decryption
#plaintext = modexp(ciphertext, d, N)
#print "decrpyted plaintext- " + str(plaintext)
#print plaintext == message	
