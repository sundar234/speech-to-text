import speech_recognition as sr
import pyttsx3

r=sr.Recognizer()

def SpeakText(command):
    engine=pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

while(1):
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source,duration=0.10)
            print("Please say something....")
            audio=r.listen(source)


            MyText=r.recognize_google(audio)
            MyText=MyText.lower()

            print("You have said  "+MyText)
            print("Audio recorded Successfully \n")
            SpeakText(MyText)
            

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("unknown error occured")
    
