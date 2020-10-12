import pyautogui as pyg
import time
import random
import time
from datetime import datetime
import os



clicked = 0
currentTime = str(datetime.now())
timeIntervals = [240,360,120,60,50,30,10]

timeIntervals =[5,6,7]
def actHuman(x):
    selectedTime = random.choice(timeIntervals)
    strSelectedTime = str(selectedTime)
    pyg.scroll(x)
    time.sleep(selectedTime)
    print('Times and the time interval was ',end='')
    print(strSelectedTime)
    
# change url here

url = "https://homeage17.blogspot.com/2020/06/blog-post.html"
logFile = "log.txt" #log file name

f = open(logFile, "a")
f.write('\n----------------------------')
f.write(currentTime)
f.write('----------------------------\n')
f.close()

#opening browser
browserLocation = "C:\Users\Vibhuti\Desktop\minecraft\Storage\Tor Browser\Browser"
os.system("cd "+browserLocation+"&& firefox.exe");
#pyg.hotkey('ctrl','shift','t')
time.sleep(15)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------Capnin----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

while 1:
    
# veriable
    time.sleep(2)
    clicked +=1
    strClicked = str(clicked)

    
#tying  search
    
    pyg.press('f6')
    pyg.write(url)
    time.sleep(0.5)
    pyg.press('enter')
 
#scrolling page

    pyg.moveTo(373,683)
    time.sleep(10)

    actHuman(-10000)
    actHuman(-10000)
    actHuman(-10000)
    
    pyg.scroll(-10000)
    time.sleep(3)
    pyg.scroll(10000)

#changing ip address
    
    pyg.hotkey('ctrl', 'shift','u') #creating new identy in tor
    time.sleep(3)

#adding in log

    f = open(logFile, "a")
    f.write('\nThis link was clicked ')
    f.write(strClicked)
    f.write('\n')
    f.close()

# print on terminal

    print('went over the page ' ,end='')
    print(clicked)
 

#--------------this was made by capnin and uploaded on github----------------------------------------------------------------------------------------------------------------------------------------------------

