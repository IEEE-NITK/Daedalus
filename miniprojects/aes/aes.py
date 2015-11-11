from sage.all import *


# In most AES implementations, the S-Box is not explicitly computed.
# Instead, lookup tables like the one below are used.
sbox = [
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16
]

# Constant matrix used in the MixColumn sublayer
constantMatrix = Matrix([
    [0x02, 0x03, 0x01, 0x01],
    [0x01, 0x02, 0x03, 0x01],
    [0x01, 0x01, 0x02, 0x03],
    [0x03, 0x01, 0x01, 0x02]
])

# Byte Substitution layer
# =======================

def subBytes(state):
    size = len(state)
    for i in range(size):
        index = ord(state[i])
        state[i] = sbox[index]
    return state

# ShiftRows sublayer
# ===================

# Python slices are a handy way to easily rotate a row
def rotate(row, shift):
    return row[shift:] + row[:shift]

# Each row gets shifted cyclically by n, where n is the row number
def shiftRows(state):
    for i in range(4):
        state[i*4:i*4+4] = [chr(x) for x in rotate(state[i*4:i*4+4], i)]
    return state

# MixColumn sublayer
# ==================

# Convert hex number to Galois field polynomial
# Couldn't find an inbuilt way to do this...
def numToPoly(num):
    # Convert hex number to binary string
    bitVector = bin(num)[2:]
    while len(bitVector) != 8:
        bitVector = "0" + bitVector
    # Initialize a Galois field of size 256
    f = GF(2**8, 'x')
    x = f.gen()
    res = f(0)
    for i in range(8):
        res += f(int(bitVector[i]) * x**i)
    return res

def mixColumns(state):
    output = [[] for i in range(4)]
    f = GF(2**8, 'x')
    x = f.gen()
    # construct vector and multiply with matrix
    for i in range(4):
        inputColumn = [ord(state[i]), ord(state[i+4]), ord(state[i+8]), ord(state[i+12])]
        for j in range(4):
            c = f(0)
            for k in range(4):
                c += numToPoly(constantMatrix[j][k]) * numToPoly(inputColumn[k])
            # <3 Sage functions!
            output[i].append(c.integer_representation())

    out = [chr(item) for sublist in output for item in sublist]
    return out

# Key Addition Layer
# ==================

def addRoundKey(state, roundKey):
    for i in range(len(state)):
        state[i] = chr(ord(state[i]) ^ ord(roundKey[i]))

def g(row, roundNum):
    # Cyclic left shift by 1
    row = rotate(row, 1)
    # S-box substitution
    for i in range(len(row)):
        row[i] = sbox[row[i]]
    # Add round coefficient (RC) to first byte
    f = GF(2**8, 'x')
    x = f.gen()
    RC = f(x**(roundNum - 1))
    row[0] = (numToPoly(row[0]) + RC).integer_representation()
    return row


def keySchedule(key):
    W = [[] for x in range(44)]
    key = [ord(ch) for ch in key]
    W[0:4] = [key[i:i+4] for i in range(0, 13, 4)]
    f = GF(2**8, 'x')
    x = f.gen()
    for i in range(1, 11):
        glist = g(W[4*i-1], i)
        for j in range(4):
            W[4*i].append((numToPoly(W[4*(i-1)][j]) + numToPoly(glist[j])).integer_representation())
        for j in range(1, 4):
            for k in range(4):
                W[4*i+j].append((numToPoly(W[4*i+j-1][k]) + numToPoly(W[4*(i-1)+j][k])).integer_representation())
    W = [chr(item) for sublist in W for item in sublist]
    return ''.join(W)

# returns a 16-byte round key based on an expanded key and round number
def createRoundKey(expandedKey, n):
    return expandedKey[(n*16):(n*16+16)]

def encrypt(IV):
    key = raw_input('Enter key: ')
    ptext = raw_input('Enter plaintext: ')
    ctext = []
    first = True
    # Padding to a multiple of 16
    if len(ptext) % 16 != 0:
        padChar = 16 - len(ptext) % 16
    while len(ptext) % 16 != 0:
        ptext += padChar

    expandedKey = keySchedule(list(key))

    pos = 0
    plain = []
    while pos != len(ptext):
        if first == True:
            state = IV
            first = False
        else:
            state = ctext[len(ctext) - 1]
        plain = list(ptext[pos:pos+16])
        roundNum = 0
        roundKey = createRoundKey(expandedKey, roundNum)
        addRoundKey(state, roundKey)
        while roundNum < 10:
            roundKey = createRoundKey(expandedKey, roundNum)
            state = subBytes(state)
            state = shiftRows(state)
            if roundNum != 9:
                state = mixColumns(state)
            addRoundKey(state, roundKey)
            roundNum += 1
        for i in range(len(state)):
            state[i] = chr(ord(state[i]) ^ ord(plain[i]))
        ctext.append(''.join(state))
        pos += 16

    print "Encrypted text: ", ''.join(ctext)
    print "Bytes: ", [hex(ord(ch)) for ch in ''.join(ctext)]

# Driver
if __name__ == '__main__':
    choice = raw_input('1. Encrypt\n2. Decrypt\n')
    if choice == '1':
        IV = []
        for i in range(16):
            IV.append(chr(randint(0, 255)))
        encrypt(IV)
    elif choice == '2':
        print 'Nothing yet!'
    else:
        print 'Uh-oh. Only 1 or 2!'
