#setup
import random, math, psychopy.visual, psychopy.event, psychopy.core


#settings

display_resolution = [1366,768]  
my_radius = 40                   # radius of inner circle
my_border_width = 5              # border width of the circle
path_radius = 200                # radius of the circular path of our circle
frame_duration = 0.016666        # refresh rate

#preparing the frames

win = psychopy.visual.Window(display_resolution, fullscr=True, units='pix', allowGUI=False) #creating a window


backcircle_list = [] # here's the array where I store the bigger  circle objects
forecircle_list = [] # here's the array where I store the smaller circle objects



for theta in range(360):        
    backcircle = psychopy.visual.Circle(win, radius=my_radius+my_border_width, pos=(math.cos(math.radians(theta))*path_radius, math.sin(math.radians(theta))*path_radius)) # draws the bigger  circle with the coordinates according to theta
    forecircle = psychopy.visual.Circle(win, radius=my_radius                , pos=(math.cos(math.radians(theta))*path_radius, math.sin(math.radians(theta))*path_radius)) # draws the smaller circle with the coordinates according to theta
    flash      = psychopy.visual.Circle(win, radius=my_radius                , pos=(math.cos(math.radians(theta))*path_radius, math.sin(math.radians(theta))*path_radius)) # draws the flash   circle with the coordinates according to theta
    
    backcircle.setFillColor((0,0,0)   , colorSpace='rgb255') # sets the color of the bigger  circle's Fill
    backcircle.setLineColor((0,0,0)   , colorSpace='rgb255') # sets the color of the bigger  circle's Border
    forecircle.setFillColor((127,127,127), colorSpace='rgb255')  # sets the color of the smaller circle's Fill
    forecircle.setLineColor((127,127,127), colorSpace='rgb255')  # sets the color of the smaller circle's Border
    flash.setFillColor((255,255,255), colorSpace='rgb255')       # sets the color of the flash   circle's Fill
    flash.setLineColor((255,255,255), colorSpace='rgb255')       # sets the color of the flash circle's Border
    
    backcircle_list.append(backcircle)     # append command adds what's in it's parentheses to the list mentioned before it. so here we are adding the bigger circle object to the list we wanted to store bigger circles
    if random.randint(1,50)==28:          # here we are considering a 2% chance for showing the flash for each frame.
        forecircle_list.append(flash)      # if the chance occured then we should store a yellow circle as smaller circle
    else:
        forecircle_list.append(forecircle) # stores normal small circle
        

#execute the trial

my_clock = psychopy.core.Clock()  

degrees = range(60)            # setting
for i in range(60):           # the step of
    degrees[i] = degrees[i]*6 # degrees

for ali in range(3):
    for theta in degrees:           
        backcircle_list[theta].draw() 
        forecircle_list[theta].draw()  
        win.flip()                    
print my_clock.getTime()
