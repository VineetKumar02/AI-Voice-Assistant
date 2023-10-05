import datetime
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import google.generativeai as palm   # pip install -U google-generativeai
# pip install pyaudio

import os
from dotenv import load_dotenv
load_dotenv()

# Confugure Palm with API Key
palm.configure(api_key=os.getenv('PALM_API_KEY'))

# Voice Engine Settings
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  # 0 - male, 2 - female


# To make the bot speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# To start the bot with greetings
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


# To get voice input and return the query
def takeCommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()

    with sr.Microphone() as source:
        # wait for a second to let the recognizer adjust the energy threshold based on the surrounding noise level
        r.adjust_for_ambient_noise(source, duration=1)

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"\nUser: {query}")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"

    return query


if __name__ == "__main__":
    # wishMe()

    # An array of "ideal" interactions between the user and the model
    examples = [
        ("Hello Jarvis",  # A hypothetical user input
         "Hello Sir, How ay I help you today? "  # A hypothetical model response
         ),
        ("I'm kind of bored",
         "It's ok sir. Maybe we could try to learn something new sir!")
    ]

    response = palm.chat(
        context="You are Jarvis, my personal assistant. The one is iron man movies. So speak like him",
        examples=examples,
        messages='hello jarvis',
        temperature=1)

    print("Jarvis: ", response.last)
    speak(response.last)

    while True:
        query = takeCommand().lower()
        # print(query)

        if "shutdown" in query and "jarvis" in query:
            print("System Shutting Down. See you soon sir")
            speak("System Shutting Down. See you soon sir")
            exit()

        elif query != "none":
            # Add to the existing conversation by sending a reply
            response = response.reply(query)
            print("Jarvis: ", response.last)
            speak(response.last)


# Tuning Temperature
# You can also change the way the model responses by adjusting the temperature field.
# This field controls how much randomness is injected in the model's responses.
# Setting the temperature close to 1 will allow for more "random," surprising, or even seemingly "creative" model responses.
# Setting the temperature to 0 typically produces more predictable model responses.

# Setting temperature=0 eliminates all randomness in the way model responses are generated.
# Setting temperature=1 usually produces more zany responses!

# response = palm.chat(messages="What should I eat for dinner tonight? List a few options", temperature=1)
# print(response.last)

# Context
# There are two ways to prime models to take on different behaviors.
# One way is to set the context field, describing how the model should behave (i.e. "Speak like Shakespeare").
# You can think of this as zero-shot learning, because you're simply instructing the model how you want it to act.

# reply = palm.chat(context="Be an alien that lives on one of Jupiter's moons",
#                    messages="How's it going?")
# print(reply.last)

# Using Examples
# You can further refine this chatbot's behavior by offering some examples,
# illustrating what you consider to be "ideal" exchanges between user and bot.


# An array of "ideal" interactions between the user and the model
# examples = [
#     ("What's up?", # A hypothetical user input
#      "What isn't up?? The sun rose another day, the world is bright, anything is possible! ☀️" # A hypothetical model response
#      ),
#      ("I'm kind of bored",
#       "How can you be bored when there are so many fun, exciting, beautiful experiences to be had in the world? 🌈")
# ]

# response = palm.chat(
#     context="Be a motivational coach who's very inspiring",
#     examples=examples,
#     messages="I'm too tired to go the gym today")

# print(response.last)
