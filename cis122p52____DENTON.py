'''
Title: Project 5-2 – Housing Priority 
Author: Ryan Denton
Credits: Based on project by Evan Peck, Bucknell University 
Description: Collect user attributes and calculate a housing priority score 
based on this input.
'''

def is_eligible():
    '''
    Determines eligibility of fourth year student depending on their input
    when asked if they graduate or not this year. If they do graduate this
    year, returns False.
    If they do not graduate this year, returns True.

    >>> is_eligible()
        Will you graduate this year? (yes or no): yes
        False
    '''
    
    x = input('Will you graduate this year? (yes or no): ')
    
    if x == 'yes':
        return False
    elif x == 'no':
        return True
    else:
        print('Invalid input. Please try again.')
        
    return

def housing_priority(year, age, off_campus, acad_prob, disc_prob):
    '''
    Determines housing score based on school year, age, if student teacher
    living off campus or not, and if on academic and/or disciplinary probation.
    Then returns score as integer.

    >>> housing_priority(2, 23, 'no', 'no', 'no')
        3
    '''
    
    score = year
    
    if age >= 23:
        score = score + 1
        
    if off_campus == True:
        score = score + 1

    if acad_prob == True:
        score = score - 1

    if disc_prob == True:
        score = score - 3

    return score
    
def process_application(year):
    '''
    Determines and reports housing score based on user input when asked about their
    year in school, age, if they are a student teacher living off campus,
    if on academic probation, and if on disciplinary probation within
    academic year.

    >>> process_application(3)
        What is your age? (integers please): 23
        Are a student teacher living off campus? (yes or no): no
        Are you on academic probation? (yes or no): no
        Are you on disciplinary probation? (yes or no): no
        4
    '''
    
    age = int(input('What is your age? (integers please): '))
    off_campus = input('Are a student teacher living off campus? (yes or no): ')
    
    if off_campus == 'yes':
        off_campus = True
    elif off_campus == 'no':
        off_campus = False
    else:
        print('Invalid input. Please try again.')
        return
    
    acad_prob = input('Are you on academic probation? (yes or no): ')
    
    if acad_prob == 'yes':
        acad_prob = True
    elif acad_prob == 'no':
        acad_prob = False
    else:
        print('Invalid input. Please try again.')
        return
    
    disc_prob = input('Are you on disciplinary probation? (yes or no): ')
    
    if disc_prob == 'yes':
        disc_prob = True
    elif disc_prob == 'no':
        disc_prob = False
    else:
        print('Invalid input. Please try again.')
        return
                
    score = housing_priority(year, age, off_campus, acad_prob, disc_prob)

    return score

def report_priority(score):
    '''
    Auxillary function for housing_main().
    Prints housing points score.

    >>> report_priority(2)
        You have 2 housing point(s).
    '''
    
    print(f'You have {score} housing point(s).')

    return
    
def housing_main():
    '''
    Driver for housing priority program.
    Determines housing eligibility and points based on input and
    reports results to user.

    >>> housing_main()
        Welcome to the U Housing Information Center.
        Please respond to the following questions: 

        What year are you? (1 for 1st year, 2 for 2nd year, etc.): 3
        What is your age? (integers please): 22
        Are a student teacher living off campus? (yes or no): yes
        Are you on academic probation? (yes or no): no
        Are you on disciplinary probation? (yes or no): no
        You have 4 housing point(s).

    '''
    # set up
    print('Welcome to the University Housing Information Center.')
    print('Please respond to the following questions: ')
    print()
    
    # determine eligibility for housing
    year = int(input('What year are you? (1 for 1st year, 2 for 2nd year, etc.): '))
    if year >= 4:
        housing_eligible = is_eligible()
    else:
        housing_eligible = True
        
    # process application and report priority for eligible students
    if housing_eligible:
        priority = process_application(year)
        report_priority(priority)
    else:
        print('You are no longer eligible for student housing.')
 
    return
