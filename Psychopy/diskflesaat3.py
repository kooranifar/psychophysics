#setup
import random, math, psychopy.visual, psychopy.event, psychopy.core, psychopy.sound


#settings

display_resolution = [1366,768]
my_radius = 50                   # radius of inner circle
my_border_width = 1              # border width of the circle
path_radius = 300                # radius of the circular path of our circle
frame_duration = 0.016666

#preparing the frames

win =  psychopy.visual.Window(display_resolution, fullscr=True, units='pix', allowGUI=False)
my_text = psychopy.visual.TextStim(win, text='+', bold=True, height=36, wrapWidth=800, pos=(0,0))

backcircle_list =  []
forecircle_list  = []


for theta in range(360):        
    backcircle = psychopy.visual.Circle(win, radius=my_radius+my_border_width, pos=(math.cos(math.radians(theta))*path_radius, math.sin(math.radians(theta))*path_radius)) # draws the bigger  circle with the coordinates according to theta
    forecircle = psychopy.visual.Circle(win, radius=my_radius                , pos=(math.cos(math.radians(theta))*path_radius, math.sin(math.radians(theta))*path_radius)) # draws the smaller circle with the coordinates according to theta
    flash      = psychopy.visual.Circle(win, radius=my_radius                , pos=(math.cos(math.radians(theta))*path_radius, math.sin(math.radians(theta))*path_radius)) # draws the flash   circle with the coordinates according to theta

    backcircle.setFillColor((0,0,0)   , colorSpace='rgb255')     # sets the color of the bigger  circle's Fill
    backcircle.setLineColor((0,0,0)   , colorSpace='rgb255')     # sets the color of the bigger  circle's Border
    forecircle.setFillColor((127,127,127), colorSpace='rgb255')  # sets the color of the smaller circle's Fill
    forecircle.setLineColor((127,127,127), colorSpace='rgb255')  # sets the color of the smaller circle's Border
    flash.setFillColor((255,255,255), colorSpace='rgb255')       # sets the color of the flash   circle's Fill
    flash.setLineColor((255,255,255), colorSpace='rgb255')       # sets the color of the flash circle's Border

    
    backcircle_list.append(backcircle)

    
    if theta==0:
        forecircle_list.append(flash)     
    else:
        forecircle_list.append(forecircle)
    


theta=0
while not psychopy.event.getKeys():
        backcircle_list[theta%360].draw()
        forecircle_list[theta%360].draw()
        my_text.draw()
        win.flip()
        theta = theta + 2

