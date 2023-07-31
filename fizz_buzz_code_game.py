def fb(n):
  for i in range(1,n+1):
    m3 = (i%3) == 0
    m5 = (i%5) == 0
    
    if m3 and m5:
      print('fizzbuzz')
      
    elif m3:
      print('fizz')
      
    elif m5:
      print('buzz')
    
    else:
      print(i)
      
  print('game over')
    
  return
  
fb(15)
