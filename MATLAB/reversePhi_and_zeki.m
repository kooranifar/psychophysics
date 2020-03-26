clear all
close all
sca
Screen ('Preference','SkipSyncTests',1)
[wp, rect]= Screen (0,'OpenWindow',128);
squareside= 100;
rectinrect= [rect(3)/4.*1, rect(4)/4.*1, rect(3)/4.*3, rect(4)/4.*3];
squareblackx= [rect(3)/4.*3-squareside-100, rect(3)/4.*3-100];
squareredx= [rect(3)/4.*1+100, rect(3)/4.*1+squareside+100];

rect41= rect(4)/4.*1;
rect43= rect(4)/4.*3;
step= +4;
borderwidth = 1;
cf=1;
for j= 1:3
    adad= 420;
    cf= cf.*-1;
    if (mod(j,2)==1)
        for i= rect(4)/4.*1 :+4:rect(4)/4.*3-squareside-4
            adad= adad-8;
            Screen ('FrameRect', wp, [255, 0, 0], [rect(3)/4.*1-borderwidth, rect(4)/4.*1-borderwidth, rect(3)/4.*3+borderwidth, rect(4)/4.*3+borderwidth])
            if (cf==-1)
            Screen ('FillRect', wp, 0, [squareblackx(1),i,squareblackx(2),i+squareside]);                
            Screen ('FillRect', wp, 255, [squareredx(1),i+adad,squareredx(2),i+adad+squareside]);
            end
            Screen ('Flip', wp);
        end
    end
    
    if (mod(j,2)==0)
        for i=  rect(4)/4.*3-squareside:-4:rect(4)/4.*1+4
            adad= adad-8;
            Screen ('FrameRect', wp, [255, 0, 0], [rect(3)/4.*1-borderwidth, rect(4)/4.*1-borderwidth, rect(3)/4.*3+borderwidth, rect(4)/4.*3+borderwidth], borderwidth)
            if (cf==1)
            Screen ('FillRect', wp, 255, [squareblackx(1),i,squareblackx(2),i+squareside]);
            Screen ('FillRect', wp, 0, [squareredx(1),i-adad,squareredx(2),i-adad+squareside]);
            end
            Screen ('Flip', wp);
        end
    end
end
pause(3);    
sca; 