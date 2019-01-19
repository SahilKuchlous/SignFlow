# remember to remove the debuggers
import speech_recognition as sr
import pyaudio
recog = sr.Recognizer()
mic = sr.Microphone()
with mic as source:
    print(1)
    recog.adjust_for_ambient_noise(source)
    audio = recog.listen(source)
print(2)
r = recog.recognize_google(audio).upper()
print(r)
print(3)
text = open("dataStorage.txt", "w")
for i in r:
    if ord(i) != 32:
        text.write(i+"\n")
text.close()
