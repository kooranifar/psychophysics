import random, psychopy.visual, psychopy.event
from psychopy import core

displayresolution = [1366, 768]
textwidth = 800
interval = 0.02
flag=0

win = psychopy.visual.Window(displayresolution, fullscr=True, units='pix', allowGUI=False)

mycircle = [0,0,0,0,0,0,0,0,0,0,0,0]
for x in range(6):
    for y in range(2):
        mycircle[y*6+x] = psychopy.visual.Circle(win, radius=20, pos=(-150+x*60,-30+y*60))
        mycircle[y*6+x].setFillColor([255,255,180], colorSpace='rgb255')
        mycircle[y*6+x].setLineColor([100,100,100], colorSpace='rgb255')
        mycircle[y*6+x].draw()
mytext1 = psychopy.visual.TextStim(win, text='Beta Movement', bold=True, height=30, wrapWidth=textwidth,pos=(0,displayresolution[1]/6*2))
mytext2 = psychopy.visual.TextStim(win, text='Press any key to exit', bold=True, height=30, wrapWidth=textwidth,pos=(0,-displayresolution[1]/6*2))
mytext1.draw()
mytext2.draw()
while flag != 1:
    for n in range (12):
        for j in range (12):
            mycircle[j].draw()
        if n<6:
            mycircle[n].setFillColor([255,255,0], colorSpace='rgb255')
            mycircle[n].setLineColor([0,0,0], colorSpace='rgb255')
            mycircle[n].draw()
        if n>=6:
            mycircle[17-n].setFillColor([255,255,0], colorSpace='rgb255')
            mycircle[17-n].setLineColor([0,0,0], colorSpace='rgb255')
            mycircle[17-n].draw()
        mytext1.draw()
        mytext2.draw()
        win.flip()
        core.wait(interval)
        if n<6:
            mycircle[n].setFillColor([255,255,180], colorSpace='rgb255')
            mycircle[n].setLineColor([100,100,100], colorSpace='rgb255')
        if n>=6:
            mycircle[17-n].setFillColor([255,255,180], colorSpace='rgb255')
            mycircle[17-n].setLineColor([100,100,100], colorSpace='rgb255')
        if psychopy.event.getKeys():
            flag=1
            break
