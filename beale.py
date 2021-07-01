'''
This part contains the encrypt and decrypt function of Beale Cipher.
The encryption and decryption rule is that the if the book does not
contain certain letter in plaintext, it will raise an error.
Since the same number should not be used for the same letter throughout
encryption, if the book has used out all numbers for a letter,
it will raise an error.
If numbers presented in plaintext, they will be removed.
Only the letters will be encrypted.
If a number in ciphertext exceeds the length of the book, it will
raise an error.
'''

import utils
import random


def encrypt(plaintext, file_name, seed):
    '''
    Function -- encrypt
        encrypt the plaintext using Beale Cipher.
    Parameters:
        plaintext -- some unencrypted data
        file_name -- the book used to encode message
        seed -- an integer to make the generator pseudorandom
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
    plaintext = plaintext.lower()
    plaintext = utils.remove_numbers(plaintext)
    if not isinstance(seed, int):
        raise TypeError('encrypt is expecting an integer as'
                        ' the third parameter')
    content = read_data(file_name)
    dict = to_dict(content)
    random.seed(seed)
    res = ''
    for i in range(len(plaintext)):
        if plaintext[i] in dict:
            list = dict[plaintext[i]]
            if len(list) != 0:
                random_int = random.randint(0, len(list) - 1)
                res += str(list[random_int]) + ' '
                del dict[plaintext[i]][random_int]
            else:
                raise ValueError('The book has used out all words '
                                 'start with '
                                 + '\'' + plaintext[i] + '\'')
        else:
            raise ValueError('The book does not have a word starts with '
                             + '\'' + plaintext[i] + '\'')
    res = res.rstrip()
    return res


def decrypt(ciphertext, file_name):
    '''
    Function -- decrypt
        decrypt the ciphertext using Beale Cipher.
    Parameters:
        ciphertext -- some unencrypted data
        file_name -- the book used to encode message
    Returns a string of encrypted message
    Raises a TypeError or ValueError if any errors occur
    while reading the parameters
    '''
    content = read_data(file_name)
    len_content = 0
    for i in range(len(content)):
        for j in range(len(content[i])):
            len_content += 1
    if not isinstance(ciphertext, str):
        raise TypeError('decrypt is expecting a string as'
                        ' the first parameter')
    if ciphertext == '':
        raise ValueError('ciphertext cannot be empty')
    ciphertext = ciphertext.split()
    for i in range(len(ciphertext)):
        if not ciphertext[i].isdigit():
            raise ValueError('ciphertext can only contain numbers')
        if int(ciphertext[i]) > len_content:
            raise ValueError('wrong number ' + ciphertext[i] +
                             ' in ciphertext, which exceeds the length '
                             'of this book')
    res = ''
    start = 0
    while start < len(ciphertext):
        length = 0
        flag = False
        for i in range(len(content)):
            for j in range(len(content[i])):
                if length + j + 1 == int(ciphertext[start]):
                    res += content[i][j][0].upper()
                    start += 1
                    flag = True
                    break
                if j == len(content[i]) - 1:
                    length += len(content[i])
            if flag:
                break
    return res


def read_data(file_name):
    '''
    Function -- read_data
        reads all of the words in that file into a list and return
    Parameters:
        file_name -- accepts the name of a text file as a parameter
    Returns a list with all the words in the file
    Raises a ValueError if any errors occur while reading the file
    '''
    try:
        input_file = open(file_name, 'r')
        file_data = input_file.readlines()
        input_file.close()
        list1 = []
        for i in range(len(file_data)):
            list1.append(file_data[i].split())
        list1 = list(filter(None, list1))
        return list1
    except FileNotFoundError:
        raise
    except PermissionError:
        raise
    except OSError:
        raise


def to_dict(content):
    '''
    Function -- to_dict
        reads all of the words in the list and allocate their positions
        by their first letters
    Parameters:
        content -- a list contains all words
    Returns a dictionary with the first letters as key and positions
    as values
    '''
    dict = {}
    position = 1
    for j in range((len(content))):
        k = 0
        while k < len(content[j]):
            content[j][k] = content[j][k].lower()
            if content[j][k].endswith('-'):
                content[j][k] = content[j][k][0: -1] + content[j][k + 1]
                del content[j][k + 1]
            if content[j][k][0] in dict:
                dict[content[j][k][0]].append(position)
            else:
                dict[content[j][k][0]] = [position]
            k += 1
            position += 1
    return dict
