'''
CIS 122 Spring 2022 Project 8-2
Author(s): Ryan Denton
Credit: CIS 122 Resources
Description: Password Checker
'''

import doctest

def len_check(p):
    '''
    Checks the length of the password to make sure it is of length 6 or greater.
    Returns True if password meets this condition or returns False if it does not.

    >>> len_check('ghT')
    False

    >>> len_check('123 56')
    True

    >>> len_check('hGyd$')
    False

    >>> len_check('123456')
    True
    '''
    if len(p) < 6:
        return False
    else:
        return True

def E_e_check(p):
    '''
    Checks the password for the letter 'E' or 'e'.
    Returns False if 'E' or 'e' is a part of the password or
    returns True is they are not.

    >>> E_e_check('er5423')
    False

    >>> E_e_check('55yh d')
    True

    >>> E_e_check('t$ EkhY2')
    False

    >>> E_e_check('45$gjFFg')
    True
    '''
    for char in p:
        if char == 'E' or char == 'e':
            return False
        
    return True

def upper_case_check(p):
    '''
    Checks the password for an uppercase letter.
    Returns True if there is an uppercase letter in the password
    or returns False if there is not one.

    >>> upper_case_check('jgh76$')
    False

    >>> upper_case_check('887hGT5$ y')
    True

    >>> upper_case_check('# hTTf45')
    True

    >>> upper_case_check('jhh  vc5')
    False

    >>> upper_case_check('sfdg78##')
    False
    '''
    for char in p:
        if char.isupper():
            return True
        
    return False

def number_check(p):
    '''
    Checks the password for at least one number being present.
    Returns True if there is at least one number or returns
    False if there are no numbers in the password.

    >>> number_check('dfgag')
    False

    >>> number_check('sfg 54$')
    True

    >>> number_check('HH^#df67')
    True
    
    >>> number_check('hh G$')
    False
    '''
    for char in p:
        if char.isdigit():
            return True

    return False
    
def special_char_check(p):
    '''
    Checks the password for at least one special character
    being present. (i.e. !, @, #, $, %, ^, &).
    Returns True if there is at least one special character or
    returns False if there are no special character in the
    password.

    >>> special_char_check('sdfgt56')
    False

    >>> special_char_check('H 564$fg')
    True

    >>> special_char_check('kjadfHH534 7')
    False

    >>> special_char_check('hd55 s$# 65')
    True
    '''
    for char in p:
        if char == '!':
            return True
        elif char == '@':
            return True
        elif char == '#':
            return True
        elif char == '$':
            return True
        elif char == '%':
            return True
        elif char == '^':
            return True
        elif char == '&':
            return True

    return False
    
def password_check(p):
    '''
    Checks the password to make sure it is of proper length and contents.
    Returns True if password meets conditions and False if it does not.

    >>> password_check('A99#!') 
    False
     
    >>> password_check('') 
    False
    
    >>> password_check('#Qwerty') 
    False
    
    >>> password_check('#qwerty') 
    False
    
    >>> password_check('Qwerty99') 
    False
    
    >>> password_check('123456') 
    False

    >>> password_check('#Qwzrty') 
    False
    
    >>> password_check('#Qw9rty') 
    True
    
    >>> password_check('OK99!!') 
    True
    '''
    if not len_check(p):
        return False
    elif not E_e_check(p):
        return False
    elif not upper_case_check(p):
        return False
    elif not number_check(p):
        return False
    elif not special_char_check(p):
        return False

    return True

print(doctest.testmod())

def main():
    '''
    Main driver for checking a password. Asks for a password and checks
    that all conditions are met to ensure a strong enough password
    based upon SecuriCorp's new security regulations.
    Tells the user if the password is secure enough.
    If password is not secure enough (i.e. does not meet the new regulations)
    if asks the user to re-enter a new one until it is secure enough.

    >>> main()
    Please input password: jsrkjg HH$5
    This password is secure, thank you.

    >>> main()
    Please input password: hkdr 4
    This is not a secure password, please try again
    Please input password: bnm @F
    This is not a secure password, please try again
    Please input password: dhy^@M hg45
    This password is secure, thank you.

    >>> main()
    Please input password: jhgVF54$
    This password is secure, thank you.
    '''
    while True:
        p = input('Please input password: ')

        if password_check(p):
            print('This password is secure. SecuriCorp appreciates you!')
            return
        else:
            print('This is not a secure password, try again.')
    return

