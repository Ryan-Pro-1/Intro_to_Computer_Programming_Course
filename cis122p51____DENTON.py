'''
Title: CIS 122 Spring 2022 Project 5-1 - Mars rover
Author: Ryan Denton
Credits: CIS 122 materials
'''

from turtle import *
import random

def rover_loc():
    '''
    Returns random integer between -275 and 275 for rover location.

    >>> rover_loc()
        137
    '''

    return random.randint(-275, 275)

def water_content():
    '''
    Returns random integer between 1 and 290 for the water content of
    location (in ppm).

    >>> water_content()
        73 [for example]
    '''

    return random.randint(1, 290)

def temperature():
    '''
    Returns random integer between -178 and 1 for temperature of
    location (degrees Fahenheit).

    >>> temperature()
        -67 [for example]
    '''

    return random.randint(-178, 1)

def collect_data():
    '''
    Determines rover location, moves rover there, marks position,
    shows path, collects water conent and temperature. Then prints results
    x-coordinate, y-coordinate, water content, and temperature in a row.

    >>> collect_data()
        250 	 -51 	 104 	 -176
    '''
    
    color('blue')
    pd()
    x = rover_loc()
    y = rover_loc()
    setpos(x, y)
    dot()

    w = water_content()
    t = temperature()

    print(x, '\t',
          y, '\t',
          w, '\t',
          t, '\t')

    return

def mars_explore(stops):
    '''
    Determines the number of stops the rover will make then calls collect_data()
    to extract that data.
    Prints the data gathered in columns.
    
    >>> mars_explore(5)
        169 	 218 	 281 	 -45 	
        -76 	 -213 	 72 	 -70 	
        4 	 -209 	 64 	 -109 	
        -128 	 -216 	 255 	 -118 	
        265 	 189 	 10 	 -119
    '''
    
    for i in range(stops):
        collect_data()
        
    return 

def mars_explore_setup():
    '''
    Set up printed and graphical output
    called from: mars_explore_main
    
    >>> mars_explore_setup()
        xpos     ypos    water    temp
    '''
    
    # print title line for printed output
    print('xpos', '\t',
            'ypos', '\t',
            'water', '\t', 
            'temp') 
    # set up graphical output
    reset()
    title('Mars Rover')
    speed('fastest')
    display_color = 'blue'
    pencolor(display_color)
    dot(10, display_color) # mark the rover's starting position
    
    return

def mars_explore_main():
    '''
    Main function for mars_explore.
    Prints location and data collected from 20 locations on Mars.

    >>> mars_explore_main()
    xpos 	 ypos 	 water 	 temp
    91 	         -225 	 19 	 -81 	
    -262 	 272 	 250 	 -59 	
    78 	         95 	 37 	 -121 	
    29 	         -252 	 75 	 -134 	
    123 	 124 	 196 	 -139 	
    270 	 198 	 17 	 -35 	
    11 	         212 	 231 	 -72 	
    208 	 -142 	 122 	 -107 	
    218 	 124 	 175 	 -41 	
    214 	 272 	 7 	 -118 	
    210 	 208 	 265 	 -62 	
    -211 	 159 	 282 	 -25 	
    -173 	 -55 	 249 	 -3 	
    168 	 109 	 233 	 -47 	
    -227 	 142 	 189 	 -60 	
    -208 	 -112 	 166 	 -23 	
    1 	         -215 	 120 	 -154 	
    258 	 -108 	 30 	 -178 	
    65 	         19 	 269 	 -7 	
    -163 	 -111 	 210 	 -176
    '''

    #set up printed and graphical environment
    mars_explore_setup()

    #explore mars
    mars_explore(20)

    return
