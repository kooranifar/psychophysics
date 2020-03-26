#setup
import random, math, psychopy.visual, psychopy.event, psychopy.core, psychopy.sound, psychopy.gui

test_type =  [1,1,2,1,2,3,1,2,1,1,2,1,3,2,3,1,3,2,3,3,2,1,3,3,1,3,2,2,2,3]

test_place = [66/6,42/6,18/6,84/6,84/6,84/6,18/6,18/6,18/6,84/6,66/6,66/6,84/6,18/6,18/6,42/6,66/6,18/6,42/6,84/6,42/6,84/6,66/6,84/6,84/6,42/6,84/6,42/6,42/6,84/6]

def prepare_the_sounds (testtype, place):
    
    beep_list = [0]*21
    
    if testtype==1:        
        return beep_list
    
    if testtype==2:
        beep_list[place] = 1
        return beep_list
    
    if testtype==3:
        beep_list[place-2] = 1
        beep_list[place+2] = 1
        return beep_list


def display_my_text (string):
    my_text = psychopy.visual.TextStim(win, text=string, bold=True, height=36, wrapWidth=800, pos=(0,0))
    my_text.draw()
    win.flip()
    answer = psychopy.event.waitKeys()
    answer = answer[0]
    return answer
   
def framemaker_type1and2 (index, flash_place):
    degrees=[]
    for i in range(21):
        degrees.append(i*6)
        
    for theta in degrees:        
        forecircle = psychopy.visual.Circle(win, radius=my_radius, pos=(math.cos(math.radians(theta))*path_radius, math.sin(math.radians(theta))*path_radius)) # draws the smaller circle with the coordinates according to theta
        flash      = psychopy.visual.Circle(win, radius=my_radius, pos=(math.cos(math.radians(theta))*path_radius, math.sin(math.radians(theta))*path_radius)) # draws the flash   circle with the coordinates according to theta
        
        forecircle.setFillColor((127,127,127), colorSpace='rgb255')  # sets the color of the smaller circle's Fill
        forecircle.setLineColor((127,127,127), colorSpace='rgb255')  # sets the color of the smaller circle's Border
        flash.setFillColor((255,255,255), colorSpace='rgb255')       # sets the color of the flash   circle's Fill
        flash.setLineColor((255,255,255), colorSpace='rgb255')       # sets the color of the flash circle's Border    
        
        if theta==flash_place*6-6 or theta==flash_place*6+6:
            forecircle_list.append(flash)     
        else:
            forecircle_list.append(forecircle)
    return forecircle_list

def framemaker_type3 (index, flash_place):
    degrees=[]
    for i in range(21):
        degrees.append(i*6)
        
    for theta in degrees:        
        forecircle = psychopy.visual.Circle(win, radius=my_radius, pos=(math.cos(math.radians(theta))*path_radius, math.sin(math.radians(theta))*path_radius)) # draws the smaller circle with the coordinates according to theta
        flash      = psychopy.visual.Circle(win, radius=my_radius, pos=(math.cos(math.radians(theta))*path_radius, math.sin(math.radians(theta))*path_radius)) # draws the flash   circle with the coordinates according to theta
    
        forecircle.setFillColor((127,127,127), colorSpace='rgb255')  # sets the color of the smaller circle's Fill
        forecircle.setLineColor((127,127,127), colorSpace='rgb255')  # sets the color of the smaller circle's Border
        flash.setFillColor((255,255,255), colorSpace='rgb255')       # sets the color of the flash   circle's Fill
        flash.setLineColor((255,255,255), colorSpace='rgb255')       # sets the color of the flash circle's Border    
        
        if theta==flash_place*6:
            forecircle_list.append(flash)     
        else:
            forecircle_list.append(forecircle)
    return forecircle_list


dialog = psychopy.gui.Dlg (title='Subject info')
dialog.addField (label='Subject label:')
dialog.show()
if dialog.OK:
    sub_label = dialog.data[0]
    

#settings

display_resolution = [1366,768]
my_radius = 50                   # radius of inner circle
my_border_width = 1              # border width of the circle
path_radius = 400                # radius of the circular path of our circle
frame_duration = 0.016666

#generating the frames

win      = psychopy.visual.Window(display_resolution, fullscr=True, units='pix', allowGUI=False)
beep     = psychopy.sound.Sound (value=3500, secs=0.007)
fixation = psychopy.visual.TextStim(win, text='+', bold=True, height=36, wrapWidth=800, pos=(0,0))


backcircle_list =  []
forecircle_list  = []
flash_list  =      []

degrees=[]
for i in range(21):
    degrees.append(i*6)


for theta in degrees:        
    backcircle = psychopy.visual.Circle(win, radius=my_radius+my_border_width, pos=(math.cos(math.radians(theta))*path_radius, math.sin(math.radians(theta))*path_radius)) # draws the bigger  circle with the coordinates according to theta
    backcircle.setFillColor((0,0,0), colorSpace='rgb255')
    backcircle.setLineColor((0,0,0), colorSpace='rgb255')
    backcircle_list.append(backcircle)
    
display_my_text('You see 2 flashesh in each trial. After the presentation of each trial, answer to these questions :\n\n1- Where was the 1st flash (Before the ring/After the ring/Fitted the ring)?\n\n2- Where was the 1st flash (Before the ring/After the ring/Fitted the ring)?')
display_my_text('Try to be accurate!')

initial_backcircle = psychopy.visual.Circle(win, radius=my_radius+my_border_width, pos=(math.cos(math.radians(0))*path_radius, math.sin(math.radians(0))*path_radius))
initial_backcircle.setLineColor((0,0,0), colorSpace='rgb255')

file_name = 'sub_'+sub_label+'_data.txt'
my_file = open (file_name, 'w')
my_file.write('Trial number\tTrial type\tFirst position\tSecond position\n')

for i in range (30):
    my_file.write('{0}\t{1}\t'.format(i+1, test_type[i]-1))

    if test_type[i]==1:
        this_trial_frames = framemaker_type1and2(i, test_place[i])
        
    if test_type[i]==2:
        this_trial_frames = framemaker_type1and2(i, test_place[i])
        
    if test_type[i]==3:
        this_trial_frames = framemaker_type3(i)
        
    this_trial_sounds = prepare_the_sounds(test_type[i], test_place[i])
    
    initial_backcircle.draw()
    fixation.draw()
    win.flip()
    psychopy.event.waitKeys()
    
    for j in range (21):
        
        backcircle_list[j].draw()
        this_trial_frames[j].draw()
        fixation.draw()
        win.flip()
            
        if this_trial_sounds[j]==1:
            beep.play()
            
    psychopy.core.wait(1)
    answers = []
    for i in range(2):
        ans = display_my_text('Where was flash no.{0}?(b/f/a)'.format(i+1))
        ans = ans[0]
        my_file.write('{0}\t'.format(ans))
        
    my_file.write('\n')    
my_file.close()