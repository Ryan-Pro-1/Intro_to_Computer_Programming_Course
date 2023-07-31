'''
CIS 122 Spring 2022 Project 4-1
Author(s): Ryan Denton
Credit: CIS 122 Resources
Description: Safe Lead algorithm
'''

def safe_lead(lead, possession, time):
  '''
  Algorithm to determine is lead is insurmountable depending on
  points team is ahead, if they have possession of the ball (True or False),
  and time (in seconds) left in the game.

  >>> safe_lead(7, True, 20)
  This is a safe lead.

  >>> safe_lead(7, False, 20)
  This lead is NOT safe!.
  '''
  lead = lead - 3
  
  if possession == True:
    lead = lead + 0.5
  else:
    lead = lead - 0.5
  
  lead = lead ** 2
  
  if lead > time:
    print('This is a safe lead.')
  else:
    print('This lead is NOT safe!')
    
  return

def main():
  '''
  Main driver for the Safe Lead algorithm.
  Asks the user for the point lead, possession status
  and time left in game to determine is the lead is 'safe'.
  '''
  lead = int(input('Enter point lead: '))
  
  possession = input('Do they have possession? (yes or no): ')

  #Determine the value of 'possession' based on the input
  if possession == 'yes':
    possession = True
  elif possession == 'no':
    possession = False
  else:
  #Add response for in case they input invalid response 
    print('Invalid possession status, please try again.')
    return
  
  time = int(input('Time left in game (seconds): '))
  
  safe_lead(lead, possession, time)
  
  return



