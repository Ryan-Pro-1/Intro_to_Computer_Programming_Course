'''
CIS 122 Spring 2022 Project 7-1
Author(s): Ryan Denton
Credit: CIS 122 Resources
Description: In the Loop: DNA to RNA Transcription
'''

import doctest

def transcribe1(s):
    '''
    Transcribes DNA genetic information into RNA information through
    the proper letter conversion based on input 's' into the function,
    using a for loop.

    >>> transcribe1('ACGT TGCA')
    'UGCAACGU'
        
    >>> transcribe1('GATTACA')
    'CUAAUGU'
        
    >>> transcribe1('GAtTtTACA')
    'CUAAUGU'
        
    >>> transcribe1('TTt ACT')
    'AAUGA'
        
    >>> transcribe1('cs5')
    ''
    '''

    RNA_string = ''

    for char in s:
        if char == 'A':
            RNA_string += 'U'
        elif char == 'C':
            RNA_string += 'G'
        elif char == 'G':
            RNA_string += 'C'
        elif char == 'T':
            RNA_string += 'A'

    return RNA_string

def transcribe2(s):
    '''
    Transcribes DNA genetic information into RNA information through
    the proper letter conversion based on input 's' into the function,
    using a while loop.

    >>> transcribe2('ACGT TGCA')
    'UGCAACGU'
        
    >>> transcribe2('GATTACA')
    'CUAAUGU'
        
    >>> transcribe2('GAtTtTACA')
    'CUAAUGU'
        
    >>> transcribe2('TTt ACT')
    'AAUGA'
        
    >>> transcribe2('cs5')
    ''
    '''

    RNA_string = ''
    index = 0
    
    while index < len(s):
        char = s[index]
        
        if char == 'A':
            RNA_string += 'U'
        elif char == 'C':
            RNA_string += 'G'
        elif char == 'G':
            RNA_string += 'C'
        elif char == 'T':
            RNA_string += 'A'
        index += 1

    return RNA_string

print(doctest.testmod())
