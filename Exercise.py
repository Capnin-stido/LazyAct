import time 
import datetime
import cv2
import numpy as np


def chetime():  
    minutes = datetime.datetime.now().minute
    hours = (datetime.datetime.now().hour)*60
    time = hours+minutes
    return(time)



def video():
    cap = cv2.VideoCapture('video.webm')
    while 1:
        ret , frame = cap.read()
        cv2.imshow('frame',frame)
        k = cv2.waitKey(0)
        if k == ord('q'):
            print('prospnded' , water)
            break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()


water = int(input('Enter time you want drink water: '))
ext = int(input('Enter time you want to do exercise: '))
eye = int(input('Enter time you want to do exercise of eye: '))


startingtime = chetime()
while 1:
    time.sleep(1)
    current = chetime()
    Time = current - startingtime
    print("Time: ",Time)
    if Time == water:
        video()
        water +=water
        continue
    if ext == Time :
        video()
        ext += ext
        continue
    if eye ==Time:
        video()
        eye += eye
        continue
    
    else:
        continue
