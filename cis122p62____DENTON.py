'''
CIS 122 Spring 2022 Project 6-2
Author(s): Ryan Denton
Credit: CIS 122 Resources
Description: Rock, Paper, Scissors Game
'''

import random

def rps():
    '''
    Determines winner of rock, paper, scissors game by going through
    each of the possible outcomes of the game.

    >>> rps()
        Player 1 got: s and player 2 got: s.
        Seems to be a tie. Play again!!!
        Player 1 got: p and player 2 got: r.
        Player 1 wins!!
    '''

    player_1 = ''
    player_2 = ''

    while player_1 == player_2:
        player_1 = random.choice('rps')
        player_2 = random.choice('rps')
        print(f'Player 1 got: {player_1} and player 2 got: {player_2}.')
        
        if player_1 == 'r' and player_2 == 's':
            print('Player 1 wins!!')
        elif player_1 == 's' and player_2 == 'p':
            print('Player 1 wins!!')
        elif player_1 == 'p' and player_2 == 'r':
            print('Player 1 wins!!')
        elif player_2 == 'r' and player_1 == 's':
            print('Player 2 wins!!')
        elif player_2 == 's' and player_1 == 'p':
            print('Player 2 wins!!')
        elif player_2 == 'p' and player_1 == 'r':
            print('Player 2 wins!!')
        else:
            print('Seems to be a tie. Play again!!!')

    return
