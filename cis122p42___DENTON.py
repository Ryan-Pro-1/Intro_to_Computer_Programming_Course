'''
CIS 122 Spring 2022 Project 4-1
Author(s): Ryan Denton
Credit: CIS 122 Resources
Description: FizzBuzz Game
'''

def fb(n):
    '''
    Prints 'Fizz!' if integer is divisible by 3.
    Prints 'Buzz!' if integer is divisible by 5.
    Prints 'FizzBuzz!!' if integer is divisible by 3 and 5.
    Prints value of integer if neither apply.
    Function prints this list from integers 1 to n, then prints 'Game over!'.

    >>>fb(15)
    1
    2
    Fizz!
    4
    Buzz!
    Fizz!
    7
    8
    Fizz!
    Buzz!
    11
    Fizz!
    13
    14
    FizzBuzz!!
    Game over!
    '''
    for n in range(1, n+1):
        if (n % 5 == 0) and (n % 3 == 0):
            print('FizzBuzz!!')
        elif n % 3 == 0:
            print('Fizz!')
        elif n % 5 == 0:
            print('Buzz!')
        else:
            print(n)

    print('Game over!')
    return

def main():
    '''
    Main Driver for the FizzBuzz game.
    Asks user for input and runs funtion 'fb(n)' based on input.
    '''
    
    x = int(input('Enter positive integer to start the FizzBuzz game: '))
    n = x

    fb(n)

    return

#Now let's attempt the challenge part of the project
def fb(n, a, b):
    '''
    Prints 'Fizz!' if integer is divisible by a.
    Prints 'Buzz!' if integer is divisible by b.
    Prints 'FizzBuzz!!' if integer is divisible by a and b.
    Prints value of integer if neither apply.
    Function prints this list from integers 1 to n, then prints 'Game over!'.

    >>>fb(10, 2, 3)
    1
    Fizz!
    Buzz!
    Fizz!
    5
    FizzBuzz!
    7
    Fizz!
    Buzz!
    Fizz!
    Game over!
    '''
    for n in range(1, n+1):
        if (n % a == 0) and (n % b == 0):
            print('FizzBuzz!!')
        elif n % a == 0:
            print('Fizz!')
        elif n % b == 0:
            print('Buzz!')
        else:
            print(n)

    print('Game over!')
    return
