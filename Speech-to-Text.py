

import speech_recognition as sr 
from googletrans import Translator

translator=Translator()

AUDIO_FILE = ("hindi1.wav") 
  
# use the audio file as the audio source 
  
r = sr.Recognizer() 
with sr.AudioFile(AUDIO_FILE) as source: 
    #reads the audio file. Here we use record instead of 
    #listen 
    audio = r.record(source)   
  
try: 
    #print("The audio file contains: " + r.recognize_google(audio)) 
    #fh.write(r.recognize_google(audio)+".")
    content=r.recognize_google(audio)
    result = translator.translate(content,dest='en')
    print("Destination: {}".format(result.text))
    print("Pronounciation: {}".format(result.pronunciation))    

except sr.UnknownValueError: 
    print("Google Speech Recognition could not understand audio") 
  
except sr.RequestError as e: 
    print("Could not request results from Google Speech  Recognition service; {0}".format(e)) 