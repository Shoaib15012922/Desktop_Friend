import speech_recognition as sr
import os  # To interact with the operating system
import webbrowser
import datetime


def say(text: object) -> object:

    os.system(f"say -v Karen {text}")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=4)  # Adjust the timeout as needed
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred"


if __name__ == '__main__':
    print('Aditi is Active')
    say("Hi Shoaib I am Aditi , Your Buddy")
    while True:
        print("You can Speak")
        query = takeCommand()
        sites = [["youtube", "https://www.youtube.com/"], ["linkedin", "https://www.linkedin.com/feed/"],
                 ["google", "https://www.google.co.in/"], ["gmail", "https://mail.google.com/mail/u/0/?ogbl#inbox"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening Sir")
                webbrowser.open(site[1])

        if "the time" in query.lower():
            hour = datetime.datetime.now().strftime("%H")
            minute = datetime.datetime.now().strftime("%M")
            say(f"Sir the time is {hour} hour and {minute} minutes")

        if "Thank".lower() in query.lower():
            say(f"Anything for my Buddy")

        if "Bye".lower() in query.lower():
            say(f"Bye Shoaib")
            exit()


