from gtts import gTTS
import os
tts = gTTS(text="I can recognize sign language", lang='en')
tts.save("tts.mp3")
os.system("mpg321 tts.mp3")