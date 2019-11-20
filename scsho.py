from tkinter import * 
from PIL import Image, ImageTk
import pyautogui
import tkinter as tk, threading
import sys, imageio

#Get Video
vid = sys.argv[1:][0]
video = imageio.get_reader(vid)

#Set Tkinter objects
root = tk.Tk()
canvas = tk.Canvas(root, width=600, height=450)
canvas.pack()


def stream(label): 
	for image in video.iter_data(): 
		frame_image = ImageTk.PhotoImage(Image.fromarray(image))
		label.config(image=frame_image)
		label.image = frame_image
		#label.place(x=20,y=20)

#Screen shot button
def take_Shot():
    shot = pyautogui.screenshot()
    shot.save(r'/Users/ugoslight/Desktop/AR/shot.png')
btn = tk.Button(text='Take Screenshot', comman=take_Shot, bg='Gold', fg='white', font=10)
canvas.create_window(225, 430, window=btn)


#Main
if __name__== "__main__":
	my_label = tk.Label(root)
	my_label.place(x=20,y=20)
	thread = threading.Thread(target=stream, args=(my_label,))
	thread.daemon = 1
	thread.start()
	root.mainloop()

root.mainloop()
