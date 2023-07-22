# Python program to translate speech to text and text to speech
import pywhatkit as kit   # pip install pywhatkit
import speech_recognition as sr
import pyttsx3


r = sr.Recognizer()    

# Function to convert text to speech
def SpeakText(command):
	
	# Initialize the engine
	engine = pyttsx3.init()
	engine.say(command)
	engine.runAndWait()
	
def speech_to_text():	
	# Exception handling to handle exceptions at the runtime
    while (1):
        try:
                    
            # use the microphone as source for input.
            with sr.Microphone() as source:
                        
                # wait for a second to let the recognizer adjust the energy threshold based on the surrounding noise level
                r.adjust_for_ambient_noise(source, duration=1)
                print("Listening...")    
                    
                #listens for the user's input
                audio = r.listen(source)
                        
                # Using google to recognize audio
                MyText = r.recognize_google(audio)
                MyText = MyText.lower()

                print("User said:",MyText)
                return MyText
                #print("Did you say "+MyText)
                #SpeakText(MyText)  #Use for making program speak
                        
        except sr.RequestError as e:
            print("Jarvis: Could not request results; {0}".format(e))
                    
        except sr.UnknownValueError:
            print("Jarvis: Couldn't hear properly !! say again")

def jarvis(s):   
    if 'message' in s:
        num=input("Enter Mob No. (without country code): ")
        t=input("Enter time in hours and min format: ").split()
        s=input("Enter the Message: ")
        kit.sendwhatmsg('+91'+num,s,int(t[0]),int(t[1]))
    elif 'youtube' in s:
        print("Say the Video Title: ")
        search=speech_to_text()
        SpeakText("Opening"+search+"for u sir")
        kit.playonyt(search)
    elif 'google' in s:
        kit.search(input("Enter the Topic: "))
    elif 'text' in s:    
        kit.text_to_handwriting(input("Enter the Text: "))
    elif 'exit' or 'quit' or 'shutdown' in s:
        exit
    else:
        print("Couldn't hear properly !! say again") 
        s=speech_to_text()

SpeakText("hello sir. jarvis at your service")
print('''\nEnter the Action you want to perform:-
         1) Send Whatsapp Message.
         2) Play something on Youtube.
         3) Search something on Google.
         4)Convert text to Handwriting format.''')
s=speech_to_text()
jarvis(s)