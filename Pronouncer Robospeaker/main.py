
from win32com.client import Dispatch
speak = Dispatch("SAPI.SpVoice").Speak

if __name__ == '__main__':
    print("hello i am robo speaker 1.1 created by Minur Hussain")
    while True:

        x =input("enter your name or text to pronounce\n")
        if x == "q":
            speak("bye bye friend \t i am ending the programme\n programme ended!")
            print("programme ended")
            break
        speak({x})





