# Mini-project #3
# input comes from buttons and an input field
# all output for the game printed in the console

import simplegui
import random
import math

# initialize global variables used in your code
number_range = 100
secret_number = 7

# helper function to start and restart the game
def new_game():
    # remove this when you add your code 
    global number_range
    global guess_number
    global secret_number
   
    secret_number = random.randrange(0, number_range)
    guess_number = math.ceil (math.log(number_range + 1, 2))
    print "New game. Range is from 0 to", number_range
    print "Number of remaining guesses is", guess_number, '\n'
    pass


# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global secret_number
    global guess_number
    global number_range
    number_range = 100
    new_game()

def range1000():
    # button that changes range to range [0,1000) and restarts
    global secret_number
    global guess_number
    global number_range
    number_range = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here
    global secret_number
    global guess_number
    guess_number -= 1
    guess = int(guess)
   
    print "Guess was", guess
    print "Number of remaining guesses is", math.floor(guess_number)
   
    if guess_number > 0:
        if guess > secret_number:
            print "Lower!"
        elif guess < secret_number:
            print "Higher!"
       
        elif guess == secret_number:
            print "Correct!\n"
            new_game()
    else:
       print "You ran out of guesses. The number was", secret_number, '\n'
       new_game()
    print ""

    
# create frame

f = simplegui.create_frame("Guess the number!",200,200)

f.add_button("Range is [0, 100]", range100, 200)
f.add_button("Range is [0, 1000]", range1000, 200)
f.add_input("Input your guess", input_guess, 200)
# register event handlers for control elements



# call new_game and start frame

new_game()

# always remember to check your completed program against the grading rubric
