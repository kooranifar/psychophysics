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
barr= barr+1
myvec= myvec+1
Screen('Preference', 'SkipSyncTests', 1);
[windowPtr rect]= Screen(0,'OpenWindow', [0 0 0]);
HideCursor
for it= 1:20
    if (it==20)
        [a(it) rect]=Screen('OpenOffscreenWindow',0);
        [row col]= size(barr);
        r= [0 0 col.*3 row.*3];
        r= CenterRect(r,rect);
        r(1)=r(1)+150;
        r(3)=r(3)+150;
        pic= Screen ('MakeTexture', a(it), barr);
        Screen ('DrawTexture', a(it), pic, [], r);
        DrawFormattedText(a(it),'+','center','center',[255 255 255]);
    else
        [a(it) rect]=Screen('OpenOffscreenWindow',0);
        [row col]= size(myvec(:,:,it));
        r= [0 0 col.*3 row.*3];
        r= CenterRect(r,rect);
        pic=Screen('MakeTexture', a(it), myvec(:,:,it));
        Screen('DrawTexture', a(it), pic, [], r);
        DrawFormattedText(a(it),'+','center','center',[255 255 255]);
    end
end
for ite= 1:20
    Screen('CopyWindow',a(ite),windowPtr)
    prioritylevel= MaxPriority(windowPtr)
    Priority(prioritylevel)         
    Screen ('Flip',windowPtr)
    Priority(0)
end
pause(3)
Screen('CloseAll')