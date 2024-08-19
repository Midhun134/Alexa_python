import speech_recognition as sr
import pyttsx3 #text to speech
import pywhatkit #used here for utube opening
import datetime
import wikipedia
import time
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id) #to change the voice tone 
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        print("Listening...")
        with sr.Microphone() as source:  # Correct usage of sr.Microphone()
            listener.adjust_for_ambient_noise(source)  # Optional: Adjust for ambient noise
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            
            command = command.lower()
            if 'alexa' in command:
                command = command.replace("alexa", "")#will replace alexa from command

                print(command) #repeat what the user says

    except:
        pass
    return command
def run_alexa():
    command = take_command()
    print(command)
    if "play" in command:
        song = command.replace("play", "")
        talk("playing" + song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        talk("Current time is"+time)
    elif "who is" in command:
        person = command.replace("who is", "")
        info = wikipedia.summary(person, 2)
        print(info)
    elif "stop" in command:
        talk("Adios")
        return False
    else:
        talk("sorry, i didn't understand that command")

        


while True: 
   run_alexa()
   time.sleep(3) #for each iteration
#    if not run_alexa():
#        break
   
   
   

