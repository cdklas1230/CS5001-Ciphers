'''
This part contains the encrypt and decrypt function of Playfair Cipher.
The encryption and decryption rule is that the key can only contain letters.
If numbers presented in plaintext/ciphertext, they will be removed.
Only the letters will be encrypted/decrypted. The length of ciphertext must
be even after removing all numbers.
'''

import utils


def encrypt(plaintext, key):
    '''
    Function -- encrypt
        encrypt the plaintext using Playfair Cipher.
    Parameters:
        plaintext -- some unencrypted data
        key -- a word where its letters are encoded
        into a 5 x 5 grid
    Returns a string of encrypted message
    Raises a TypeError or ValueError if any errors occur
    while reading the parameters
    '''
    if not isinstance(plaintext, str):
        raise TypeError('encrypt is expecting a string as'
                        ' the first parameter')
    if plaintext == '':
        raise ValueError('plaintext cannot be empty')
    if utils.contain_letters(plaintext) is False:
        raise ValueError('plaintext must contain letters')
    if not isinstance(key, str):
        raise TypeError('encrypt is expecting a string as'
                        ' the second parameter')
    if key.isalpha() is False:
        raise ValueError('key can only contain letters')
    if key == '':
        raise ValueError('Key cannot be empty')
    plaintext = utils.strip(plaintext)
    plaintext = utils.remove_numbers(plaintext)
    plaintext = plaintext.upper()
    key = key.upper()
    # use list to store letters in plain text
    text = []
    for i in range(len(plaintext)):
        text.append(plaintext[i])
    if len(text) % 2 != 0:
        text.append('X')
    for i in range(len(text)):
        if text[i] == 'J':
            text[i] = 'I'
    for i in range(1, len(text), 2):
        if text[i] == text[i - 1]:
            text[i] = 'X'
    # convert key to key square
    matrix = key_square(key)
    res = ''
    for i in range(0, len(text), 2):
        location1 = find_location(text[i], matrix)
        location2 = find_location(text[i + 1], matrix)
        # if the letters are in different rows and columns
        if location1[0] != location2[0] and location1[1] != location2[1]:
            new_location1 = [location1[0], location2[1]]
            new_location2 = [location2[0], location1[1]]
        # if the letters are on the same row
        elif location1[0] == location2[0]:
            new_location1 = [location1[0], (location1[1] + 1) % 5]
            new_location2 = [location2[0], (location2[1] + 1) % 5]
        # if the letters are on the same column
        else:
            new_location1 = [(location1[0] + 1) % 5, location1[1]]
            new_location2 = [(location2[0] + 1) % 5, location2[1]]
        # convert to letters based on their locations
        new_letter1 = find_word(new_location1, matrix)
        res += new_letter1
        new_letter2 = find_word(new_location2, matrix)
        res += new_letter2
    return res


def decrypt(ciphertext, key):
    '''
    Function -- decrypt
        decrypt the ciphertext using Playfair Cipher.
    Parameters:
        ciphertext -- some encrypted data
        key -- a word where its letters are encoded
        into a 5 x 5 grid
    Returns a string of decrypted message
    Raises a TypeError or ValueError if any errors occur
    while reading the parameters
    '''
    if not isinstance(ciphertext, str):
        raise TypeError('decrypt is expecting a string as'
                        ' the first parameter')
    if ciphertext == '':
        raise ValueError('ciphertext cannot be empty')
    if utils.contain_letters(ciphertext) is False:
        raise ValueError('ciphertext must contain letters')
    ciphertext = utils.strip(ciphertext)
    ciphertext = utils.remove_numbers(ciphertext)
    ciphertext = ciphertext.upper()
    if len(ciphertext) % 2 != 0:
        raise ValueError('ciphertext must contain even number of letters')
    if not isinstance(key, str):
        raise TypeError('decrypt is expecting a string as'
                        ' the second parameter')
    if key.isalpha() is False:
        raise ValueError('key can only contain letters')
    if key == '':
        raise ValueError('key cannot be empty')
    key = key.upper()
    matrix = key_square(key)
    # use list to store letters in cipher text
    text = []
    for i in range(len(ciphertext)):
        if ciphertext[i] == 'J':
            text.append('I')
        else:
            text.append(ciphertext[i])
    res = ''
    for i in range(0, len(text), 2):
        location1 = find_location(text[i], matrix)
        location2 = find_location(text[i + 1], matrix)
        # if the letters are in different rows and columns
        if location1[0] != location2[0] and location1[1] != location2[1]:
            new_location1 = [location1[0], location2[1]]
            new_location2 = [location2[0], location1[1]]
        # if the letters are on the same row
        elif location1[0] == location2[0]:
            new_location1 = [location1[0], (location1[1] - 1) % 5]
            new_location2 = [location2[0], (location2[1] - 1) % 5]
        # if the letters are on the same column
        else:
            new_location1 = [(location1[0] - 1) % 5, location1[1]]
            new_location2 = [(location2[0] - 1) % 5, location2[1]]
        # convert to letters based on their locations
        new_letter1 = find_word(new_location1, matrix)
        res += new_letter1
        new_letter2 = find_word(new_location2, matrix)
        res += new_letter2
    return res


def key_square(key):
    '''
    Function -- key_square
        Encode the letters of the key into a 5 x 5 grid
    Parameters:
        key -- a word where its letters are encoded
        into a 5 x 5 grid
    Returns a matrix of key square
    '''
    LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
               'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
               'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    new_key = []
    for i in key:
        if i not in new_key:
            new_key.append(i)
    for j in LETTERS:
        if j not in new_key:
            new_key.append(j)
    for k in range(len(new_key)):
        if new_key[k] == 'J':
            new_key[k] = 'I'
    matrix = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    start = 0
    for i in range(0, 5):
        for j in range(0, 5):
            matrix[i][j] = new_key[start]
            start += 1
    return matrix


def find_location(letter, matrix):
    '''
    Function -- find_location
        Find the location of a certain letter in the matrix
    Parameters:
        letter -- a letter in the text
        matrix -- the key square
    Returns a list of integers representing the location
    of that letter
    '''
    location = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == letter:
                location.append(i)
                location.append(j)
    return location


def find_word(location, matrix):
    '''
    Function -- find_word
        Find a certain letter's by its location in the matrix
    Parameters:
        location -- a list of integers representing the location
    of that letter
        matrix -- the key square
    Returns a string letter
    '''
    return matrix[location[0]][location[1]]
