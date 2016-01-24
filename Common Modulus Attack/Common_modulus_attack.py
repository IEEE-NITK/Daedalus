#!/usr/bin/python2

"""
TO DO
1.Documentation
2.Testing
3.Optimizations(if any)
"""

from sys import argv
from Crypto.PublicKey import RSA

def encode(message_string):
	
	input_tokens = ""
#	
	for character in message_string:
		
		temp = str((bin(ord(character)))[2:])
		
		if(len(temp) != 8):
			temp = (8-len(temp))*"0" + temp
			
		input_tokens += temp
		
	return int(input_tokens,2)
	
def decode(encoded_number):
	
	decoded_message = ""
	
	encoded_number = int(encoded_number)
	
	binary_string = bin(encoded_number)[2:]
	
	if( len(binary_string) % 8 != 0 ):
	
		binary_string = (8 - (len(binary_string) % 8)) * "0" + binary_string
		
	while(len(binary_string) > 0):
	
		temp = int(binary_string[0:8],2)
		
		decoded_message += chr(temp)
		
		binary_string = binary_string[8:]
		
	return decoded_message		
	
def extended_euclidian_algorithm(private_exponent_e1, private_exponent_e2):
	
	private_exponent_e1 = int(private_exponent_e1)
	
	private_exponent_e2 = int(private_exponent_e2)
	
	if(private_exponent_e2 > private_exponent_e2):
	
		private_exponent_e1 , private_exponent_e2 = private_exponent_e2 , private_exponent_e1
	
	
	x , y , u , v = 0 , 1 , 1 , 0
	
	while ( private_exponent_e1 != 0 ):
	
		quotient , remainder = private_exponent_e2 // private_exponent_e1 , private_exponent_e2 % private_exponent_e1
		
		m , n = x - ( u * quotient ) , y - ( v * quotient )
		
		private_exponent_e2 , private_exponent_e1 , x , y , u , v = private_exponent_e1 , remainder , u , v , m , n
	
	gcd = private_exponent_e2
	
	return gcd , x , y
	
def extract_exponents(public_key_file_1 , public_key_file_2):
	
	pem_file_one = open(public_key_file_1,'r')
	pem_file_two = open(public_key_file_2,'r')
	
	key_one = RSA.importKey(pem_file_one.read())
	key_two = RSA.importKey(pem_file_two.read())
	
	if ( key_one.n != key_two.n ):
		print 'Unable to implement common modulus attack.'
		print 'Modulii are different. :('
		return None
	
	pem_file_one.close()
	pem_file_two.close()
	
	return key_one.e , key_two.e , key_one.n

if ( len(argv) != 5 ):

	print "insufficient arguements"

file_to_decrypt_1 = open(argv[3],'r')
file_to_decrypt_2 = open(argcv[4],'r')

encrypted_1 = file_to_decrypt.read()
encrypted_encoded_1 = encode(encrypted_1)

encrypted_2 = file_to_decrypt_2.read()
encrypted_encoded_2 = encode(encrypted_2)

exponents = extract_exponents(argv[1],argv[2])

compute_x_and_y = extended_euclidian_algorithm(exponents(0),exponents(1))

decoded = ( ( encrypted_encoded_1 ** compute_x_and_y(1) ) * ( encrypted_encoded_2 ** compute_x_and_y(2)) % exponents(2)

final_decrypted = decode(decoded)
	

