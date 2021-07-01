'''
This part contains the encrypt and decrypt function of Rail Fence Cipher.
The encryption and decryption rule is that if numbers presented in
plaintext/ciphertext, they will be removed.
Only the letters will be encrypted/decrypted.
'''

import utils


def encrypt(plaintext, key):
    '''
    Function -- encrypt
        encrypt the plaintext using Rail Fence Cipher.
    Parameters:
        plaintext -- some unencrypted data
        key -- indicate the number of "rails"
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
    if not isinstance(key, int):
        raise TypeError('encrypt is expecting an integer as'
                        ' the second parameter')
    if key == '':
        raise ValueError('Key cannot be empty')
    if key < 2:
        raise ValueError('Key must be at least 2')
    rail = []
    for i in range(0, key - 1):
        rail.append(i)
    for j in range(key - 1, 0, -1):
        rail.append(j)
    # use dictionary to store letters on each rail
    dict = {}
    for k in range(len(plaintext)):
        count = rail[k % len(rail)]
        if count in dict:
            dict[count].append(plaintext[k])
        else:
            dict[count] = [plaintext[k]]
    # extract all values in order
    res = ''
    for val in dict.keys():
        for letter in dict[val]:
            res += letter
    return res


def decrypt(ciphertext, key):
    '''
    Function -- decrypt
        decrypt the ciphertext using Rail Fence Cipher.
    Parameters:
        ciphertext -- some encrypted data
        key -- indicate the number of "rails"
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
    ciphertext = utils.remove_numbers(ciphertext)
    ciphertext = ciphertext.upper()
    if not isinstance(key, int):
        raise TypeError('decrypt is expecting an integer as'
                        ' the second parameter')
    if key == '':
        raise ValueError('key cannot be empty')
    if key < 2:
        raise ValueError('Key must be at least 2')
    # calculate the length of each row
    count = 2 * key - 2
    len1 = int(len(ciphertext) / count)
    base_len = len1 * count
    diff = len(ciphertext) - base_len
    no_middle_row = key - 2
    if no_middle_row != 0:
        len_middle_row = int((base_len - len1 * 2) / no_middle_row)
    else:
        len_middle_row = 0
    # use list to indicate number of letters on each rail
    list = []
    list.append(len1)
    while no_middle_row > 0:
        list.append(len_middle_row)
        no_middle_row -= 1
    list.append(len1)
    rail = []
    for i in range(0, key - 1):
        rail.append(i)
    for j in range(key - 1, 0, -1):
        rail.append(j)
    rail = rail[0: count - 1]
    for k in range(len(rail)):
        if diff > 0:
            list[rail[k % len(rail)]] += 1
        diff -= 1
    # split ciphertext by length
    text = []
    start = 0
    for i in range(len(list)):
        text.append(ciphertext[start: start + list[i]])
        start = start + list[i]
    # rearrange text to plain text
    order = []
    for i in range(0, key - 1):
        order.append(i)
    for j in range(key - 1, 0, -1):
        order.append(j)
    res = ''
    for i in range(len(ciphertext)):
        count = order[i % len(order)]
        res += text[count][0]
        text[count] = text[count][1:]
    return res
