import pyttsx3  #pip install pyttsx3
import datetime
import speech_recognition as sr  #pip install SpeachRecognition
import wikipedia  #pip install wikipedia
import smtplib
import webbrowser as wb
import os

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Keep [0] for male voice and [1] for female voice


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():                    # To detect current system time
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is ")
    speak(Time)


def date():                    # To detect current system date
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("The current date is ")
    speak(day)
    speak(month)
    speak(year)


def wish_me():                 # To wish the user at start
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        speak("Good Morning sir! ")
    elif 12 <= hour < 18:
        speak("Good Afternoon sir! ")
    elif 18 <= hour < 24:
        speak("Good Evening sir! ")
    else:
        speak("Good Night sir! ")
    speak("Welcome back ! ")
    speak("Jarvis at your service. Please tell me how can i help you? ")


def takeCommand():           # To listen and recognize your voice
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 4
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again please...")

        return "None"
    return query


def send_Email(to, content):            #To send email
    server = smtplib.SMTP('smtp.gmail.com', 587)       #SMTP-Simple Mail Transfer Protocol
    server.ehlo()
    server.starttls()
    server.login('YOUR EMAIL@gmail.com','YOUR PASSWORD')       # Write your Email and password here
    server.sendmail('YOUR EMAIL@gmail.com', to, content)       # Write your Email here
    server.close()

if __name__ == "__main__":

    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'   # Path of chrome app in your system

    wish_me()
    while True:
        query = takeCommand().lower()

        if 'what is your name' in query:
            speak('My name is JARVIS !')

        elif 'who are you' in query:
            speak('My name is JARVIS !')

        elif 'what is the meaning of your name' in query:
            speak('J. A. R. V. I. S. stands for JUST A RATHER VERY INTELLIGENT SYSTEM')

        elif 'time' in query:
            time()

        elif 'date' in query:
            date()

        elif 'hello jarvis' in query:
            speak("Hello sir!")

        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences = 2)
            print(result)
            speak(result)

        elif 'send email' in query:
            try:
                speak("What is the message ?")
                content = takeCommand()
                speak(content)
                to = 'XYZ@gmail.com'             # Email to which mail has to be sent
                send_Email(to, content)
                speak("Email has been sent successfully! ")
            except Exception as e:
                print(e)
                speak("There was an error sending the email !")

        elif 'open website in chrome' in query:
            speak("Which website should i open ? ")
            search = takeCommand().lower()
            wb.get(chrome_path).open_new_tab(search + ".com")

        elif 'open youtube in chrome' in query:
            wb.get(chrome_path).open_new_tab('https://youtube.com')

        elif 'open google in chrome' in query:
            wb.get(chrome_path).open_new_tab('https://google.com')

        elif 'open stack overflow in chrome' in query:
            wb.get(chrome_path).open_new_tab('https://stackoverflow.com')

        elif 'search in chrome' in query:
            speak('What do you want to search for?')
            search = takeCommand()
            url = 'https://google.com/search?q=' + search
            wb.get(chrome_path).open_new_tab(url)
            speak('Here is What I found for ' + search)

        elif 'logout' in query:             # Logout from system
            os.system("shutdown -1")

        elif 'shutdown' in query:             # Shutdowns system
            os.system("shutdown /s /t 1")

        elif 'restart' in query:              # Restarts system
            os.system("shutdown /r /t 1")

        elif 'play songs' in query:
            songs_dir = 'F:/songs'                 # Path of the music directory
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[8]))  #The song number to be played

        elif 'remember that' in query:              # For this command, first make a data.txt file in the same folder where this jarvis file is stored
            speak("What should i remember ?")
            data = takeCommand()
            speak("You said me to remember : "+data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close

        elif 'do you remember anything' in query:
            remember = open('data.txt','r')
            speak("You said me to remember that "+remember.read())

        elif 'offline' in query:
            speak("Ok sir. Pleasure helping you!")
            quit()