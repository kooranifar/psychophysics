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
map=[128 128 128;255 0 255]
Screen('Preference', 'SkipSyncTests', 1);
[wp rect]= Screen(0,'OpenWindow', [0 0 0]);
framesSinceLastWait = Screen('WaitBlanking', wp);
[row col]= size(chiefvec(:,:,1))
r= [0 0 col.*0.5 row.*0.5];
r= CenterRect(r,rect);
HideCursor
for looper=1:3
    for it= 1:20
        if(it==20)
            prioritylevel= MaxPriority(wp)
            Priority(prioritylevel)
            pic= Screen ('MakeTexture', wp, chiefvec(:,:,it))
            Screen ('DrawTexture', wp, pic, [], r)
            framesSinceLastWait = Screen('WaitBlanking', wp);
            Screen ('Flip',wp);
            Priority(0)
            Priority(prioritylevel)
            InitializePsychSound(1);
            nrchannels = 2;
            freq = 48000;
            repetitions = 1;
            beepLengthSecs = 0.05;
            beepPauseTime = 0.02;
            startCue = 0;
            waitForDeviceStart = 1;
            pahandle = PsychPortAudio('Open', [], 1, 1, freq, nrchannels);
            PsychPortAudio('Volume', pahandle, 0.5);
            myBeep = MakeBeep(1500, beepLengthSecs, freq);
            PsychPortAudio('FillBuffer', pahandle, [myBeep; myBeep]);
            PsychPortAudio('Start', pahandle, repetitions, startCue, waitForDeviceStart);
            WaitSecs(beepLengthSecs + beepPauseTime)
            PsychPortAudio('Start', pahandle, repetitions, startCue, waitForDeviceStart);
            WaitSecs(beepLengthSecs)
            PsychPortAudio('Stop', pahandle);
            PsychPortAudio('Close', pahandle);
            Priority(0)
        else
            prioritylevel= MaxPriority(wp);
            Priority(prioritylevel)
            pic= Screen ('MakeTexture', wp, chiefvec(:,:,it));
            Screen ('DrawTexture', wp, pic, [], r)
            Screen ('Flip',wp);
            Priority(0)
            WaitSecs(0.16)
        end
    end
end
pause(3)
Screen('CloseAll')