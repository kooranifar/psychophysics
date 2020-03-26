clear all
close all

% drawing the half circle
[X,Y]= meshgrid (-7:0.1:6,5:-0.1:-5.5);
Z=X+Y.*i;
fasele = abs(Z);  
x = 1:50;
y = 1:131;
fasele(x,y)=0;
flager = ((fasele >= 2.25) &  (fasele <= 3));
flager = circshift(flager,-5,2);
flager = circshift(flager,2,1);
flager = flager+1;

% loading PTB
HideCursor
Screen('Preference','SkipSyncTests',1)
[wp, rect] = Screen(0,'OpenWindow');
framesSinceLastWait = Screen('WaitBlanking', wp);
map = [255, 255, 255;128, 128, 128];
[row, col] = size(flager);
r = [0, 0, col, row];
r = r.*3;
r = CenterRect(r, rect);
for q = 1:10
    if (mod(q,2)==1)
        PL = MaxPriority(wp);
        Priority(PL)
        X = ind2rgb(flager, map);
        pic = Screen('MakeTexture', wp, X);
        Screen('DrawTexture', wp, pic, [], r)
        Screen('Fillrect', wp, [255, 0, 0], [595, 370, 615, 380])
        Screen('Flip', wp)
        WaitSecs(0.15)
        Priority(0)
    else
        Priority(PL)
        pic = Screen('MakeTexture', wp, X);
        Screen('DrawTexture', wp, pic, [], r)
        Screen('Fillrect', wp, [255, 0, 0], [754, 370, 774, 380])
        Screen('Flip', wp)
        WaitSecs(0.15)
        Priority(0)
    end
    Priority(PL)
    pic = Screen('MakeTexture', wp, X);
    Screen('DrawTexture', wp, pic, [], r)
    Screen('Fillrect', wp, [255, 255, 255], [595, 370, 615, 380])
    Screen('Fillrect', wp, [255, 255, 255], [754, 370, 774, 380])
    Screen('Flip', wp)
    WaitSecs(0.5)
    Priority(0)
end
sca




