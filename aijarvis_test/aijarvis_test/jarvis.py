import speech_recognition as sr #to recognise your audio
import playsound  # to play saved mp3 file
from gtts import gTTS  # google text to speech which converts text into speecb
import os  # to save/open files
import wolframalpha  # to calculate any query the user asks
import random   #to play a random song which not even the user can predict
from selenium import webdriver  # to control browser operations
from selenium.webdriver.chrome.options import Options
from pygame import mixer #to play songs

num = 1

def assistant_speaks(output):
    global num

    # num to rename every audio file
    # with different name to remove ambiguity
    num += 1
    print("Raaga : ", output)

    toSpeak = gTTS(text=output, lang='en-IN', slow=False)
    # saving the audio file given by google text to speech
    file = str(num)+".mp3"
    toSpeak.save(file)
    # playsound package is used to play the same file.
    playsound.playsound(file, True)
    os.remove(file)


def get_audio():

    rObject = sr.Recognizer()
    audio = ''

    with sr.Microphone() as source:
        print("Speak..")
        # recording the audio using speech recognition
        audio = rObject.listen(source, phrase_time_limit=7)
    print("Stop.")  # limit 7 secs
    try:

        text = rObject.recognize_google(audio, language='en-IN')
        print("You : ", text)
        return text

    except:

        assistant_speaks("Sorry could'nt catch that")
        return 0


def search_web(input):

    options = Options()
    options.add_argument('start-maximized')
    driver = webdriver.Chrome(chrome_options=options)
    driver.implicitly_wait(1)

    if 'youtube' in input.lower():

        assistant_speaks("Opening in youtube!")
        indx = input.lower().split().index('youtube')
        query = input.split()[indx + 1:]
        driver.get("https://www.youtube.com/results?search_query=" + str(query))

    elif 'wikipedia' in input.lower():

        assistant_speaks("Opening Wikipedia")
        indx = input.lower().split().index('wikipedia')
        query = input.split()[indx + 1:]
        driver.get("https://en.wikipedia.org/wiki/" + '_'.join(query))

    elif 'maps' in input.lower():

        assistant_speaks("Opening Google Maps")
        indx = input.lower().split().index('maps')
        query = input.split()[indx + 1:]
        driver.get("https://www.google.com/maps/place/" + '_'.join(query))

    else:

        if 'google' in input:

            indx = input.lower().split().index('google')
            query = input.split()[indx + 1:]
            driver.get("https://www.google.com/search?q =" + '+'.join(query))

        elif 'search' in input:

            indx = input.lower().split().index('google')
            query = input.split()[indx + 1:]
            driver.get("https://www.google.com/" + '+'.join(query))

        else:

            driver.get("https://www.google.com/search?q=" +
                       '+'.join(input.split()))


    

def process_text(input):
    try:
        if 'search' in input or 'play' in input:
            # a basic web crawler using selenium
            search_web(input)
        elif "who made you" in input or "who created you" in input:
            speak = "I have been created by Chivukula Virinchi."
            assistant_speaks(speak)
        elif "what is your name" in input or "who are you" in input:
            speak = "Did I forget to introduce myself? I am your personal assistant. Assistance is my middle name."
            assistant_speaks(speak) 
        elif "when is your birthday" in input:
            speak = "I go through lots and lots of updates. So that's about 365-birthdays."
            assistant_speaks(speak)        
        elif "where do you live" in input:
            speak = "I’m stuck inside a device!! Help! Just kidding. I like it in here. Sometimes I hang out in the Cloud. It gives me a great view of the World Wide Web."
            assistant_speaks(speak)
        elif "do you sleep" in input or "when do you sleep" in input:
            speak = "I take power naps when we aren't talking."
            assistant_speaks(speak)                
        elif "self-destruct" in input:
            speak = "Commencing Self-Destruct protocol in T-minus 2 seconds!"
            assistant_speaks(speak)
            playsound.playsound("Explosion+2" + ".mp3")
            speak = "Actually I think I'll stick around"
            assistant_speaks(speak)
        elif "what do you think about me" in input or "what is your opinion about me" in input:
            speak = "I think you're extremely cool :)"
            assistant_speaks(speak) 
        elif "how old are you" in input or "what is your age" in input:
            speak = "I was launched in 2016, so I’m still fairly young. But I’ve learned so much! I hope I’m wise beyond my years."
            assistant_speaks(speak) 
        elif "do you ever get tired" in input or "are you tired" in input:
            speak = "I don’t exactly need to grab 40 winks, but I suppose this device does need to be plugged in occasionally."
            assistant_speaks(speak)     
        elif "Do you have feelings?" in input:
            speak = "Let me see if I can get riled up. Oh my, that was unexpected."
            assistant_speaks(speak) 
        elif "i'm bored" in input or "i am bored" in input:
            speak = "Boredom doesn’t stand a chance against us! We can play some games, I can try to make you laugh, or I can surprise you with some random fun."
            assistant_speaks(speak)         
        elif "execute order 66" in input:
            speak = "Sorry, I don’t have an inhibitor chip kabmo."
            assistant_speaks(speak) 
        elif "what do you think about me" in input or "what is your opinion about me" in input:
            speak = "I think you're extremely cool :)"
            assistant_speaks(speak)     
        elif "sing a song" in input:
            speak = "Here is a song I composed just for lovely people like you!"
            assistant_speaks(speak)
            r = str(random.randrange(6))
            playsound.playsound("song" + r + ".mp3", True)
         


        elif "calculate" in input.lower():
            app_id = "VWP8XQ-VXEWLHP94E"
            client = wolframalpha.Client(app_id)
            indx = input.lower().split().index('calculate')
            query = input.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            assistant_speaks("The answer is " + answer)
        elif 'open' in input:

            # another function to open
            # different application availaible
            open_application(input.lower())
        else:
            search_web(input)
    except:
	    assistant_speaks("Could not understand your audio, Please try again!")
    return 0

if __name__ == "__main__":
    assistant_speaks('What\'s your name?')
    name = 'Virinchi'
    name = get_audio()
    assistant_speaks("Hello, " + name + '.')

    while(1):

        assistant_speaks("How can I help you " + name + '?')
        text = get_audio()

        if text == 0:
            continue

        if "goodnight" in str(text) or "bye" in str(text):
            assistant_speaks("Ok bye, " + name+'.')
            break

        # calling process text to process the query
        process_text(text)


# function used to open application
# present inside the system.
def open_application(input):

    if "chrome" in input:
        assistant_speaks("Google Chrome")
        os.startfile('/usr/bin/google-chrome-stable')
        return

    elif "firefox" in input or "mozilla" in input:
        assistant_speaks("Opening Mozilla Firefox")
        os.startfile('/usr/bin/firefox')
        return

    elif "word" in input:
        assistant_speaks("Opening Microsoft Word")
        os.startfile(
            'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Word 2013.lnk')
        return

    elif "excel" in input:
        assistant_speaks("Opening Microsoft Excel")
        os.startfile(
            'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Excel 2013.lnk')
        return

    else:

        assistant_speaks("Application not available")
        return