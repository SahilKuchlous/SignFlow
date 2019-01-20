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
    closed_palm = cv2.CascadeClassifier("Haarcascades/closed_frontal_palm.xml")
    palm = cv2.CascadeClassifier("Haarcascades/palm.xml")

    video_capture = cv2.VideoCapture(0)

    while True:
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        closed_palms = closed_palm.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(31, 31),
                flags=cv2.CASCADE_SCALE_IMAGE
        )

        palms = palm.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=6,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE
        )

        for (x, y, w, h) in closed_palms :
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                y = y - 15 if y - 15 > 15 else y + 15
                cv2.putText(frame, "A", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)
                '''tts = gTTS(text="A", lang='en')
                tts.save("tts.mp3")
                os.system("mpg321 tts.mp3")'''

        for (x, y, w, h) in palms :
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 2)
                y = y - 15 if y - 15 > 15 else y + 15
                cv2.putText(frame, "B", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,0), 2)
                '''tts = gTTS(text="B", lang='en')
                tts.save("tts.mp3")
                os.system("mpg321 tts.mp3")'''

        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    video_capture.release()
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
