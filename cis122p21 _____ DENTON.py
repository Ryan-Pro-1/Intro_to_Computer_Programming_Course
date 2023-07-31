'''
CIS 122 Spring 2022
Project	2-1: Form	and	Function,	Part	1 (Bridges)
Ryan Denton
Description: Python functions; transportation problems.
'''

def max_trans1(a, b, c):
  '''
  Determines maximum weight of a truck allowed on this route.
  
  >>>max_trans1(1, 2, 3)
  The max weight is: 1
  
  >>>max_trans1(9, 6, 3)
  The max weight is: 3
  '''
  max_weight_route1 = min(a, b, c)
  print('The max weight is:', + max_weight_route1)
  return

def max_trans2(a, b, c, d, e):
  '''
  Determines maximum weight of a truck allowed between the two possible routes,
  either route 1: a, b, c or route 2: d, e.
  
  >>>max_trans2(1, 2, 3, 4, 5)
  The max weight is: 4
  
  >>>max_trans2(222, 110, 411, 54, 73)
  The max weight is: 110
  '''
  max_weight_route1 = min(a, b, c)
  max_weight_route2 = min(d, e)
  print('The max weight is:', + max(max_weight_route1, max_weight_route2)) 
  return





