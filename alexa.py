from logging import info
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def search_wikipedia(command):
    if 'who the heck is' in command:
        person = command.replace('who the heck is', '').strip()
        try:
            info = wikipedia.summary(person,1)
            print(info)
            talk(info)  
        except wikipedia.exceptions.DisambiguationError :
            print("There are multiple results for this name. Please be more specific.")
            talk("There are multiple results for this name. Please be more specific.")
        except wikipedia.exceptions.PageError:
            print("I couldn't find any information on that person.")
            talk("I couldn't find any information on that person.")
        except Exception as e:
            print("Something went wrong:", str(e))
            talk("Sorry, I couldn't complete the request.")
def take_command():

    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        command = ""  

        try:
            command = recognizer.recognize_google(audio)
            print("You said:", command)
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError:
            print("Sorry, there was an issue with the request.")

    return command  

def run_alexa():
    command = take_command()
    if not command:
        return
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing' +song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' +time)
    elif 'who the heck is' in command:
        search_wikipedia(command)
    elif 'date' in command:
        talk('sorry , I have a headache')
    elif 'are you single' in command:
        talk('I am in relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'stop' in command:
        talk("Goodbye!")
        exit()
    else:
        talk('Please say the command again.')

while True:
    run_alexa()
    
