close all;
clear all;
sca;
screens=Screen('Screens');
[window,windowRect]=PsychImaging('OpenWindow',0);
ifi = Screen('GetFlipInterval',window);
numSecs=1;
numFrames=round(numSecs/ifi);
waitframes=1;
for frame=1:numFrames
    screen('FillRect',window,[128 128 128]);
    Screen('Flip',window);
end
vbl=Screen('Flip',window);
for frame=1:numFrames
    Screen('FillRect',window,[128 0 0]);
    vbl=Screen('Flip',window,vbl+(waitframes-0.5)*ifi);
end
priority(topPriorityLevel);
vbl= Screen('Flip',window);
for frame =1:numFrames
    Screen('FillRect',window,[128 0 128]);
    vbl=Screen('Flip',window,vbl+(waitframes-0.5)*ifi);
end
    
priority(0);
priority(topPriorityLevel);
vbl= Screen('Flip',window);
for frame =1:numFrames
    Screen('FillRect',window,[0 0 128]);
    Screnn('DrawingFinished',window);
    vbl=Screen('Flip',window,vbl+(waitframes-0.5)*ifi);
end
priority(0);
close all;
clear all;
sca;