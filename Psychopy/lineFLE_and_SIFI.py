#setup
import random, math, psychopy.visual, psychopy.event, psychopy.core, psychopy.sound


#settings

display_resolution = [1366,768]
needle_length = 200
flash_length  = 100
gap           = 10
my_width      = 4
frame_duration = 0.016666

#preparing the frames

win = psychopy.visual.Window(display_resolution, fullscr=True, units='pix', allowGUI=False)
beep      = psychopy.sound.Sound (value=3500, secs=0.016)
fixation1 = psychopy.visual.Line(win, start=(-370,0),   end=(-350,0), lineWidth=3)
fixation2 = psychopy.visual.Line(win, start=(-360,-10), end=(-360,10),lineWidth=3)


needle_list = []
flash_list  = []
sound_list  = []

for theta in range(360):        
    needle     = psychopy.visual.Line(win, start=(0,0),                                                                                                    end=(math.cos(math.radians(theta))*needle_length, math.sin(math.radians(theta))*needle_length), lineWidth=my_width) 
    flash      = psychopy.visual.Line(win, start=(math.cos(math.radians(theta))*(needle_length+gap), math.sin(math.radians(theta))*(needle_length+gap)), end=(math.cos(math.radians(theta))*(needle_length+gap+flash_length), math.sin(math.radians(theta))*(needle_length+gap+flash_length)), lineWidth=my_width)   
    fake_flash = psychopy.visual.Line(win, start=(math.cos(math.radians(theta))*(needle_length+gap), math.sin(math.radians(theta))*(needle_length+gap)), end=(math.cos(math.radians(theta))*(needle_length+gap+flash_length), math.sin(math.radians(theta))*(needle_length+gap+flash_length)), lineWidth=my_width)   
    

    fake_flash.setLineColor([127, 127, 127], colorSpace='rgb255')

    needle_list.append(needle)
    
    if theta==180:
        flash_list.append(flash)
    
    else:
        flash_list.append(fake_flash)

    if theta==178 or theta==182:
        sound_list.append(1)
    else:
        sound_list.append(0)
    

#needle_list[0].draw()
#flash_list[0].draw()
#clock = psychopy.core.Clock()
#wait_till = clock.getTime()
#for theta in xrange(359):
#    win.flip()
#    wait_till = wait_till + 0.016666
#    needle_list[theta+1].draw()
#    flash_list[theta+1].draw()
#    while clock.getTime()<wait_till:
#        psychopy.core.wait(0.001)
#    if sound_list[theta]==1:        
#        beep.play()
#    my_text.draw()
clock = psychopy.core.Clock()
while not psychopy.event.getKeys():
    for theta in range(360):
        needle_list[theta].draw()
        flash_list[theta].draw()
#        fixation1.draw()
#        fixation2.draw()
        win.flip()
        if sound_list[theta]==1:        
            beep.play()
            
print clock.getTime() 
#needle_list[180].draw()
#flash_list[180].draw()
#fixation1.draw()
#fixation2.draw()
#win.flip()
#psychopy.core.wait(5)
