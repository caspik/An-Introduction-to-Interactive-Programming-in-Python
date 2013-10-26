# template for "Stopwatch: The Game"
import simplegui
# define global variables


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    pass
    
# define event handlers for buttons; "Start", "Stop", "Reset"


# define event handler for timer with 0.1 sec interval


# define draw handler
def draw(canvas):
    canvas.draw_text("Hi!",[100,100],20,"Red")
    
# create frame
frame = simplegui.create_frame("My frame",300,300)

# register event handlers
frame.set_draw_handler(draw)

# start frame
frame.start()
