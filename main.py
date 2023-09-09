import os
import pyttsx3

if __name__ == '__main__':
    print ("Welcome to HiRobo")
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    while(True):
        cmd = input("Enter what you want to say OR enter 0 to exit : ")
        if(cmd == '0'):
            break
        engine.say(cmd)
        engine.runAndWait()
