#IMPORTANT change numbers inside mouse.position depending on your resolution to match tiktok buttons, current positions are for 1920x1080
#prints are for debugging
#to avoid bans you may wanna change time.sleep values to random numbers in wich case you write time.sleep(random.randint(lower number, larger number)/10or100or1000...)
#or add interval to pyautogui.typewrite(comment): pyautogui.typewrite(comment, interval=number)
#although I did not receive a ban during script testing
import webbrowser
import os
import pynput
from pynput.mouse import Button, Controller
import time
import random
from selenium import webdriver
import pyautogui
from tkinter import Tk
from pynput import keyboard
import keyboard
from pynput.keyboard import Key, Listener

def on_press(key):
    pass
def on_release(key):
    if key == Key.esc or key == Key.f2:
            y=50
            exit()
with Listener(on_press=on_press, on_release=on_release) as listener:
    x=0
    y=0
    z=0
    follow=0
    like=0
    f=list(open("comments.txt","r").readlines())
    #print(f.read())
    webbrowser.open('http://tiktok.com')
    mouse = Controller()
    #print ("Current position: " + str(mouse.position)) #this way you can find your current mouse coordinates on the screen so you can put those numbers in mouse.position = (x, y)
    mouse.position = (997, 564) 
    time.sleep(5)
    mouse.press(Button.left)
    mouse.release(Button.left) #click on the video to make it bigger
    time.sleep(2)
    while(y < 15):
        mouse.position = (1452, 1040)
        mouse.press(Button.left)
        mouse.release(Button.left) #click on the comment field
        y+=1
        r=str(f)
        x=random.randrange(0, 5) #change the second number depending how many lines you have in comments.txt file (start counting from 0, also each line is one comment)
        #print(x)
        #print(f[x])
        comment=str(f[x]) #pick comment from the list
        pyautogui.typewrite(comment)
        time.sleep(1.5)
                
        mouse.position = (1334, 592)
        mouse.press(Button.left)
        mouse.release(Button.left) #go to the next video
        time.sleep(1)
        mouse.position = (1452, 1040)

        follow=random.randint(1, 9999999999)
        like=random.randint(1, 9999999999)
        clink=random.randint(1, 9999999999)
        #it has a chance to follow user account, like video or copy video link
        if follow%11 == 0: 
            mouse.position = (1859, 176)
            mouse.press(Button.left)
            mouse.release(Button.left)
        elif like%4 == 0:
            mouse.position = (1425, 318)
            mouse.press(Button.left)
            mouse.release(Button.left)
        elif clink%7 == 0:
            mouse.position = (1847, 364)
            mouse.press(Button.left)
            mouse.release(Button.left)
    listener.join()
