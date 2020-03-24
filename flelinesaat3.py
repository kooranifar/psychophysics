#setup
import random, math, psychopy.visual, psychopy.event, psychopy.core


#settings

display_resolution = [1366,768]
needle_length = 200
flash_length  = 100
gap           = 10
my_width      = 4
frame_duration = 0.016666

#preparing the frames

win = psychopy.visual.Window(display_resolution, fullscr=True, units='pix', allowGUI=False)
my_text = psychopy.visual.TextStim(win, text='Press any key to exit', bold=True, height=36, wrapWidth=800, pos=(0,-350))

needle_list = []
flash_list  = []
my_line = psychopy.visual.Line(win, start=(-1024,0), end=(1024,0), lineWidth=1)
my_line.setLineColor([255,0,0], colorSpace='rgb255')
for theta in range(360):        
    needle     = psychopy.visual.Line(win, start=(0,0),                                                                                                    end=(math.cos(math.radians(theta))*needle_length, math.sin(math.radians(theta))*needle_length), lineWidth=my_width) 
    flash      = psychopy.visual.Line(win, start=(math.cos(math.radians(theta))*(needle_length+gap), math.sin(math.radians(theta))*(needle_length+gap)), end=(math.cos(math.radians(theta))*(needle_length+gap+flash_length), math.sin(math.radians(theta))*(needle_length+gap+flash_length)), lineWidth=my_width)   
    fake_flash = psychopy.visual.Line(win, start=(math.cos(math.radians(theta))*(needle_length+gap), math.sin(math.radians(theta))*(needle_length+gap)), end=(math.cos(math.radians(theta))*(needle_length+gap+flash_length), math.sin(math.radians(theta))*(needle_length+gap+flash_length)), lineWidth=my_width)   
    
    fake_flash.setLineColor([128, 128, 128], colorSpace='rgb255')
 
    needle_list.append(needle)
    if theta == 0:
        flash_list.append(flash)
    else:
        flash_list.append(fake_flash)
    

clock = psychopy.core.Clock()
while not psychopy.event.getKeys():
    for theta in xrange(360):
        if theta == 0:
            my_line.draw()
        needle_list[theta].draw()
        flash_list[theta].draw()
        win.flip()
print clock.getTime() 