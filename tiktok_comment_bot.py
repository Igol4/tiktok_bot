import webbrowser
import os
import subprocess
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
    #print ("Current position: " + str(mouse.position))
    mouse.position = (997, 564)
    time.sleep(5)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(2)
    while(y < 15):
        mouse.position = (1452, 1040)
        mouse.press(Button.left)
        mouse.release(Button.left)
        y+=1
        r=str(f)
        x=random.randrange(0, 5)
        #print(x)
        print(f[x])
        comment=str(f[x])
        pyautogui.typewrite(comment)
        time.sleep(1.5)
                
        mouse.position = (1334, 592)
        mouse.press(Button.left)
        mouse.release(Button.left)
        time.sleep(1)
        mouse.position = (1452, 1040)
        #mouse.press(Button.left)
        #mouse.release(Button.left)
        #y+=1
        #z=random.randrange(0, 5)
        #comment=str(f[z])
        #pyautogui.typewrite(comment)
        #mouse.position = (1452, 1040)
        #time.sleep(1.5)

        follow=random.randint(1, 9999999999)
        like=random.randint(1, 9999999999)
        clink=random.randint(1, 9999999999)
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
        time.sleep(5)
    listener.join()
    
