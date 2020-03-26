clear all
close all
[X,Y]=meshgrid (-7:0.1:6,5:-0.1:-5.5);
Z=X+Y.*i;
fasele= abs(Z);
flager = ((fasele >= 2.75) &  (fasele <= 3));
flager= flager.*255;
[row, col]= size(flager);
r= [0, 0, col, row];
Screen('Preference','SkipSyncTests',1);
[wp, rect]= Screen(0,'OpenWindow', [0 0 0]);
HideCursor
for i=1:15
    pause(0.5)
    if (mod(i,3)==0)
        InitializePsychSound(1);
        nrchannels = 2;
        freq = 3000;
        repetitions = 1;
        beepLengthSecs = 0.07;
        beepPauseTime = 0.01;
        startCue = 0;
        waitForDeviceStart = 1;
        pahandle = PsychPortAudio('Open', [], 1, 1, freq, nrchannels);
        PsychPortAudio('Volume', pahandle, 0.5);
        myBeep = MakeBeep(500, beepLengthSecs, freq);
        PsychPortAudio('FillBuffer', pahandle, [myBeep; myBeep])
        PsychPortAudio('Start', pahandle, repetitions, startCue, waitForDeviceStart);
        WaitSecs(beepLengthSecs)   
        
        r= CenterRect(r,rect);
        r(1)=r(1)-100;
        r(3)=r(3)-100;
        pic= Screen('MakeTexture', wp, flager);
        Screen('DrawTexture', wp, pic,[], r);
        DrawFormattedText(wp,'+','center','center',[255 255 255]);
        Screen('Flip', wp);
        
        WaitSecs(beepPauseTime)
        PsychPortAudio('Start', pahandle, repetitions, startCue, waitForDeviceStart);
        WaitSecs(beepLengthSecs)
        
        r2=CenterRect([0,0,150,150],rect)
        Screen('Fillrect', wp, [0 0 0], r2)
        DrawFormattedText(wp,'+','center','center',[255 255 255]);
        Screen('Flip', wp);
        
        PsychPortAudio('Stop', pahandle);
        PsychPortAudio('Close', pahandle);
    end
    DrawFormattedText(wp,'+','center','center',[255 255 255])
    Screen('Flip',wp)
    
end
sca