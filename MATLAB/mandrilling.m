%% Creating abc
clear all;
close all;
sca;
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
Screen('Preference','SkipSyncTests',1);
[wp rect]= Screen(0,'OpenWindow',[0 0 0]);

%% PTB Loading abc
Screen('preference','SkipSyncTests',1);
[wp, rect]= Screen(0,'OpenWindow',[0 0 0]);
r=[0 0 524 424];
r=CenterRect(r,rect);
for f=18:18:3600
    if (mod(f,360)==0)
        r=[0 0 524 424];
        pic=Screen('MakeTexture',wp,barr);
        Screen('DrawTexture',wp,pic,[],r)
    else
        r=[0 0 924 424];
        pic=Screen('MakeTexture',wp,myvec(:,:,mod(f/18,20)));
        Screen('DrawTexture',wp,pic,[],r)
    end
    Screen('Flip',wp)
    pause(0.05)
end
pause(3)
Screen('CloseAll')
