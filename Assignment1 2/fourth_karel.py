from stanfordkarel import *

"""
For this problem, there
are 8 colored squares
and 8 beepers on the map.
Your job is to move the
beepers so that there is one
beeper on each colored square.
Try to do this with as few
lines of code as possible.
You may use any of the following
functions:

turn_left()
move()
pick_beeper()
put_beeper()
"""

def main():
    move_four()
    turn_left()
    move()
    move()
    pick_three_beeper()
    move_four()
    move()
    pick_two_beeper()
    move()
    turn_left()
    move()
    move()
    pick_two_beeper()
    turn_around()
    move_four()
    put_beeper()
    move()
    put_beeper()
    move()
    turn_right()
    move_three()
    pick_beeper()
    move()
    move()
    put_beeper()
    move()
    put_beeper()
    turn_right()
    move()
    put_beeper()
    turn_right()
    move()
    put_beeper()
    move_four()
    put_beeper()
    turn_left()
    move()
    put_beeper()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def move_three():
    move()
    move()
    move()
    
def move_four():
    move()
    move()
    move()
    move()
    
def turn_around():
    turn_left()
    turn_left()
    
def pick_three_beeper():
    pick_beeper()
    pick_beeper()
    pick_beeper()
    
def pick_two_beeper():
    pick_beeper()
    pick_beeper()
    
    """Karel code goes here!"""


if __name__ == "__main__":
    run_karel_program("fourth_world")
