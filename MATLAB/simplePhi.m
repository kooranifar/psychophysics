clear all
close all
sca
[X,Y]=meshgrid (-7:0.01:6,5:-0.01:-5.5);
Z=X+Y.*i;
radius=4;
for t=1:20
theta=18:18:360;
theta(t)= [];
x= cosd(theta).*radius;
y= sind(theta).*radius;

for j=1:19
    fasele(:,:,j)= sqrt((x(j)-X).^2+(y(j)-Y).^2);
end

flager= (fasele<=0.5);
abc= sum(flager,3);
abc(abc==2)=1;
abc= circshift(abc,-50,2);
abc= circshift(abc,20,1);
myvec(:,:,t)= abc;
end
chiefvec= zeros(1051,3301,20);
plushy= 1630:1670;
plushx= 505:545;
for i=1:20
    motsazi = zeros(1051,1000);
    chiefvec(:,:,i)=[motsazi, myvec(:,:,i), motsazi];
    helpme= chiefvec(:,:,i);
    helpme(525, plushy)=1;
    helpme(plushx, 1650)=1;
    chiefvec(:,:,i)= helpme;
end
chiefvec= chiefvec.*255;
Screen('Preference', 'SkipSyncTests', 1);
[wp, rect]= Screen(0,'OpenWindow', [0 0 0]);
[row, col]= size(chiefvec(:,:,1));
r= [0, 0, col.*0.5, row.*0.5];
r= CenterRect(r,rect);
for it=1:20
    pic(it)=Screen('MakeTexture', wp, chiefvec(:,:,it));
end
PL = MaxPriority(wp);
Priority(PL)
HideCursor
for i=1:10
for j=1:20
    Screen('DrawTexture', wp, pic(j), [], r)
    Screen('Flip', wp)
    framesSinceLastWait = Screen('WaitBlanking', wp);
    pause(0.05)
end
end
Priority(0)
pause(3)
sca