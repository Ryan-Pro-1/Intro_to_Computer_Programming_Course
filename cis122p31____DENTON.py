'''
CIS 122 Spring 2022 Project 3-1
Author(s): Ryan Denton
Credit: CIS 122 Resources
Description: Sun and Earth Visualization
'''

from turtle import*

def draw_sun_earth():
    '''draw sun and earth visualization
 
    >>> draw_sun_earth()
    [graphical visualization of sun and earth]
    ''' 
    # calculate ratio of sun and earth to use for the visualization 
    SUN_DIAMETER = 1392000
    EARTH_DIAMETER = 12756
 
    ratio = SUN_DIAMETER / EARTH_DIAMETER
    sun_diameter = ratio 
    earth_diameter = 1
    print(sun_diameter, earth_diameter)
 
    # adjust for a better visualization – ratio is maintained
    multiplier = 2
    sun_diameter = sun_diameter * multiplier
    earth_diameter = earth_diameter * multiplier

    draw_vis(sun_diameter, 'yellow')
    draw_vis(earth_diameter, 'blue')
 
    return

def draw_vis(r, c):
    '''Draw circle with radius 'r' and color 'c'

    >>>draw_vis(1,'red')
    [draws circle with radius 1 and fills with color of red.]
    '''
    color(c)
    begin_fill()
    circle(r)
    end_fill()
    return

def main():
    '''driver for sun-earth drawing'''
 
    # set turtle environment
    hideturtle()
    speed(0)
    penup()
    setpos(0, -250)
    pendown()
 
    # draw the sun and earth
    draw_sun_earth()
 
    return

