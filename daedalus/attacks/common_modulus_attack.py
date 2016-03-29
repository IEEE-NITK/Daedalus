#!/usr/bin/python2

"""
TO DO
1.Line comments
2.Testing
3.Optimizations(if any)
"""

#The input{} must have 
#1. Encrypted Message files E and F.
#2. Public Key 1 and 2 with their paths as strings.
#3. Example:
#   {
#Key1:"/media/jk/jl/key1.pem"
#Key2:"/media/user/ll/key2.pem"
#}

from Crypto.PublicKey import RSA

#The global error basket: To collect all the errors that occur during the attack operation.
errors = []
"""
The encode function encodes the message string into a number,
by taking the binary representation of the character and appending
them all together to form one big number.
"""
def encode(message_string): 
    
    input_tokens = ""
    for character in message_string:
        temp = str((bin(ord(character)))[2:])
        if(len(temp) != 8):
            temp = (8-len(temp))*"0" + temp
        input_tokens = input_tokens + temp[-8:]
    return int(input_tokens,2)

"""
End of the encode function
"""

"""
The decode function is designed to recover the original string,
assuming that the encoding was done using the above function.
"""
def decode(encoded_number):
    
    decoded_message = ""
    encoded_number = int(encoded_number)
    binary_string = bin(encoded_number)[2:]
    
    if( len(binary_string) % 8 != 0 ):
        binary_string = (8 - (len(binary_string) % 8)) * "0" + binary_string

    while(len(binary_string) > 0):
        temp = int(binary_string[:8],2)
        decoded_message += chr(temp)
        binary_string = binary_string[8:]

    return decoded_message

"""
The extended euclidian algoithm returns a tuple consisting of three numbers:
1. gcd of the two parameters.
2. Bezout's* identity x and y for the given parameters.
*Given two integers a and b, Bezout's identity integers x and y are two integers
that satisfy the below condition,
(a*x) + (b*y) = gcd(a,b)
"""
def extended_euclidian_algorithm(private_exponent_e1, private_exponent_e2):
    
    try:
        private_exponent_e1 = int(private_exponent_e1)
        private_exponent_e2 = int(private_exponent_e2)
    
        
        x , y , u , v = 0 , 1 , 1 , 0
        
        while ( private_exponent_e1 != 0 ):
            
            quotient , remainder = private_exponent_e2 // private_exponent_e1 , private_exponent_e2 % private_exponent_e1
            m , n = x - ( u * quotient ) , y - ( v * quotient )
            private_exponent_e2 , private_exponent_e1 , x , y , u , v = private_exponent_e1 , remainder , u , v , m , n

        gcd = private_exponent_e2
        return gcd , x , y
    except Exception as e:
        globals()['errors'].append(e)

"""
The parameters for extract_exponents() must be a valid file location,
parsable by python.
It also checks if the both the key files have the same modulus.
The function returns a tuple consisting of:
1. Exponent e1 of the first key.
2. Exponent e2 of the second key.
3. The (common) modulus n.
"""
def extract_exponents(public_key_file_1 , public_key_file_2):
    
    try:
        pem_file_one = open(public_key_file_1,'r')
        pem_file_two = open(public_key_file_2,'r')
        key_one = RSA.importKey(pem_file_one.read())
        key_two = RSA.importKey(pem_file_two.read())

        if ( key_one.n != key_two.n ):
        
            globals()['errors'].append('Unable to implement common modulus attack.Modulii are different. :(')
            return None

        pem_file_one.close()
        pem_file_two.close()
        return key_one.e , key_two.e , key_one.n

    except Exception as e:
        globals()['errors'].append(e)


"""
The driver function attack():in accordance with the guidelines specified,
performs exponent extraction,
decryption, and
decoding
It returns the results by adding an entry to the dictionary: results.
The key for the result is "common modulus attack"
"""
def attack(inputs={'m1':"encrypted_text_1.txt",'m2':"encrypted_text_2.txt"}, errors=[], results={}):
    try:
        
        file_to_decrypt_1 = open(inputs['m1'],'r')
        file_to_decrypt_2 = open(inputs['m2'],'r')
        encrypted_1 = file_to_decrypt_1.read()
        encrypted_encoded_1 = encode(encrypted_1)
        encrypted_2 = file_to_decrypt_2.read()
        encrypted_encoded_2 = encode(encrypted_2)


        E = raw_input("Enter the filename containing the First set of public keys:Example-/usr/folder/file1\n")
        F = raw_input("Enter the filename containing the Second set of keys:Example-/usr/folder/file2\n")
        #E="mpub.pem"
        #F="kpub.pem"
        exponents = extract_exponents(E,F)
        compute_x_and_y = extended_euclidian_algorithm(exponents[0],exponents[1])
        if(compute_x_and_y[1]<0):
            
            a=  encrypted_encoded_1 ** (-compute_x_and_y[1])
            b=  encrypted_encoded_2 ** (compute_x_and_y[2])
            decoded=(b/a)
        else:
            
            a=  encrypted_encoded_1 ** (compute_x_and_y[1])
            b=  encrypted_encoded_2 ** (-compute_x_and_y[2])
            decoded=(a/b)
        decoded=decoded%(exponents[2])
        final_decrypted = decode(decoded)
        results["common modulus attack"] = final_decrypted
        #print final_decrypted
    except Exception as e:
        globals()['errors'].append(e)
    return {'errors': globals()['errors'], 'results': results}


#a=attack()
#print a
