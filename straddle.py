'''
This part contains the encrypt and decrypt function of Straddle Cipher.
The encryption and decryption rule is that the alphabetic key must contain
all 26 letters, no duplicates. The numeric key must be 2 distinct numbers
greater than 0, no repetition. The adder key can be any length or zero,
but cannot be negative.
If numbers presented in plaintext, they will be removed.
Only the letters will be encrypted.
'''

import utils


def encrypt(plaintext, alphabetic_key, numeric_key, adder_key):
    '''
    Function -- encrypt
        encrypt the plaintext using Straddle Cipher.
    Parameters:
        plaintext -- some unencrypted data
        alphabetic key -- a word where its letters are encoded
        into a 5 x 5 grid
        numeric key -- 2 distinct numbers greater than zero
        adder key -- another numeric value of any length
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
    plaintext = utils.remove_numbers(plaintext)
    plaintext = plaintext.upper()
    if not isinstance(alphabetic_key, str):
        raise TypeError('encrypt is expecting a string as'
                        ' the second parameter')
    if alphabetic_key == '':
        raise ValueError('Alphabetic key cannot be empty')
    if alphabetic_key.isalpha() is False:
        raise ValueError('Alphabetic key can only contain letters')
    if len(alphabetic_key) != 26:
        raise ValueError('Alphabetic key must be 26 characters in length')
    if len(set(alphabetic_key)) != 26:
        raise ValueError('Alphabetic key must contain all of the letters '
                         'of the alphabet')
    alphabetic_key = alphabetic_key.upper()
    if not isinstance(numeric_key, int):
        raise TypeError('encrypt is expecting an integer as'
                        ' the third parameter')
    if numeric_key == '':
        raise ValueError('Numeric key cannot be empty')
    if len(str(numeric_key)) != 2:
        raise ValueError('Numeric key must contain 2 distinct numbers')
    if int(str(numeric_key)[0]) <= 0:
        raise ValueError('Numbers in numeric key must be greater than 0')
    if int(str(numeric_key)[1]) <= 0:
        raise ValueError('Numbers in numeric key must be greater than 0')
    if int(str(numeric_key)[0]) == int(str(numeric_key)[1]):
        raise ValueError('Numbers in numeric key must be distinct')
    if not isinstance(adder_key, int):
        raise TypeError('encrypt is expecting an integer as'
                        ' the fourth parameter')
    if adder_key == '':
        raise ValueError('Adder key cannot be empty')
    if adder_key < 0:
        raise ValueError('Adder key cannot be negative')
    # find key square
    numeric_key_1 = numeric_key // 10
    numeric_key_2 = numeric_key - numeric_key_1 * 10
    matrix = key_square(alphabetic_key, numeric_key_1, numeric_key_2)
    # convert plaintext to numeric text
    numeric_text = []
    for i in range(len(plaintext)):
        location = find_location(plaintext[i], matrix)
        if type(location) == tuple:
            numeric_text.append(location[0])
            numeric_text.append(location[1])
        else:
            numeric_text.append(location)
    # convert adder key to a list
    adder = to_list(adder_key)
    # convert numeric text to adder text
    if adder_key == 0:
        adder_text = numeric_text
    else:
        adder_text = []
        for i in range(len(numeric_text)):
            new_value = (numeric_text[i] + adder[i % len(adder)]) % 10
            adder_text.append(new_value)
    # convert adder text to cipher text
    start = 0
    ciphertext = ''
    while start < len(adder_text):
        if adder_text[start] == numeric_key_1 \
                or adder_text[start] == numeric_key_2:
            location = []
            location.append(adder_text[start])
            if start != len(adder_text) - 1:
                location.append(adder_text[start + 1])
                letter = find_letter(location, matrix)
                ciphertext += str(letter)
                start += 2
            else:
                break
        else:
            location = []
            location.append(adder_text[start])
            letter = find_letter(location, matrix)
            ciphertext += str(letter)
            start += 1
    return ciphertext


def decrypt(ciphertext, alphabetic_key, numeric_key, adder_key):
    '''
    Function -- decrypt
        decrypt the plaintext using Straddle Cipher.
    Parameters:
        ciphertext -- some encrypted data
        alphabetic key -- a word where its letters are encoded
        into a 5 x 5 grid
        numeric key -- 2 distinct numbers greater than zero
        adder key -- another numeric value of any length
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
    if not isinstance(alphabetic_key, str):
        raise TypeError('decrypt is expecting a string as'
                        ' the second parameter')
    if alphabetic_key == '':
        raise ValueError('Alphabetic key cannot be empty')
    if alphabetic_key.isalpha() is False:
        raise ValueError('Alphabetic key can only contain letters')
    if len(alphabetic_key) != 26:
        raise ValueError('Alphabetic key must be 26 characters in length')
    if len(set(alphabetic_key)) != 26:
        raise ValueError('Alphabetic key must contain all of the letters '
                         'of the alphabet')
    alphabetic_key = alphabetic_key.upper()
    if not isinstance(numeric_key, int):
        raise TypeError('decrypt is expecting an integer as'
                        ' the third parameter')
    if numeric_key == '':
        raise ValueError('Numeric key cannot be empty')
    if len(str(numeric_key)) != 2:
        raise ValueError('Numeric key must contain 2 distinct numbers')
    if int(str(numeric_key)[0]) <= 0:
        raise ValueError('Numbers in numeric key must be greater than 0')
    if int(str(numeric_key)[1]) <= 0:
        raise ValueError('Numbers in numeric key must be greater than 0')
    if int(str(numeric_key)[0]) == int(str(numeric_key)[1]):
        raise ValueError('Numbers in numeric key must be distinct')
    if not isinstance(adder_key, int):
        raise TypeError('decrypt is expecting an integer as'
                        ' the fourth parameter')
    if adder_key == '':
        raise ValueError('Adder key cannot be empty')
    if adder_key < 0:
        raise ValueError('Adder key cannot be negative')
    # find key square
    numeric_key_1 = numeric_key // 10
    numeric_key_2 = numeric_key - numeric_key_1 * 10
    matrix = key_square(alphabetic_key, numeric_key_1, numeric_key_2)
    # convert ciphertext to adder text
    adder_text = []
    for i in range(len(ciphertext)):
        location = find_location(ciphertext[i], matrix)
        if type(location) == tuple:
            adder_text.append(location[0])
            adder_text.append(location[1])
        else:
            adder_text.append(location)
    # convert adder key to a list
    adder = to_list(adder_key)
    # convert adder text to numeric text
    if adder_key == 0:
        numeric_text = adder_text
    else:
        numeric_text = []
        for i in range(len(adder_text)):
            new_value = (adder_text[i] - adder[i % len(adder)]) % 10
            numeric_text.append(new_value)
    # convert numeric text to plaintext
    start = 0
    plaintext = ''
    while start < len(numeric_text):
        if numeric_text[start] == numeric_key_1 \
                or numeric_text[start] == numeric_key_2:
            location = []
            location.append(numeric_text[start])
            if start != len(numeric_text) - 1:
                location.append(numeric_text[start + 1])
                letter = find_letter(location, matrix)
                plaintext += str(letter)
                start += 2
            else:
                break
        else:
            location = []
            location.append(numeric_text[start])
            letter = find_letter(location, matrix)
            plaintext += str(letter)
            start += 1
    return plaintext


def key_square(alphabetic_key, numeric_key_1, numeric_key_2):
    '''
    Function -- key_square
        Encode the letters of the alpha key into a 3 x 10 grid
        using the numeric key
    Parameters:
        alphabetic key -- a word where its letters are encoded
        into a 5 x 5 grid
        numeric key 1 -- the first number of a 2 distinct numbers
        greater than zero
        numeric key 2 -- the second number of a 2 distinct numbers
        greater than zero
    Returns a matrix of key square
    '''
    matrix = [['', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [numeric_key_1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [numeric_key_2, 0, 0, 0, 0, 0, 0, 0, 0, str(0), str(1)]]
    start = 0
    for i in range(1, 4):
        for j in range(1, 11):
            if i == 1 and (j == numeric_key_1 + 1
                           or j == numeric_key_2 + 1):
                matrix[i][j] = ''
            else:
                matrix[i][j] = alphabetic_key[start]
                start += 1
            if start == len(alphabetic_key):
                break
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
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == letter:
                if i == 1:
                    return matrix[0][j]
                elif i == 2:
                    return matrix[2][0], j - 1
                else:
                    return matrix[3][0], j - 1


def find_letter(location, matrix):
    '''
    Function -- find_letter
        Find a certain letter's by its location in the matrix
    Parameters:
        location -- a list of integers representing the location
    of that letter
        matrix -- the key square
    Returns a string letter
    '''
    if len(location) == 1:
        return matrix[1][location[0] + 1]
    elif location[0] == matrix[2][0]:
        return matrix[2][location[1] + 1]
    else:
        return matrix[3][location[1] + 1]


def to_list(integer):
    '''
    Function -- to_list
        Convert an integer into a list by its digits
    Parameters:
        integer -- an integer number
    Returns a list
    '''
    list = []
    while integer:
        list.append(integer % 10)
        integer = integer // 10
    list.reverse()
    return list
