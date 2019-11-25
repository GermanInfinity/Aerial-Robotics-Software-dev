#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 19:58:30 2019

@author: ugoslight
"""

import tkinter as tk
from PIL import ImageTk, Image

#This creates the main window of an application
window = tk.Tk()
window.title("SEE image and ENTER its information")
window.geometry("600x400")
window.configure(background='grey')

#Creates a tkinter-compatible photo image.
path = "l.jpg"
img = ImageTk.PhotoImage(Image.open(path))

#The Label widget is a standard tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image = img)

# Create textbox in window
text_widget = tk.Text(panel)
text_widget.insert('insert',"Enter image information here")
text_widget.pack(anchor = "w", padx = 50, pady = 50)


#The Pack geometry manager packs widgets in rows or columns.
#panel.pack(side = "bottom", fill = "both", expand = "no")
panel.pack()


#Start the GUI
window.mainloop()