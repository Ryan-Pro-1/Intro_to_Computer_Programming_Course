'''
Title: CIS 122 Spring 2022 Project 9-1 - Mars Data Analysis
Author: Ryan Denton
Credits: CIS 122 materials
'''

from turtle import *
import statistics
import random

def rover_loc():
    '''
    Returns random integer between -275 and 275 for rover location.

    >>> rover_loc()
    137

    >>> rover_loc()
    1
    '''

    return random.randint(-275, 275)

def water_content():
    '''
    Returns random integer between 1 and 290 for the water content of
    location (in ppm).

    >>> water_content()
    73
    
    >>> water_content()
    134
    '''

    return random.randint(1, 290)

def temperature():
    '''
    Returns random integer between -178 and 1 for temperature of
    location (degrees Farenheit).

    >>> temperature()
    -67

    >>> temperature()
    -123
    '''

    return random.randint(-178, 1)

def collect_data():
    '''
    Determines rover location, moves rover there, marks position,
    shows path, collects water conent and temperature. Then prints results
    x-coordinate, y-coordinate, water content, and temperature in a row.
    It also creates a tuple containing just the water content and temperature and
    returns that tuple.

    >>> collect_data()
    -233    -145    155     -67 	
    (155, -67)

    >>> collect_data()
    129     83 	    144     -100 	
    (144, -100)
    '''
    
    color('blue')
    pd()
    x = rover_loc()
    y = rover_loc()
    setpos(x, y)
    dot()

    w = water_content()
    t = temperature()
    c = (w, t)

    print(x, '\t',
          y, '\t',
          w, '\t',
          t, '\t')
    
    return c

def analyze_data(li):
    '''
    Analyzing the parameter 'li', finds the mean, mode (if applicable),
    and the range, in terms of the minimum to the maximum value. It then
    returns these values.

    >>> analyze_data([100, 100, 200])
    (133.33, [100], (100, 200))
    
    >>> analyze_data([-150, 0])
    (-75, [], (-150, 0))
    '''

    mean = round(statistics.mean(li), 2)
    mode = statistics.multimode(li)
    if len(mode) == len(li):
        mode = []
    range = (min(li),  max(li))
    
    return (mean, mode, range)

def mars_report(dtype, dmean, dmode, drange):
    '''
    Prints out the data type (typed in as a string)
    as well as the mean, mode, and range for the data.

    >>> mars_report('Water Content', 131.35, 93, (18, 290))
    Water Content Data Analysis
    range:  18 to 290
    mean:   131.35
    mode:   93

    >>> mars_report('Temperature', -84.7, [], (-175, -3))
    Temperature Data Analysis
    range:  -175 to -3
    mean:   -84.7
    mode:   No value occurred more than once.
    '''

    print(f'{dtype} Data Analysis')
    print(f'range: \t{drange[0]} to {drange[1]}')
    print(f'mean: \t{dmean}')

    if dmode == []:
        print(f'mode: \tNo value occurred more than once.')
    else:
        print(f'mode: \t{dmode}')

    return

def mars_explore(stops):
    '''
    Determines the number of stops the rover will make then calls collect_data()
    to extract that data, runs 'mars_report' to calculate the mean, mode, range
    and then prints the data gathered in columns as well as the statistics of both
    the water content data and temperature data.
    
    >>> mars_explore(3)
    103     -100    287     -172 	
    21 	    45 	    235     -174 	
    42 	    123     148     -62 	
    Water Content Data Analysis
    range:  148 to 287
    mean:   223.33
    mode:   No value occurred more than once.
    Temperature Data Analysis
    range:  -174 to -62
    mean:   -136
    mode:   No value occurred more than once.

    >>> mars_explore(5)
    -49     18 	    206     -108 	
    109     -83     261     -34 	
    119     -140    93 	    -174 	
    144     25 	    215     -80 	
    113     -57     215     -105 	
    Water Content Data Analysis
    range:  93 to 261
    mean:   198
    mode:   [215]
    Temperature Data Analysis
    range:  -174 to -34
    mean:   -100.2
    mode:   No value occurred more than once.
    '''

    water_data = []
    temp_data = []
    
    for i in range(stops):
        cd = collect_data()
        water_data.append(cd[0])
        temp_data.append(cd[1])

    w = analyze_data(water_data)
    t= analyze_data(temp_data)

    mars_report('Water Content', w[0], w[1], w[2])
    mars_report('Temperature', t[0], t[1], t[2])
        
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
    Prints location and data collected from 20 locations on Mars as well
    as the statistics on the water content and the temperature gathered
    from all locations.

    >>>mars_explore_main()
    xpos 	 ypos 	 water 	 temp
    -44 	 88 	 114 	 -63 	
    211 	 136 	 187 	 -49 	
    -32 	 -115 	 95 	 -71 	
    271 	 -118 	 63 	 -66 	
    190 	 23 	 217 	 -37 	
    132 	 -255 	 9 	 -28 	
    69 	         -47 	 187 	 -138 	
    -265 	 -164 	 140 	 -15 	
    -94 	 -79 	 149 	 -132 	
    -82 	 217 	 94 	 -44 	
    234 	 -107 	 272 	 -159 	
    230 	 -58 	 270 	 -83 	
    74 	         30 	 72 	 -102 	
    72 	         -173 	 52 	 -85 	
    -132 	 -153 	 137 	 -107 	
    231 	 -65 	 138 	 -125 	
    5 	         256 	 273 	 -122 	
    155 	 112 	 8 	 -64 	
    -34 	 21 	 290 	 -169 	
    -261 	 192 	 26 	 -24 	
    Water Content Data Analysis
    range:  8 to 290
    mean:   139.65
    mode:   [187]
    Temperature Data Analysis
    range:  -169 to -15
    mean:   -84.15
    mode:   No value occurred more than once.
    '''

    #set up printed and graphical environment
    mars_explore_setup()

    #explore mars
    mars_explore(20)

    return
