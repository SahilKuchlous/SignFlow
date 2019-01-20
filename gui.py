import cv2
import csv
from tkinter import *
from PIL import Image, ImageTk
from imutils.video import VideoStream
from imutils.video import FPS
import time
import imutils
import speech_recognition as sr
import pyaudio

top = Tk()

def beginStream():
    print("Video Stream starts!")
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

def beginRecording():
    print("Recording starts!")
    recog = sr.Recognizer()
    mic = sr.Microphone()
    
    with mic as source:
        try:
            recog.adjust_for_ambient_noise(source)
            audio = recog.listen(source)
            r = recog.recognize_google(audio).upper()
            print(r)
            text = open("dataStorage.txt", "w")
            for i in r:
                if ord(i) != 32:
                    text.write(i+"\n")

                    img = cv2.imread("datasets\\Signs\\"+i+".jpg")
                    cv2.imshow("img",img)
                    cv2.waitKey()
            text.close()
        except:
            print("Error:Inaudible. Try again")

button = Button(top, text = "Begin Stream", command=beginStream)
button.pack()
button2 = Button(top, text = "Begin Recording", command = beginRecording)
button2.pack()

top.mainloop()
