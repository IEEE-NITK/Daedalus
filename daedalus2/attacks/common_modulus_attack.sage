#!/usr/bin/python2

#The input{} must have 
#1. Encrypted Message files E and F.
#2. Public Key 1 and 2 with their paths as strings.
#3. Example:
#   {
#Key1:"/media/jk/jl/key1.pem"
#Key2:"/media/user/ll/key2.pem"
#}

from Crypto.PublicKey import RSA
from Crypto.Util.number import bytes_to_long,long_to_bytes

#The global error basket: To collect all the errors that occur during the attack operation.
errors = []

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
def attack(inputs={'m1':"e_m.txt",'m2':"e_k.txt"}, errors=[], results={}):
    try:
        
        file_to_decrypt_1 = open(inputs['m1'],'r')
        file_to_decrypt_2 = open(inputs['m2'],'r')
        encrypted_1 = file_to_decrypt_1.read()
        encrypted_2 = file_to_decrypt_2.read()
        """
        The bytes_to_long() function encodes the message string into a number,
        by taking the binary representation of the character and appending
        them all together to form one big number.
        """
        encrypted_encoded_1=bytes_to_long(encrypted_1)    
        encrypted_encoded_2=bytes_to_long(encrypted_2)

        E = raw_input("Enter the filename containing the First set of public keys:Example-/usr/folder/file1\n")
        F = raw_input("Enter the filename containing the Second set of keys:Example-/usr/folder/file2\n")
        #E="mpub.pem"
        #F="kpub.pem"
        exponents = extract_exponents(E,F)
        
        """
        The extended euclidian algoithm returns a tuple consisting of three numbers:
        1. gcd of the two parameters.
        2. Bezout's identity x and y for the given parameters.
        *Given two integers a and b, Bezout's identity integers x and y are two integers
        that satisfy the below condition,
        (a*x) + (b*y) = gcd(a,b)
        """
        try:
            compute_x_and_y=xgcd(exponents[0],exponents[1])
        except Exception as e:
            globals()['errors'].append(e)
            
        
        if(compute_x_and_y[1]<0):
            
            a=  encrypted_encoded_1 ** (-compute_x_and_y[1])
            b=  encrypted_encoded_2 ** (compute_x_and_y[2])
            decoded=(b/a)
        else:
            
            a=  encrypted_encoded_1 ** (compute_x_and_y[1])
            b=  encrypted_encoded_2 ** (-compute_x_and_y[2])
            decoded=(a/b)

        decoded=decoded%(exponents[2])
        
        """
        The long_to_bytes() function is designed to recover the original string,
        assuming that the encoding was done using the bytes_to_long() function.
        """
        final_decrypted=long_to_bytes(decoded)
        
        results["common modulus attack"] = final_decrypted
    
    except Exception as e:
        globals()['errors'].append(e)
    
    return {'errors': globals()['errors'], 'results': results}

if __name__ == "__main__":
    a=attack()
    print a
