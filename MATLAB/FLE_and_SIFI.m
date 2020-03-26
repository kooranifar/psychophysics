clear all
close all
sca
Screen('Preference','SkipSyncTests',1)
[wp, rect] = Screen(0, 'OpenWindow');
framesSinceLastWait = Screen('WaitBlanking', wp);
x0 = rect(3)/2;
y0 = rect(4)/2;
PL = MaxPriority(wp);
for j = 1:10
for i = 0:1:59
    x = x0 + cosd(i.*6).*100;
    y = y0 + sind(i.*6).*100;
    rander = round(rand.*49+1);
    Priority(PL)
    Screen('FillOval', wp, [0 0 0], [x - 30, y - 30, x + 30, y + 30])
    if(flag~=2)
        if(flag ~= 1)
            if (rander == 5)
                flag=1;
                Screen('FillOval', wp, [255 255 0], [x - 25, y - 25, x + 25, y + 25])
            else
                Screen('FillOval', wp, [0 0 255], [x - 25, y - 25, x + 25, y + 25])
            end
        else
            Screen('FillOval', wp, [0 0 255], [x - 25, y - 25, x + 25, y + 25])
            flag=2;
        end
    else
        Screen('FillOval', wp, [255 255 0], [x - 25, y - 25, x + 25, y + 25])
        flag=0;
    end 
    DrawFormattedText(wp, '+', 'center', 'center', [0 0 255])
    Screen('Flip', wp)
    Priority(0)
end 
end

pause(2)
sca