clear all
close all
sca
Screen('Preference','SkipSyncTests',1)
[wp, rect]= Screen(0,'OpenWindow', 0);
framesSinceLastWait = Screen('WaitBlanking', wp);
HideCursor
a = zeros(700,700);
a2 = zeros(700,700);
y = 351:600;
y2 = 611:700;
x = 347:353;
a(x,y) = 255;
a2(x,y) = 2555;
a2(x,y2) = 255;
[row, col] = size(a);
r = [0,0,col,row];
r=CenterRect(r,rect);
PL = MaxPriority(wp);
Priority(PL)
    for i= 0:1:360-1
        rander = round(rand.*49+1);
        if (rander == 33)
            flag=1;
            pic = Screen('MakeTexture', wp, a2);
        else
            pic = Screen('MakeTexture', wp, a);
        end
        Screen('DrawTexture' ,wp, pic, [], r,i);
        Screen('Flip', wp)
        frameSinceLastWait = Screen('WaitBlanking', wp);
    end
Priority(0)
WaitSecs(5)
sca