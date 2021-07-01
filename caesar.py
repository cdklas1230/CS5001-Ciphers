'''
This part contains the encrypt and decrypt function of Caesar cipher.
The encryption and decryption rule is that if numbers presented in
plaintext/ciphertext, they will remain unchanged.
Only the letters will be encrypted/decrypted.
'''

import utils


def encrypt(plaintext, key):
    '''
    Function -- encrypt
        encrypt the plaintext using Caesar cipher.
    Parameters:
        plaintext -- some unencrypted data
        key -- indicate certain number of places 'shifted'
    Returns a string of encrypted message
    Raises a TypeError or ValueError if any errors occur
    while reading the parameters
    '''
    if not isinstance(plaintext, str):
        raise TypeError('encrypt is expecting a string as'
                        ' the first parameter')
    if plaintext == '':
        raise ValueError('plaintext cannot be empty')
    plaintext = utils.strip(plaintext)
    plaintext = plaintext.upper()
    if not isinstance(key, int):
        raise TypeError('encrypt is expecting an integer as'
                        ' the second parameter')
    if key == '':
        raise ValueError('Key cannot be empty')
    if key < 0:
        raise ValueError('Key cannot be negative')
    res = ''
    for i, c in enumerate(plaintext):
        if c.isdigit():
            res += c
        else:
            res += chr(((ord(c) + key) - 65)
                       % (90 - 65 + 1) + 65)
    return res


def decrypt(ciphertext, key):
    '''
    Function -- decrypt
        decrypt the ciphertext using Caesar cipher.
    Parameters:
        ciphertext -- some encrypted data
        key -- indicate certain number of places 'shifted'
    Returns a string of decrypted message
    Raises a TypeError or ValueError if any errors occur
    while reading the parameters
    '''
    if not isinstance(ciphertext, str):
        raise TypeError('decrypt is expecting a string as'
                        ' the first parameter')
    if ciphertext == '':
        raise ValueError('ciphertext cannot be empty')
    if not isinstance(key, int):
        raise TypeError('decrypt is expecting an integer as'
                        ' the second parameter')
    if key == '':
        raise ValueError('key cannot be empty')
    if key < 0:
        raise ValueError('Key cannot be negative')
    ciphertext = utils.strip(ciphertext)
    ciphertext = ciphertext.upper()
    res = ''
    for i, c in enumerate(ciphertext):
        if c.isdigit():
            res += c
        else:
            res += chr(((ord(c) - key) - 65)
                       % (90 - 65 + 1) + 65)
    return res
