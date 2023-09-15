import asyncio, json
import os
import re
import datetime

import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition

# pip install EdgeGPT --upgrade
from EdgeGPT.EdgeGPT import Chatbot, ConversationStyle
from EdgeGPT.EdgeUtils import ImageQuery
from EdgeGPT.EdgeUtils import Query, Cookie

# pip install pyAudio


# Voice Engine Settings
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[2].id)  # 0 - male, 2 - female

# EdgeGPT Settings
cookies = json.loads(open("bing_cookies.json", encoding="utf-8").read())
imagePath = "./images"
ImageQuery.image_dir_path = imagePath


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


# To Preprocess the text before speaking out
def clean_text_for_speech(text):
    # Remove [^#^] citations in response
    text = re.sub(r"\[\^\d+\^\]", "", text)

    # Keep only alphanumeric characters, spaces, and common punctuation marks
    text = re.sub(r"[^a-zA-Z0-9.,!? \n]", "", text)

    return text.strip()


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
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"

    return query


# Function to generate response from Bing AI
async def bingAI_text(query):

    try:
        bot = await Chatbot.create(cookies=cookies)

        response = await bot.ask(
            prompt=query,
            conversation_style=ConversationStyle.precise,
        )

        # Select only the bot response from the response dictionary
        for message in response["item"]["messages"]:
            if message["author"] == "bot" and "messageType" not in message:
                bot_response = clean_text_for_speech(message["text"])

                print(bot_response)
                # speak(bot_response)
                break

        await bot.close()

    except Exception as e:
        print("Error from Bot: {0}".format(e))


# Function to generate images from Bing AI
def bingAI_image(query):

    try:
        for filename in os.listdir(imagePath):
            file_path = os.path.join(imagePath, filename)

            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                os.rmdir(file_path)

        q = ImageQuery(
            query,
            cookie_files="./bing_cookies.json",
        )

    except Exception as e:
        print("Error from BOT: {0}".format(e))



# Entry point of code
if __name__ == "__main__":

    q = ImageQuery(
            "Images of vande bharat train",
            cookie_files="./bing_cookies.json",
        )
    # q = Query(
    #     "What are you? Give your answer as Python code",
    #     style="creative",  # or: 'balanced', 'precise'
    #     cookie_files="./bing_cookies.json"
    #     )
    # print(q)

    # wishMe()

    # Run forever. Untill user says shutdown
    # while True:
    #     query = takeCommand().lower()

    #     if "shutdown" and "jarvis" in query:
    #         print("System Shutting Down")
    #         speak("System Shutting Down")
    #         exit()

    #     elif "generate" and "image" in query:
    #         bingAI_image(query)

    #     elif query != "none":
    #         asyncio.run(bingAI_text(query))

    # q = Query(
    #     "What are you?",
    #     style="precise",  # or: 'balanced', 'creative'
    #     cookie_files="./bing_cookies.json",
    #     echo=False,
    # )
    # print(q)
