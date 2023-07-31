'''
CIS 122 Spring 2022 Project 6-1
Author(s): Ryan Denton
Credit: CIS 122 Resources
Description: Square root approximation
'''

import math

def mysqrt(a):
    '''
    Estimates the square root of a parameter value 'a' using the Babylonian method
    and uses it's own approximation in a loop until it is within 0.0000001
    of the actual answer and then prints the result when that condition is met.

    >>> mysqrt(9)
        3.0

    >>> mysqrt(44)
        6.6332495807108
    '''
    
    x = 1
    epsilon = .0000001

    while True:
        y = (x + a/x) / 2
        if abs(y - x) < epsilon:
            break
        x = y

    return y

def square_root_compare():
    '''
    Runs though the 'mysqrt(a)' function and the 'math.sqrt(a)' functions as well
    as finds the difference between these two function estimates from a = 1
    to a = 10.
    Then formats these results in columns for easier viewing/comparison.

    >>> square_root_compare()
        1    1.0                      1.0                      0.0                      
        2    1.414213562373095        1.4142135623730951       2.220446049250313e-16    
        3    1.7320508075688772       1.7320508075688772       0.0                      
        4    2.000000000000002        2.0                      2.220446049250313e-15    
        5    2.23606797749979         2.23606797749979         0.0                      
        6    2.449489742783178        2.449489742783178        0.0                      
        7    2.6457513110645907       2.6457513110645907       0.0                      
        8    2.82842712474619         2.8284271247461903       4.440892098500626e-16    
        9    3.0                      3.0                      0.0                      
        10   3.162277660168379        3.1622776601683795       4.440892098500626e-16
    '''

    for a in range(1, 11):
        mysqrt(a)
        math.sqrt(a)
        diff = abs(mysqrt(a) - math.sqrt(a))
        print(f'{a:<5}{mysqrt(a):<25}{math.sqrt(a):<25}{diff:<25}')

    return

def main():
    '''
    Main driver for square root calculator.
    Prints header and lists estimates from 'mysqrt(a)' function, answer from
    'math.sqrt(a)', and the difference between them from a = 1 to a = 10.

    >>> main()
        Square Root Calculator

        a    mysqrt(a)                math.sqrt(a)             diff                     
        1    1.0                      1.0                      0.0                      
        2    1.414213562373095        1.4142135623730951       2.220446049250313e-16    
        3    1.7320508075688772       1.7320508075688772       0.0                      
        4    2.000000000000002        2.0                      2.220446049250313e-15    
        5    2.23606797749979         2.23606797749979         0.0                      
        6    2.449489742783178        2.449489742783178        0.0                      
        7    2.6457513110645907       2.6457513110645907       0.0                      
        8    2.82842712474619         2.8284271247461903       4.440892098500626e-16    
        9    3.0                      3.0                      0.0                      
        10   3.162277660168379        3.1622776601683795       4.440892098500626e-16
    '''
    
    # print table header
    print('\nSquare Root Calculator\n')
    print(f'{"a":5}{"mysqrt(a)":25}{"math.sqrt(a)":25}{"diff":25}')
    
    square_root_compare()
    
    return
