import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia

engine = pyttsx3.init('sapiS')
voices = engine.getProperty('voices') 
print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
     engine.say(audio)
     engine.runAndWait()


def wishMe():
hour = int(datetime.datetime.now().hour)
if hour>=0 and hour<=12
   speak("Good morning")
elif hour>=12 and hour<=18
   speak("Good Afternoon")
elif hour>=18 and hour<=20
   speak("Good evening")
else
   speak("Good night")

speak("I am Jira Mam. Please tell me how may I help you")

def takeCommand():

   r= st.Recognizer()
    with sr.Microphone() as source:
    print("Listening...")
    r.pause_threshold = 1
    audio = r.listen(source)

   try:
        print("Recognizing...")
        query = r.recognize_google(audio,Language='en-in')
        print(f"User said:{query}\n")

   except Exception as e:
        print("Say that again please...")
        return "None"
   return query

if __name__ == "__main__":
    wishMe()
    while True:
    query = takeCommand().lower()

     #Logic for executing tasks based on query
     if 'wikipedia' in query:
         speak('Searching Wikipedia...')
         query = query.replace("wikipedia", "")
         results = wikipedia.summary(query,sentences=1)
         speak("According to wikipedia")
         print(results)
         speak(results)

     elif 'open youtube' in query:
        webbrowser.open("youtube.com")
       
     elif 'open google' in query:
        webbrowser.open("google.com")     

     elif 'open stackoverflow' in query:
        webbrowser.open("google.com")
     
     elif 'play music' in query:
        music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[0]))
       
     elif 'the time' in query:
          strTime = datetime.datetime.now().strftime("%H:%M:%S")
          speak(f"Mam, the time is {strTime}")

     elif 'open code' in query:
          codePath = "C:\\Users\\Nikita kushwaha\\AppData\\Local\\Programs\\Microsof Vs Code\\Code.exe"
          os.startfile(codePath)