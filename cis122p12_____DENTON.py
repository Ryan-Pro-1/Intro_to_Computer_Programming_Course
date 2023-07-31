'''
CIS 122 Spring 2022
Project 1-2: Hello, Python continued
Ryan Denton
Description: Intro to computational problem-solving: use Python 
numeric data types and operations to solve small problems.
'''


#Bringing watermelons to the family reunion







# Initialize variables with values

num_ppl = 100

num_kids = 40

num_adults = 100 - num_kids

watermelon = 10  #gives average # of slices





# Calculate total number of watermelon slices


wat_slices_adults = 2*num_adults

wat_slices_kids = 3 * num_kids

wat_slices_b4_extra = wat_slices_adults + wat_slices_kids  #slices before extra 10%




# Add extra amount and display number of slices


add_extra_wat = wat_slices_b4_extra * 1.1  #extra 10% added


total_wat_slices = round(extra_wat)  #Total slices


print("We will need", total_wat_slices, 'slices of watermelon.')





# Calculate number of watermelons needed (this may be a float)


total_wat_whole = total_wat_slices / watermelon  #find how many whole melons needed





# Round the number of watermelons


total_wat_whole_integer = round(total_wat_whole)  #Round the number(assuming can't buy fractions of melons)




# Report total number of watermelons to buy


print('We will need',total_wat_whole_integer, 'whole watermelons.' )
