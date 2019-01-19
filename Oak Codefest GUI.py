import cv2
import csv
from tkinter import *
from PIL import Image, ImageTk

top = Tk()

"""class MyUtils():
    def round(self, can, x, y, width, height, rad):
        can.arc(x, y+rad*2, x+rad*2, y, start = 90, extent = 90, style = ARC)
        can.line(x+rad, y, x+width-rad, y)
        can.arc
"""

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Sign Language Recog and Translation")
        self.button = Button(master, text = "Begin Stream", command = self.beginStream(master))
        self.button.pack()

    def beginStream(self, master):
        vc = cv2.VideoCapture(0)

        if vc.isOpened():
            rval, frame = vc.read()
        else:
            rval = False

        while rval:
            cv2.imshow("Video", frame)
            rval, frame = vc.read()
            key = cv2.waitKey(20)
            if key == 27:
                break
        cv2.destroyWindow("Video")
        
        
gui = GUI(top)
top.mainloop()
