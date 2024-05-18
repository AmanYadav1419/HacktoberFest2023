import pyttsx3
import datetime
import os 

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

with open("Alarmtext.txt","rt") as extractedtime:
    time = extractedtime.read()
    Time = str(time)
with open("Alarmtext.txt","r+") as deletetime:
    deletetime.truncate(0)

def ring(time):
    timeset = str(time)
    timenow = timeset.replace("jarvis","")
    timenow = timenow.replace("set an alarm","")
    timenow = timenow.replace(" and ",":")
    Alarmtime = timenow
    print(Alarmtime)
    while True:
        currenttime = datetime.datetime.now().strftime("%H:%M:%S")
        if currenttime == Alarmtime:
            speak("Alarm ringing,sir")
            os.startfile("music.mp3")
        elif f"{currenttime}00:00:30" == Alarmtime:
            exit()

ring(time)
