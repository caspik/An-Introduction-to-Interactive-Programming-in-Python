# code for "Stopwatch: The Game"
import simplegui
# define global variables
counter = 0
time = 0
tries = 0
wins = 0
last_stop = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global counter
    a = counter // 600
    b = ((counter//100)%6)
    c = (counter//10)%10
    d = counter%10
    return str(a) + ":" + str(b) + str(c) + "." + str(d)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    timer.start()
    
def stop_handler():
    global tries
    global wins
    global last_stop
    timer.stop()
    if counter != last_stop:
        tries += 1
        last_stop = counter
        if counter%10 == 0:
                wins += 1
    update_score() 
    
def reset_handler():
    global counter
    global tries
    global wins
    global last_stop
    timer.stop()
    counter = 0
    wins = 0
    tries = 0
    last_stop = 0

# define event handler for timer with 0.1 sec interval
def tick():
    global counter
    counter += 1
    return counter

# define draw handler
def draw(canvas):
    canvas.draw_text(format(time), (30, 90), 40, "Red")
    canvas.draw_text(update_score(), (110, 20), 25, "White")
    
def update_score():
    global tries
    global wins
    return str(wins) + "/" + str(tries)
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game",150,150)

# create buttons
timer = simplegui.create_timer(100, tick)
frame.set_draw_handler(draw)
start_button = frame.add_button('Start', start_handler, 50)
stop_button = frame.add_button('Stop', stop_handler, 50)
reset_button = frame.add_button('Reset', reset_handler, 50)

# start frame
frame.start()
