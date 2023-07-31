'''
CIS 122 Spring 2022
Project 1-1: Hello, Python
Ryan Denton
Description: Intro to computational problem-solving: use Python 
numeric data types and operations to solve small problems.
'''



#1a - determine cost of buying two kinds of shirts.

cost_t = 20

ttl_shirts = 101

cost_yellow = cost_t - (cost_t* 0.5)

ttl_green = (ttl_shirts // 2) + (ttl_shirts % 2)

ttl_yellow = ttl_shirts - ttl_green

ttl_green_cost = ttl_green * cost_t

ttl_yellow_cost = ttl_yellow * cost_yellow

ttl_cost = ttl_yellow_cost + ttl_green_cost

print('The total cost is', ttl_cost)

#This code does indeed give us a total cost of $1520.00





#1b - finding the bug in problem 1a.


#here I will paste the code from 1a and make a comment on the bug's location and what should be different.


'''
cost_t = 20

ttl_shirts = 101

cost_yellow = cost_t - (cost_t* 0.5)

ttl_green = (ttl_shirts // 2) + (ttl_shirts % 2)   --->  ### HERE IS THE BUG, since 101 is not a even number, we should be buying 51 yellow shirts not 51 green shirts (as this code is doing).

###to fix this we need to remove the "+ (ttl_shirts % 2)" part from the line of code above.


ttl_yellow = ttl_shirts - ttl_green

ttl_green_cost = ttl_green * cost_t

ttl_yellow_cost = ttl_yellow * cost_yellow

ttl_cost = ttl_yellow_cost + ttl_green_cost

print('The total cost is', ttl_cost)
'''


#Here is the proper code after fixing the bug:

cost_t = 20

ttl_shirts = 101

cost_yellow = cost_t - (cost_t* 0.5)

ttl_green = (ttl_shirts // 2) 

ttl_yellow = ttl_shirts - ttl_green

ttl_green_cost = ttl_green * cost_t

ttl_yellow_cost = ttl_yellow * cost_yellow

ttl_cost = ttl_yellow_cost + ttl_green_cost

print('The total cost is', ttl_cost)

#The total cost is $1510.10






#2a - Color count of bag of skittles


num_orange = 7

num_green = num_orange * 3

num_purple = num_orange + num_green

num_red = round(num_purple/2)

num_yellow = round(100 - (num_green + num_orange + num_purple + num_red))


#Now let's print out the numbers of each color.

print('There are', num_orange, 'orange skittles.')

print('There are', num_green, 'green skittles.')

print('There are', num_purple, 'purple skittles.')

print('There are', num_red, 'red skittles.')

print('There are', num_yellow, 'yellow skittles.')







#2b - If instead had 6 orange to start, not 7, what line of code do we change?


num_orange = 6 #This is the line we would need to change. We would change 7 to 6.

num_green = num_orange * 3

num_purple = num_orange + num_green

num_red = round(num_purple/2)

num_yellow = round(100 - (num_green + num_orange + num_purple + num_red))


#Lets print these out to verify the results.

print('There are', num_orange, 'orange skittles.')

print('There are', num_green, 'green skittles.')

print('There are', num_purple, 'purple skittles.')

print('There are', num_red, 'red skittles.')

print('There are', num_yellow, 'yellow skittles.')


#Indeed they match up to the given values.






#3 - Confirm there are 525,600 minutes in a year

#create variables in terms of minutes

minute = 1

hour = minute*60

day = hour*24

year = day*365


print('There are', year, "minutes in a year.")


#This confirms the number in the song is correct.
