# Implementation of classic arcade game Pong

import simplegui
import random
import math

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left

def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [0,0]
    ball_vel = [0,0]
    ball_pos[0] = WIDTH/2
    ball_pos[1] = HEIGHT/2
    if direction:
        ball_vel[0] = random.randrange(2, 4)
    else:
        ball_vel[0] = -random.randrange(2, 4)
    ball_vel[1] = -random.randrange(1, 3)

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball(random.choice([True, False]))
    score1, score2 = 0,0
    paddle1_vel, paddle2_vel = 0,0
    paddle1_pos, paddle2_pos = HEIGHT/2, HEIGHT/2

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # Update ball position
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]  
    
    # draw ball
    c.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos > HEIGHT - HALF_PAD_HEIGHT:
        paddle1_pos = HEIGHT - HALF_PAD_HEIGHT
    elif paddle1_pos < HALF_PAD_HEIGHT:
        paddle1_pos = HALF_PAD_HEIGHT
    else:
        paddle1_pos += paddle1_vel

    if paddle2_pos > HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos = HEIGHT - HALF_PAD_HEIGHT
    elif paddle2_pos < HALF_PAD_HEIGHT:
        paddle2_pos = HALF_PAD_HEIGHT
    else:
        paddle2_pos += paddle2_vel
        
    # ball hitts paddles
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS:
        if (paddle1_pos+HALF_PAD_HEIGHT) >= ball_pos[1] >= (paddle1_pos-HALF_PAD_HEIGHT): #it hits the paddle, bounce
            ball_vel[0] = -ball_vel[0]*1.1
            ball_vel[1] *= 1.1
        else:
            score2 += 1
            spawn_ball(True)
    elif ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS:
        if (paddle2_pos+HALF_PAD_HEIGHT) >= ball_pos[1] >= (paddle2_pos-HALF_PAD_HEIGHT):#it hits the paddle, bounce
            ball_vel[0] = -ball_vel[0] 
            ball_vel[1] *= 1.1
        else:
            score1 += 1
            spawn_ball(False)
            
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]*1.1
    
    # draw paddles
    c.draw_line([HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT], [HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT], PAD_WIDTH, "White")
    c.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT], [WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT], PAD_WIDTH, "White")
    
    # draw scores
    c.draw_text(str(score1), [WIDTH / 2 - 70, 80], 60, "White")
    c.draw_text(str(score2), [WIDTH / 2 + 40, 80], 60, "White") 
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    accel = 3
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= accel
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel += accel
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel += accel
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= accel

def keyup(key):
    global paddle1_vel, paddle2_vel
    accel = 0
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = accel
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = accel
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel = accel
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel = accel

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 100)

# start frame
new_game()
frame.start()
