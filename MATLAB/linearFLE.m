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
a2(x,y) = 255;
a2(x,y2) = 255;
PL = MaxPriority(wp);
Priority(PL)
for j=1:4
for i= 0:3:360
    Priority(PL)
    rander = round(rand.*29+1);
    if(flag~=2)
        if(flag ~= 1)
            if (rander == 11)
                flag=1;
                pic  = Screen('MakeTexture', wp, a2);
            else
                pic = Screen('MakeTexture', wp, a);
            end
        else
            pic = Screen('MakeTexture', wp, a);
            flag = 2;
        end
    else
        pic = Screen('MakeTexture', wp, a2);
        flag=0;
    end 
    Screen('DrawTexture', wp, pic, [], [], i);
    Screen('Flip', wp)
    frameSinceLastWait = Screen('WaitBlanking', wp);
end
end
Priority(0)
WaitSecs(3)
sca