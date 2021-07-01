'''
This part contains the main function and other functions to
implement all of the required functionality.
'''

import utils
import caesar
import railfence
import playfair
import substitution
import beale
import straddle


def main_menu():
    '''
    Function -- main_menu
        provides a visualized menu to users
    Parameters:
        none
    Returns: none
    '''
    flag = True
    while flag:
        print('-------------Encryption and Decryption--------------')
        print('          1 - encrypt using Caesar Cipher')
        print('          2 - decrypt using Caesar Cipher')
        print('          3 - encrypt using Rail Fence Cipher')
        print('          4 - decrypt using Rail Fence Cipher')
        print('          5 - encrypt using Playfair Cipher')
        print('          6 - decrypt using Playfair Cipher')
        print('          7 - encrypt using Substitution Cipher')
        print('          8 - decrypt using Substitution Cipher')
        print('          9 - encrypt using Beale Cipher')
        print('          10 - decrypt using Beale Cipher')
        print('          11 - encrypt using Straddle Cipher')
        print('          12 - decrypt using Straddle Cipher')
        print('          13 - quit')
        print()
        print('             Please make your selection:')

        choice = utils.choose_menu()

        if choice == '1':
            caesar_encrypt()
        elif choice == '2':
            caesar_decrypt()
        elif choice == '3':
            railfence_encrypt()
        elif choice == '4':
            railfence_decrypt()
        elif choice == '5':
            playfair_encrypt()
        elif choice == '6':
            playfair_decrypt()
        elif choice == '7':
            substitution_encrypt()
        elif choice == '8':
            substitution_decrypt()
        elif choice == '9':
            beale_encrypt()
        elif choice == '10':
            beale_decrypt()
        elif choice == '11':
            straddle_encrypt()
        elif choice == '12':
            straddle_decrypt()
        else:
            print('Are you sure you want to exit?(y/n)')
            confirm = utils.confirm_selection()
            if confirm == 'y':
                flag = False


def caesar_encrypt():
    '''
    Function -- caesar_encrypt
        Use the encrypt function from caesar.py
    Parameters:
        none
    Returns: none
    Raises a TypeError or ValueError if any errors occur
    while reading the parameters
    '''
    print('encrypt using Caesar Cipher')
    print('Please enter your plaintext: ')
    plaintext = utils.check_text()
    print('Please enter your key:')
    key = utils.check_int_key()
    try:
        res = caesar.encrypt(plaintext, key)
        print('Encrypted text is:', res)
    except TypeError as ex:
        print(ex)
    except ValueError as ex:
        print(ex)


def caesar_decrypt():
    '''
    Function -- caesar_decrypt
        Use the decrypt function from caesar.py
    Parameters:
        none
    Returns: none
    Raises a TypeError or ValueError if any errors occur
    while reading the parameters
    '''
    print('decrypt using Caesar Cipher')
    print('Please enter your ciphertext: ')
    ciphertext = utils.check_text()
    print('Please enter your key:')
    key = utils.check_int_key()
    try:
        res = caesar.decrypt(ciphertext, key)
        print('Decrypted text is:', res)
    except TypeError as ex:
        print(ex)
    except ValueError as ex:
        print(ex)


def railfence_encrypt():
    '''
    Function -- railfence_encrypt
        Use the encrypt function from railfence.py
    Parameters:
        none
    Returns: none
    Raises a TypeError or ValueError if any errors occur
    while reading the parameters
    '''
    print('encrypt using Rail Fence Cipher')
    print('Please enter your plaintext:')
    plaintext = utils.check_text()
    print('Please enter your key:')
    key = utils.check_int_key()
    try:
        res = railfence.encrypt(plaintext, key)
        print('Encrypted text is:', res)
    except TypeError as ex:
        print(ex)
    except ValueError as ex:
        print(ex)


def railfence_decrypt():
    '''
    Function -- railfence_decrypt
        Use the decrypt function from railfence.py
    Parameters:
        none
    Returns: none
    Raises a TypeError or ValueError if any errors occur
    while reading the parameters
    '''
    print('decrypt using Rail Fence Cipher')
    print('Please enter your ciphertext:')
    ciphertext = utils.check_text()
    print('Please enter your key:')
    key = utils.check_int_key()
    try:
        res = railfence.decrypt(ciphertext, key)
        print('Decrypted text is:', res)
    except TypeError as ex:
        print(ex)
    except ValueError as ex:
        print(ex)


def playfair_encrypt():
    '''
    Function -- playfair_encrypt
        Use the encrypt function from playfair.py
    Parameters:
        none
    Returns: none
    Raises a TypeError or ValueError if any errors occur
    while reading the parameters
    '''
    print('encrypt using Playfair Cipher')
    print('Please enter your plaintext:')
    plaintext = utils.check_text()
    print('Please enter your key:')
    key = utils.check_str_key()
    try:
        res = playfair.encrypt(plaintext, key)
        print('Encrypted text is:', res)
    except TypeError as ex:
        print(ex)
    except ValueError as ex:
        print(ex)


def playfair_decrypt():
    '''
    Function -- playfair_decrypt
        Use the decrypt function from playfair.py
    Parameters:
        none
    Returns: none
    Raises a TypeError or ValueError if any errors occur
    while reading the parameters
    '''
    print('decrypt using Playfair Cipher')
    print('Please enter your ciphertext:')
    ciphertext = utils.check_text()
    print('Please enter your key:')
    key = utils.check_str_key()
    try:
        res = playfair.decrypt(ciphertext, key)
        print('Decrypted text is:', res)
    except TypeError as ex:
        print(ex)
    except ValueError as ex:
        print(ex)


def substitution_encrypt():
    '''
    Function -- substitution_encrypt
        Use the encrypt function from substitution.py
    Parameters:
        none
    Returns: none
    Raises a TypeError or ValueError if any errors occur
    while reading the parameters
    '''
    print('encrypt using Substitution Cipher')
    print('Please enter your plaintext:')
    plaintext = utils.check_text()
    print('Please enter your key:')
    key = utils.check_str_key()
    try:
        res = substitution.encrypt(plaintext, key)
        print('Encrypted text is:', res)
    except TypeError as ex:
        print(ex)
    except ValueError as ex:
        print(ex)


def substitution_decrypt():
    '''
    Function -- substitution_decrypt
        Use the decrypt function from substitution.py
    Parameters:
        none
    Returns: none
    Raises a TypeError or ValueError if any errors occur
    while reading the parameters
    '''
    print('decrypt using Substitution Cipher')
    print('Please enter your ciphertext:')
    ciphertext = utils.check_text()
    print('Please enter your key:')
    key = utils.check_str_key()
    try:
        res = substitution.decrypt(ciphertext, key)
        print('Encrypted text is:', res)
    except TypeError as ex:
        print(ex)
    except ValueError as ex:
        print(ex)


def beale_encrypt():
    '''
    Function -- beale_encrypt
        Use the encrypt function from beale.py
    Parameters:
        none
    Returns: none
    Raises a TypeError or ValueError if any errors occur
    while reading the parameters
    '''
    print('encrypt using Beale Cipher')
    print('Please enter your plaintext:')
    plaintext = utils.check_text()
    print('Please enter your book:')
    book = utils.check_book()
    print('Please enter your seed:')
    seed = utils.check_int_key()
    try:
        res = beale.encrypt(plaintext, book, seed)
        print('Encrypted text is:', res)
    except TypeError as ex:
        print(ex)
    except ValueError as ex:
        print(ex)
    except FileNotFoundError as ex:
        print(ex)
    except PermissionError as ex:
        print(ex)
    except OSError as ex:
        print(ex)


def beale_decrypt():
    '''
    Function -- beale_decrypt
        Use the decrypt function from beale.py
    Parameters:
        none
    Returns: none
    Raises a TypeError or ValueError if any errors occur
    while reading the parameters
    '''
    print('decrypt using Beale Cipher')
    print('Please enter your ciphertext:')
    ciphertext = utils.check_text()
    print('Please enter your book:')
    book = utils.check_book()
    try:
        res = beale.decrypt(ciphertext, book)
        print('Decrypted text is:', res)
    except TypeError as ex:
        print(ex)
    except ValueError as ex:
        print(ex)
    except FileNotFoundError as ex:
        print(ex)
    except PermissionError as ex:
        print(ex)
    except OSError as ex:
        print(ex)


def straddle_encrypt():
    '''
    Function -- straddle_encrypt
        Use the encrypt function from straddle.py
    Parameters:
        none
    Returns: none
    Raises a TypeError or ValueError if any errors occur
    while reading the parameters
    '''
    print('encrypt using Straddle Cipher')
    print('Please enter your plaintext:')
    plaintext = utils.check_text()
    print('Please enter your alphabetic key:')
    alphabetic_key = utils.check_str_key()
    print('Please enter your numeric key: ')
    numeric_key = utils.check_int_key()
    print('Please enter your adder key: ')
    adder_key = utils.check_int_key()
    try:
        res = straddle.encrypt(plaintext,
                               alphabetic_key, numeric_key, adder_key)
        print('Encrypted text is:', res)
    except TypeError as ex:
        print(ex)
    except ValueError as ex:
        print(ex)


def straddle_decrypt():
    '''
    Function -- straddle_decrypt
        Use the decrypt function from straddle.py
    Parameters:
        none
    Returns: none
    Raises a TypeError or ValueError if any errors occur
    while reading the parameters
    '''
    print('decrypt using Straddle Cipher')
    print('Please enter your ciphertext:')
    ciphertext = utils.check_text()
    print('Please enter your alphabetic key:')
    alphabetic_key = utils.check_str_key()
    print('Please enter your numeric key: ')
    numeric_key = utils.check_int_key()
    print('Please enter your adder key: ')
    adder_key = utils.check_int_key()
    try:
        res = straddle.decrypt(ciphertext,
                               alphabetic_key, numeric_key, adder_key)
        print('Decrypted text is:', res)
    except TypeError as ex:
        print(ex)
    except ValueError as ex:
        print(ex)


def main():
    main_menu()


if __name__ == '__main__':
    main()
