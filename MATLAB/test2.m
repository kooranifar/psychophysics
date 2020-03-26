clear all
close all
sca
[X,Y]=meshgrid (-7:0.1:6,5:-0.1:-5.5);
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
abc= circshift(abc,-5,2);
abc= circshift(abc,2,1);
myvec(:,:,t)= abc;
end

helper= myvec(:,:,20);
barr= zeros(106,100);
barr= [helper,barr];
yrange= 120:160;
xrange= 50:56;
barr(xrange,yrange)= 1;
barr= barr+1;
myvec= myvec+1;
map=[128 128 128; 255 0 255]
Screen('Preference', 'SkipSyncTests', 1);
[wp rect]= Screen(0,'OpenWindow', [128 128 128]);
HideCursor
for looper=1:10
for it= 1:20
    if (it==20)
        [row col]= size(barr)
        r= [0 0 col.*3 row.*3]
        r= CenterRect(r,rect)
        r(1)=r(1)+150
        r(3)=r(3)+150
        X2=ind2rgb(barr,map)
        pic= Screen ('MakeTexture', wp, X2)
        Screen ('DrawTexture', wp, pic, [], r)
    else
        
        [row col]= size(myvec(:,:,it))
        r= [0 0 col.*3 row.*3]
        r= CenterRect(r,rect)
        X2=ind2rgb(myvec(:,:,it),map)
        pic= Screen ('MakeTexture', wp, X2)
        Screen ('DrawTexture', wp, pic, [], r)
    end
    DrawFormattedText(wp,'+','center','center',[255 255 255])
    prioritylevel= MaxPriority(wp)
    Priority(prioritylevel)
    framesSinceLastWait = Screen('WaitBlanking', wp);
    Screen ('Flip',wp);
    Priority(0)
    pause(0.01)
end
end
pause(3)
Screen('CloseAll')