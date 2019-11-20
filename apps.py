#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 07:24:45 2019

@author: ugoslight
"""
from tkinter import *
from PIL import ImageTk, Image
import cv2
import argparse
import sys
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
