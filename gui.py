import cv2
import csv
from tkinter import *
from PIL import Image, ImageTk
from imutils.video import VideoStream
from imutils.video import FPS
import time
import imutils

top = Tk()

"""class MyUtils():
    def round(self, can, x, y, width, height, rad):
        can.arc(x, y+rad*2, x+rad*2, y, start = 90, extent = 90, style = ARC)
        can.line(x+rad, y, x+width-rad, y)
        can.arc
"""

def beginStream():

    vs = VideoStream(src=0).start()
    time.sleep(1.0)
    fps = FPS().start()

    def draw(x1, x2, y1, y2, label):
        cv2.rectangle(frame, (x1, y1), (x2, y2),(0,255,0), 2)
        y = y1 - 15 if y1 - 15 > 15 else y1 + 15
        cv2.putText(frame, label, (x1, y),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)

    while True:
        frame = vs.read()
        frame = imutils.resize(frame, width=400)

        draw(15,152,53,199,"Test")

        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break

        fps.update()

    fps.stop()
    print("Elapsed time: {:.2f}".format(fps.elapsed()))
    print("Approx. FPS: {:.2f}".format(fps.fps()))
    cv2.destroyAllWindows()

button = Button(top, text = "Begin Stream", command=beginStream)
button.pack()

top.mainloop()
