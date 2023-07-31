
from turtle import*

def poly(num_sides, side_len, pcolor):
    '''
    Draws a polygon with specified number of sides, side length, and color.

    >>>poly(4, 9, 'red')
    [Graphical representation of red square with side length 9]
    '''
    fillcolor(pcolor)
    begin_fill()
    for i in range(num_sides):
        fd(side_len)
        lt(360/num_sides)
    end_fill()
    
    return

def jump(x, y):
    '''aux function sets turtle position
    without leaving pen trail
    
    >>> jump(100, 100)
    [turtle positioned at 100, 100]
    '''
    
    penup()
    setposition(x, y)
    pendown()
    
    return

def bus():
    ''' Draws bus based on input specs'''

    jump(-200, 0)
    black_square_body()

    jump(-50, 0)
    black_square_body()

    jump(100, 0)
    black_square_body()

    jump(150, 0)
    black_square_body()

    jump(-150,-20)
    tire()

    jump(170,-20)
    tire()

    jump(-190, 75)
    horz_white_rectangle()

    jump(-190, 70)
    horz_white_rectangle()

    jump(-190, 145)
    horz_white_rectangle()

    jump(0, 75)
    vert_white_rectangle()

    jump(-75, 75)
    vert_white_rectangle()
    
    jump(-190, 75)
    vert_white_rectangle()
    
    jump(75, 75)
    vert_white_rectangle()
    
    jump(190, 75)
    vert_white_rectangle()
    
    return

def horz_white_rectangle():
    ''' Horizontal white rectangle of drawing'''
    
    color('white')
    fillcolor('white')
    setheading(360)
    begin_fill()
    fd(380)
    lt(90)
    fd(2)
    lt(90)
    fd(380)
    lt(90)
    fd(2)
    end_fill()

    return

def black_square_body():
    '''Black Square that makes body of bus'''
    
    fillcolor('black')
    begin_fill()
    poly(4,150,'black')
    end_fill()

    return

def tire():
    '''Draws tire of bus'''
    
    fillcolor('yellow')
    begin_fill()
    circle(35)
    end_fill()

    return

def vert_white_rectangle():
    ''' Draws vertical white rectangles'''
    color('white')
    fillcolor('white')
    setheading(360)
    begin_fill()
    fd(2)
    lt(90)
    fd(70)
    lt(90)
    fd(2)
    lt(70)
    fd(2)
    end_fill()

    return
    

def bus_main():
    '''driver for code to draw a house'''
    
    reset()
    title('Black & Yellow Bus')
    speed(0)
    hideturtle()
    
    bus()
    
    return
