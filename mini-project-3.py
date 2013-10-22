# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# initialize global variables used in your code
num_range = 100


# helper function to start and restart the game
def new_game():
    # remove this when you add your code    
    pass


# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    
    # remove this when you add your code    
    pass

def range1000():
    # button that changes range to range [0,1000) and restarts
    
    # remove this when you add your code    
    pass
    
def input_guess(guess):
    # main game logic goes here	
    
    # remove this when you add your code
    pass

    
# create frame

f = simplegui.create_frame("Guess the number!",200,200)

f.add_button("Range is [0, 100]", range100, 200)
f.add_button("Range is [0, 1000]", range1000, 200)
f.add_input("Input your guess", input_guess, 200)
# register event handlers for control elements



# call new_game and start frame

new_game()

# always remember to check your completed program against the grading rubric
