'''
This part contains the encrypt and decrypt function of Substitution cipher.
The encryption and decryption rule is that the key must contain all 26 letters,
no duplicates.
If numbers presented in plaintext/ciphertext, they will remain unchanged.
Only the letters will be encrypted/decrypted.
'''

import utils


def encrypt(plaintext, key):
    '''
    Function -- encrypt
        encrypt the plaintext using Substitution cipher.
    Parameters:
        plaintext -- some unencrypted data
        key -- 26-letter alphabetic key that contains
        all of the letters of the alphabet that are completely jumbled.
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
    if not isinstance(key, str):
        raise TypeError('encrypt is expecting a string as'
                        ' the second parameter')
    if key == '':
        raise ValueError('Key cannot be empty')
    if len(key) != 26:
        raise ValueError('key must be 26 characters in length')
    if len(set(key)) != 26:
        raise ValueError('key must contains all of the '
                         'letters of the alphabet')
    key = key.upper()
    res = ''
    for i, c in enumerate(plaintext):
        if c.isdigit():
            res += c
        else:
            res += key[ord(plaintext[i]) - 65]
    return res


def decrypt(ciphertext, key):
    '''
    Function -- decrypt
        decrypt the ciphertext using Substitution cipher.
    Parameters:
        ciphertext -- some encrypted data
        key -- 26-letter alphabetic key that contains
        all of the letters of the alphabet that are completely jumbled.
    Returns a string of decrypted message
    Raises a TypeError or ValueError if any errors occur
    while reading the parameters
    '''
    if not isinstance(ciphertext, str):
        raise TypeError('decrypt is expecting a string as'
                        ' the first parameter')
    if ciphertext == '':
        raise ValueError('ciphertext cannot be empty')
    ciphertext = utils.strip(ciphertext)
    ciphertext = ciphertext.upper()
    if not isinstance(key, str):
        raise TypeError('decrypt is expecting a string as'
                        ' the second parameter')
    if key == '':
        raise ValueError('key cannot be empty')
    if len(key) != 26:
        raise ValueError('key must be 26 characters in length')
    if len(set(key)) != 26:
        raise ValueError('key must contains all of the '
                         'letters of the alphabet')
    key = key.upper()
    res = ''
    for i, c in enumerate(ciphertext):
        if c.isdigit():
            res += c
        for j in range(len(key)):
            if ciphertext[i] == key[j]:
                res += chr(j + 65)
    return res
