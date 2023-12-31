import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

# pip install pyAudio

engine = pyttsx3.init()
voices = engine.getProperty("voices")
# print(voices[1].id)
engine.setProperty("voice", voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 16:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    print("I am Jarvis Sir. Please tell me how may I help you")
    speak("I am Jarvis Sir. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            print("Opening Youtube")
            webbrowser.open("https://youtube.com")

        elif "open google" in query:
            print("Opening Google")
            webbrowser.open("https://google.com")

        elif "open stack over flow" in query:
            print("Opening Stack Over Flow")
            webbrowser.open("https://stackoverflow.com")

        elif "play music" in query:
            print("Playing Music")
            music_dir = "D:\\Non Critical\\songs\\Favorite Songs2"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir, the time is {strTime}")
            speak(f"Sir, the time is {strTime}")

        elif "open code" in query:
            print("Opening Code")
            codePath = "C:\\Users\\Vineet\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif "my name" in query:
            print("your name is Vineet Kumar")
            speak("your name is  Vineet Kumar")

        elif "candidate manual" in query:
            manualPath = "C:\\Users\\Vineet\\Desktop\\Candidate User Manual SSN V3.pdf"
            os.startfile(manualPath)

        elif "shut down" in query:
            print("System Shutting Down")
            speak("System Shutting Down")
            exit()
