'''
CIS 122 Spring 2022 Project 2-2
Author: Ryan Denton
Description: Python functions; minimum payment function
'''

def payment(balance):
  '''
  Gives the minimum payment due on the account (the greater of $10 or 2.1% of account balance).
  If this exceeds account balance, then the minimum payment is the balance.
  
  >>>payment(1000)
  The minimum payment due for a balance of $1000 is $21.0
  
  >>>payment(8)
  The minimum payment due for a balance of $8 is $8
  '''
  potential_min_payment1 = max(10, 0.021 * balance) 
  potential_min_payment2 = min(potential_min_payment1, balance) 
  actual_min_payment_due = round(potential_min_payment2, 2)
  print(f'The minimum payment due for a balance of ${balance} is ${actual_min_payment_due}')
  return
