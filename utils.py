'''
This part contains helper functions that are common to multiple ciphers.
'''

import string
from string import digits


def strip(word):
    '''
    Function -- strip
        remove punctuation and white space in text
    Parameters:
        word -- a string of text
    Returns: a string without punctuation or white space
    '''
    # strip the punctuation out
    for c in string.punctuation:
        word = word.replace(c, "")
    # strip the space out
    return word.replace(" ", "")


def remove_numbers(text):
    '''
    Function -- remove_numbers
        remove numbers in text
    Parameters:
        word -- a string of text
    Returns: a string without numbers
    '''
    return text.translate(str.maketrans('', '', digits))


def contain_letters(text):
    '''
    Function -- contain_letters
        check if a text contains any letter
    Parameters:
        text -- a string of text
    Returns: a boolean value
    '''
    flag = False
    for i in range(len(text)):
        if text[i].isalpha() is True:
            flag = True
    return flag


def choose_menu():
    '''
    Function -- choose_menu
        read users' input choice
    Parameters:
        none
    Returns: the valid option
    '''
    while True:
        option = input()
        if (option != '1' and option != '2' and option != '3' and
                option != '4' and option != '5' and option != '6'
                and option != '7' and option != '8' and option != '9'
                and option != '10' and option != '11' and option != '12'
                and option != '13'):
            print('Invalid option, please choose again:')
        else:
            break
    return option


def confirm_selection():
    '''
    Function -- confirm_selection
        read users' input choice
    Parameters:
        none
    Returns: the valid option
    '''
    while True:
        option = input()
        option = option.lower()
        if option == 'y' or option == 'n':
            break
        else:
            print('Invalid option, please choose again:')
    return option


def check_text():
    '''
    Function -- check_text
        check users' input
    Parameters:
        none
    Returns: the valid text
    '''
    while True:
        text = input()
        if text == '':
            print('Text cannot be empty, please try again:')
        else:
            break
    return text


def check_int_key():
    '''
    Function -- check_int_key
        check users' input
    Parameters:
        none
    Returns: the valid key
    '''
    key = None
    while key is None:
        input_value = input()
        try:
            key = int(input_value)
        except ValueError:
            print('Input is not an integer, please try again:')
    return key


def check_str_key():
    '''
    Function -- check_str_key
        check users' input
    Parameters:
        none
    Returns: the valid key
    '''
    while True:
        key = input()
        if key == '':
            print('Key cannot be empty, please try again:')
        elif key.isalpha() is False:
            print('Key must only contain letters, please try again:')
        else:
            break
    return key


def check_book():
    '''
    Function -- check_book
        check users' input
    Parameters:
        none
    Returns: the valid key
    '''
    suffix = '.txt'
    while True:
        book = input()
        if book == '':
            print('Book cannot be empty, please try again: ')
        elif not book.endswith(suffix):
            print('Wrong book name, should end with .txt, '
                  'please try again: ')
        else:
            break
    return book
