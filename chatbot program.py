import speech_recognition as s
import pyttsx3 as p
import csv
r=s.Recognizer()
file=open(r"pythonchatbot.csv")
data=csv.reader(file)
d={}
for i in data:
     d[i[0]]=i[1]
print("---------------------------------------------------\n>>> Press 1 to give Speech input"+"\n"+">>> Press 2 to give Text input\n---------------------------------------------------\n ")
p.speak("Press 1 to give speech input"+"\n"+"Press 2 to give text input")
p.speak("Enter Your Choice")
user_input=int(input("Enter your Choice:"))
while True:
    if user_input==1:
        def speechbot():
            print("Speak in English about the details that you want to know....")
            p.speak("speak in english about the details that you want to know....")
            print("Listening...")
            with s.Microphone() as source:
                audio=r.listen(source)
                txt=r.recognize_google(audio)
                txt=txt.lower()
                print(txt)
                if txt in d.keys():
                    print(d[txt])
                    p.speak(d[txt])
                else:
                    print("Sorry i can't get your question...Please repeat it again")
                    p.speak("Sorry i can't get your question...Please repeat it again")
            print("\n"+"Do you want to Search anymore?")
            p.speak("Do you want to Search anymore?")
            p.speak("Press Enter to Continue or Press anyother key to exit...")
            c=input("Press Enter to Continue or Press anyother key to exit... :")
            if c=="":
                speechbot()
            else:
                print("\nThanks for contacting me\n--------------x----------------------x---------------")
                p.speak("Thanks for contacting me")
        speechbot()
    try:
        if user_input==2:
            def txtbot():
                p.speak("Enter a Text input the about details that you want from me:")
                a=input("Enter a Text input the about details that you want from me:")
                if a in d.keys():
                    print(d[a])
                    p.speak(d[a])
                else:
                    print("OOPS... CAN YOU PLEASE REPEAT YOUR QUESTION AGAIN?")
                    p.speak("OOPS... CAN YOU PLEASE REPEAT YOUR QUESTION AGAIN?")
                print("\n"+"Anymore Questions...")
                p.speak("Anymore Questions...")
                p.speak("Press Enter to Continue or anyother key to exit:")
                b=input("Press Enter to Continue or anyother key to exit:")
                if b=="":
                    txtbot()
                else:
                    print("\nThanks for Contacting me\n--------------x----------------------x---------------")
                    p.speak("Thanks for Contacting me")
            txtbot()
    except NameError:
        break
    break
file.close()
