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
plushy= 630:670;
plushx= 505:545;
for i=1:19
    helpme= myvec(:,:,i);
    helpme(525, plushy)=1;
    helpme(plushx, 650)=1;
    myvec(:,:,i)= helpme;
end
myvec= myvec+1;
map =[128 128 128;255 0 255];
Screen('Preference', 'SkipSyncTests', 1);
[wp, rect]= Screen(0,'OpenWindow', [128 128 128]);
framesSinceLastWait = Screen('WaitBlanking', wp);
HideCursor
[row, col]= size(myvec(:,:,1));
r= [0 0 col.*0.5 row.*0.5];
r= CenterRect(r,rect);
flag= 1;
sar=1;
tah=20;
steper=1;
for looper=1:5
    ejaze= round(rand);
    if (flag==-1)
        sar= 20;
        tah= 1;
    end
    if(flag==1)
        sar= 1;
        tah= 20;
    end
    for it= sar:steper:tah
        rander= round(rand.*9+1);
        if(ejaze==1)
            if(it==rander)
                flag=flag.*-1;
                steper=steper.*-1;
                if (flag==1)
                    sar= it+1;
                    tah= 20;
 
                else
                    sar= it-1;
                    tah= 1;
                end
            end
        end
        prioritylevel= MaxPriority(wp);
        Priority(prioritylevel)
        if (flag==1)
            map =[128 128 128;0 0 0];
        end
        if (flag==-1)
            map =[128 128 128;255 255 255];
        end
        X=ind2rgb(myvec(:,:,it),map);
        pic= Screen ('MakeTexture', wp, X);
        Screen ('DrawTexture', wp, pic, [], r)
%         DrawFormattedText(wp,'+','center','center',[255 255 255])
        Screen ('Flip',wp);
        pause(0.05)
        Priority(0)
    end
end
pause(3)
Screen('CloseAll')
