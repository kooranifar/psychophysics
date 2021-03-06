import random, psychopy.visual, psychopy.event
from psychopy import core

displayresolution = [1366, 768]
textwidth = 800

win = psychopy.visual.Window(displayresolution, fullscr=True, units='pix', allowGUI=False)

mytext = psychopy.visual.TextStim(win, text='In this experiment you are required to say the color of the word, not what the word says.\n\nAs soon as the words appear on your screen, read the list as fast as you can.\n\nWhen you have finished, press any key. The time it took you to read all of the words will be shown.\n\nPress any key to go to the first test', font='Courier New', bold=True, height=30, wrapWidth=textwidth)
mytext.draw()
win.flip()
psychopy.event.waitKeys()
mytext = psychopy.visual.TextStim(win, text='Get Ready...', font='Courier New', bold=True, height=30, wrapWidth=textwidth)
mytext.draw()
win.flip()
core.wait(2.0)

mytext = psychopy.visual.TextStim(win, text='RED', font='Courier New', bold=True, height=30, wrapWidth=textwidth, pos=(displayresolution[0]/6*-2, displayresolution[1]/6*2), color=(255,0,0), colorSpace='rgb255')
mytext.draw()
mytext = psychopy.visual.TextStim(win, text='GREEN', font='Courier New', bold=True, height=30, wrapWidth=textwidth, pos=(displayresolution[0]/6*-1, displayresolution[1]/6*2), color=(0,255,0), colorSpace='rgb255')
mytext.draw()
mytext = psychopy.visual.TextStim(win, text='BLUE', font='Courier New', bold=True, height=30, wrapWidth=textwidth, pos=(displayresolution[0]/6*0, displayresolution[1]/6*2), color=(0,0,255), colorSpace='rgb255')
mytext.draw()
mytext = psychopy.visual.TextStim(win, text='YELLOW', font='Courier New', bold=True, height=30, wrapWidth=textwidth, pos=(displayresolution[0]/6*1, displayresolution[1]/6*2), color=(255,255,0), colorSpace='rgb255')
mytext.draw()
mytext = psychopy.visual.TextStim(win, text='PINK', font='Courier New', bold=True, height=30, wrapWidth=textwidth, pos=(displayresolution[0]/6*2, displayresolution[1]/6*2), color=(255,0,255), colorSpace='rgb255')
mytext.draw()

mytext = psychopy.visual.TextStim(win, text='ORANGE', font='Courier New', bold=True, height=30, wrapWidth=textwidth, pos=(displayresolution[0]/6*-2, displayresolution[1]/6*1), color=(255,128,0), colorSpace='rgb255')
mytext.draw()
mytext = psychopy.visual.TextStim(win, text='BLUE', font='Courier New', bold=True, height=30, wrapWidth=textwidth, pos=(displayresolution[0]/6*-1, displayresolution[1]/6*1), color=(0,0,255), colorSpace='rgb255')
mytext.draw()
mytext = psychopy.visual.TextStim(win, text='GREEN', font='Courier New', bold=True, height=30, wrapWidth=textwidth, pos=(displayresolution[0]/6*0, displayresolution[1]/6*1), color=(0,255,0), colorSpace='rgb255')
mytext.draw()
mytext = psychopy.visual.TextStim(win, text='BLUE', font='Courier New', bold=True, height=30, wrapWidth=textwidth, pos=(displayresolution[0]/6*1, displayresolution[1]/6*1), color=(0,0,255), colorSpace='rgb255')
mytext.draw()
mytext = psychopy.visual.TextStim(win, text='WHITE', font='Courier New', bold=True, height=30, wrapWidth=textwidth, pos=(displayresolution[0]/6*2, displayresolution[1]/6*1), color=(255,255,255), colorSpace='rgb255')
mytext.draw()

mytext = psychopy.visual.TextStim(win, text='GREEN', font='Courier New', bold=True, height=30, wrapWidth=textwidth, pos=(displayresolution[0]/6*-2, displayresolution[1]/6*0), color=(0,255,0), colorSpace='rgb255')
mytext.draw()
mytext = psychopy.visual.TextStim(win, text='YELLOW', font='Courier New', bold=True, height=30, wrapWidth=textwidth, pos=(displayresolution[0]/6*-1, displayresolution[1]/6*0), color=(255,255,0), colorSpace='rgb255')
mytext.draw()
mytext = psychopy.visual.TextStim(win, text='ORANGE', font='Courier New', bold=True, height=30, wrapWidth=textwidth, pos=(displayresolution[0]/6*0, displayresolution[1]/6*0), color=(255,128,0), colorSpace='rgb255')
mytext.draw()
mytext = psychopy.visual.TextStim(win, text='BLUE', font='Courier New', bold=True, height=30, wrapWidth=textwidth, pos=(displayresolution[0]/6*1, displayresolution[1]/6*0), color=(0,0,255), colorSpace='rgb255')
mytext.draw()
mytext = psychopy.visual.TextStim(win, text='WHITE', font='Courier New', bold=True, height=30, wrapWidth=textwidth, pos=(displayresolution[0]/6*2, displayresolution[1]/6*0), color=(255,255,255), colorSpace='rgb255')
mytext.draw()

mytext = psychopy.visual.TextStim(win, text='BROWN', font='Courier New', bold=True, height=30, wrapWidth=textwidth, pos=(displayresolution[0]/6*-2, displayresolution[1]/6*-1), color=(82,51,20), colorSpace='rgb255')
mytext.draw()
mytext = psychopy.visual.TextStim(win, text='RED', font='Courier New', bold=True, height=30, wrapWidth=textwidth, pos=(displayresolution[0]/6*-1, displayresolution[1]/6*-1), color=(255,0,0), colorSpace='rgb255')
mytext.draw()
mytext = psychopy.visual.TextStim(win, text='BLUE', font='Courier New', bold=True, height=30, wrapWidth=textwidth, pos=(displayresolution[0]/6*0, displayresolution[1]/6*-1), color=(0,0,255), colorSpace='rgb255')
mytext.draw()
mytext = psychopy.visual.TextStim(win, text='YELLOW', font='Courier New', bold=True, height=30, wrapWidth=textwidth, pos=(displayresolution[0]/6*1, displayresolution[1]/6*-1), color=(255,255,0), colorSpace='rgb255')
mytext.draw()
mytext = psychopy.visual.TextStim(win, text='GREEN', font='Courier New', bold=True, height=30, wrapWidth=textwidth, pos=(displayresolution[0]/6*2, displayresolution[1]/6*-1), color=(0,255,0), colorSpace='rgb255')
mytext.draw()

mytext = psychopy.visual.TextStim(win, text='PINK', font='Courier New', bold=True, height=30, wrapWidth=textwidth, pos=(displayresolution[0]/6*-2, displayresolution[1]/6*-2), color=(255,0,255), colorSpace='rgb255')
mytext.draw()
mytext = psychopy.visual.TextStim(win, text='YELLOW', font='Courier New', bold=True, height=30, wrapWidth=textwidth, pos=(displayresolution[0]/6*-1, displayresolution[1]/6*-2), color=(255,255,0), colorSpace='rgb255')
mytext.draw()
mytext = psychopy.visual.TextStim(win, text='GREEN', font='Courier New', bold=True, height=30, wrapWidth=textwidth, pos=(displayresolution[0]/6*0, displayresolution[1]/6*-2), color=(0,255,0), colorSpace='rgb255')
mytext.draw()
mytext = psychopy.visual.TextStim(win, text='BLUE', font='Courier New', bold=True, height=30, wrapWidth=textwidth, pos=(displayresolution[0]/6*1, displayresolution[1]/6*-2), color=(0,0,255), colorSpace='rgb255')
mytext.draw()
mytext = psychopy.visual.TextStim(win, text='RED', font='Courier New', bold=True, height=30, wrapWidth=textwidth, pos=(displayresolution[0]/6*2, displayresolution[1]/6*-2), color=(255,0,0), colorSpace='rgb255')
mytext.draw()

win.flip()
clock = core.Clock()
psychopy.event.waitKeys()
mystring = 'It took you {0} seconds. Write down this number. Press any key to start the second test'.format(round(clock.getTime(),2))
mytext = psychopy.visual.TextStim(win, text=mystring, font='Courier New', bold=True, height=30, wrapWidth=textwidth)
mytext.draw()
win.flip()
psychopy.event.waitKeys()
mytext = psychopy.visual.TextStim(win, text='Get Ready...', font='Courier New', bold=True, height=30, wrapWidth=textwidth)
mytext.draw()
win.flip()
core.wait(2.0)

mytext = psychopy.visual.TextStim(win, text='RED', font='Courier New', bold=True, height=30, wrapWidth=textwidth, pos=(displayresolution[0]/6*-2, displayresolution[1]/6*2), color=(0,255,0), colorSpace='rgb255')
mytext.draw()
mytext = psychopy.visual.TextStim(win, text='GREEN', font='Courier New', bold=True, height=30, wrapWidth=textwidth, pos=(displayresolution[0]/6*-1, displayresolution[1]/6*2), color=(255,255,0), colorSpace='rgb255')
mytext.draw()
mytext = psychopy.visual.TextStim(win, text='BLUE', font='Courier New', bold=True, height=30, wrapWidth=textwidth, pos=(displayresolution[0]/6*0, displayresolution[1]/6*2), color=(255,255,255), colorSpace='rgb255')
mytext.draw()
mytext = psychopy.visual.TextStim(win, text='YELLOW', font='Courier New', bold=True, height=30, wrapWidth=textwidth, pos=(displayresolution[0]/6*1, displayresolution[1]/6*2), color=(255,0,255), colorSpace='rgb255')
mytext.draw()
mytext = psychopy.visual.TextStim(win, text='PINK', font='Courier New', bold=True, height=30, wrapWidth=textwidth, pos=(displayresolution[0]/6*2, displayresolution[1]/6*2), color=(255,128,0), colorSpace='rgb255')
mytext.draw()

mytext = psychopy.visual.TextStim(win, text='ORANGE', font='Courier New', bold=True, height=30, wrapWidth=textwidth, pos=(displayresolution[0]/6*-2, displayresolution[1]/6*1), color=(0,0,255), colorSpace='rgb255')
mytext.draw()
mytext = psychopy.visual.TextStim(win, text='BLUE', font='Courier New', bold=True, height=30, wrapWidth=textwidth, pos=(displayresolution[0]/6*-1, displayresolution[1]/6*1), color=(255,0,0), colorSpace='rgb255')
mytext.draw()
mytext = psychopy.visual.TextStim(win, text='GREEN', font='Courier New', bold=True, height=30, wrapWidth=textwidth, pos=(displayresolution[0]/6*0, displayresolution[1]/6*1), color=(255,255,0), colorSpace='rgb255')
mytext.draw()
mytext = psychopy.visual.TextStim(win, text='BLUE', font='Courier New', bold=True, height=30, wrapWidth=textwidth, pos=(displayresolution[0]/6*1, displayresolution[1]/6*1), color=(0,255,0), colorSpace='rgb255')
mytext.draw()
mytext = psychopy.visual.TextStim(win, text='WHITE', font='Courier New', bold=True, height=30, wrapWidth=textwidth, pos=(displayresolution[0]/6*2, displayresolution[1]/6*1), color=(0,0,255), colorSpace='rgb255')
mytext.draw()

mytext = psychopy.visual.TextStim(win, text='GREEN', font='Courier New', bold=True, height=30, wrapWidth=textwidth, pos=(displayresolution[0]/6*-2, displayresolution[1]/6*0), color=(255,0,0), colorSpace='rgb255')
mytext.draw()
mytext = psychopy.visual.TextStim(win, text='YELLOW', font='Courier New', bold=True, height=30, wrapWidth=textwidth, pos=(displayresolution[0]/6*-1, displayresolution[1]/6*0), color=(0,0,255), colorSpace='rgb255')
mytext.draw()
mytext = psychopy.visual.TextStim(win, text='ORANGE', font='Courier New', bold=True, height=30, wrapWidth=textwidth, pos=(displayresolution[0]/6*0, displayresolution[1]/6*0), color=(0,255,0), colorSpace='rgb255')
mytext.draw()
mytext = psychopy.visual.TextStim(win, text='BLUE', font='Courier New', bold=True, height=30, wrapWidth=textwidth, pos=(displayresolution[0]/6*1, displayresolution[1]/6*0), color=(255,0,0), colorSpace='rgb255')
mytext.draw()
mytext = psychopy.visual.TextStim(win, text='WHITE', font='Courier New', bold=True, height=30, wrapWidth=textwidth, pos=(displayresolution[0]/6*2, displayresolution[1]/6*0), color=(255,0,255), colorSpace='rgb255')
mytext.draw()

mytext = psychopy.visual.TextStim(win, text='BROWN', font='Courier New', bold=True, height=30, wrapWidth=textwidth, pos=(displayresolution[0]/6*-2, displayresolution[1]/6*-1), color=(0,0,255), colorSpace='rgb255')
mytext.draw()
mytext = psychopy.visual.TextStim(win, text='RED', font='Courier New', bold=True, height=30, wrapWidth=textwidth, pos=(displayresolution[0]/6*-1, displayresolution[1]/6*-1), color=(255,255,0), colorSpace='rgb255')
mytext.draw()
mytext = psychopy.visual.TextStim(win, text='BLUE', font='Courier New', bold=True, height=30, wrapWidth=textwidth, pos=(displayresolution[0]/6*0, displayresolution[1]/6*-1), color=(255,0,255), colorSpace='rgb255')
mytext.draw()
mytext = psychopy.visual.TextStim(win, text='YELLOW', font='Courier New', bold=True, height=30, wrapWidth=textwidth, pos=(displayresolution[0]/6*1, displayresolution[1]/6*-1), color=(0,255,0), colorSpace='rgb255')
mytext.draw()
mytext = psychopy.visual.TextStim(win, text='GREEN', font='Courier New', bold=True, height=30, wrapWidth=textwidth, pos=(displayresolution[0]/6*2, displayresolution[1]/6*-1), color=(255,128,0), colorSpace='rgb255')
mytext.draw()

mytext = psychopy.visual.TextStim(win, text='PINK', font='Courier New', bold=True, height=30, wrapWidth=textwidth, pos=(displayresolution[0]/6*-2, displayresolution[1]/6*-2), color=(255,0,0), colorSpace='rgb255')
mytext.draw()
mytext = psychopy.visual.TextStim(win, text='YELLOW', font='Courier New', bold=True, height=30, wrapWidth=textwidth, pos=(displayresolution[0]/6*-1, displayresolution[1]/6*-2), color=(0,0,255), colorSpace='rgb255')
mytext.draw()
mytext = psychopy.visual.TextStim(win, text='GREEN', font='Courier New', bold=True, height=30, wrapWidth=textwidth, pos=(displayresolution[0]/6*0, displayresolution[1]/6*-2), color=(255,128,0), colorSpace='rgb255')
mytext.draw()
mytext = psychopy.visual.TextStim(win, text='BLUE', font='Courier New', bold=True, height=30, wrapWidth=textwidth, pos=(displayresolution[0]/6*1, displayresolution[1]/6*-2), color=(255,0,0), colorSpace='rgb255')
mytext.draw()
mytext = psychopy.visual.TextStim(win, text='RED', font='Courier New', bold=True, height=30, wrapWidth=textwidth, pos=(displayresolution[0]/6*2, displayresolution[1]/6*-2), color=(0,255,0), colorSpace='rgb255')
mytext.draw()

win.flip()
clock = core.Clock()
psychopy.event.waitKeys()
mystring = 'It took you {0} seconds. Compare this time with that of the other test. Press any key to exit'.format(round(clock.getTime(),2))
mytext = psychopy.visual.TextStim(win, text=mystring, font='Courier New', bold=True, height=30, wrapWidth=textwidth)
mytext.draw()
win.flip()
psychopy.event.waitKeys()

