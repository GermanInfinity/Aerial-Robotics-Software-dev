#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 07:04:45 2019

@author: ugoslight
Description: Screenshot collector tool.
Aerial robotics



#import pyautogui
#import tkinter as tk
#from tkinter import filedialog

root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=300)
canvas1.pack()

def scrnsht():
    myshot = pyautogui.screenshot()
    myshot.save(r'/Users/ugoslight/Desktop/AR')
    
myButton = tk.Button(text='shot', command=scrnsht, bg='green', fg='black', font=10)
canvas1.create_window(150, 150, window=myButton)

root.mainloop()


**************************************************
import pyautogui
import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

def takeScreenshot ():
    
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'./')

myButton = tk.Button(text='Take Screenshot', command=takeScreenshot, bg='green',fg='white',font= 10)
canvas1.create_window(150, 150, window=myButton)

root.mainloop()



from tkinter import *
from PIL import ImageTk, Image
import cv2, argparse
import numpy as np 
import sys


from tkinter import *

import tkinter as tk

root = tk.Tk()

app = tk.Frame(root, width=400, height = 400, background="#b22222")
app.grid()#place(relx=.5, rely=.5, anchor="c")

lmain = tk.Label(app)
lmain.place(width=300, height = 300, relx=.5, rely=.5, anchor="c")

video_to_inspect = sys.argv[1:][0]
cap = cv2.VideoCapture(video_to_inspect)
def video_stream():
    _, frame = cap.read()
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(1, video_stream) 
    
 
video_stream()

root.mainloop()
**************************************************
"""
from tkinter import *
from PIL import ImageTk, Image
import cv2, argparse
import numpy as np 
import sys

root = Tk()
# Create a frame
app = Frame(root, width=100, height=100, bg="white")
app.grid()
# Create a label in the frame
lmain = Label(app)
lmain.grid()


video_to_inspect = sys.argv[1:][0]
# Capture from filepath
cap = cv2.VideoCapture(video_to_inspect)

# function for video streaming
def video_stream():
    _, frame = cap.read()
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(1, video_stream) 
    
 
video_stream()
root.mainloop()