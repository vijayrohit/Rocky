import requests
from lxml import html
from bs4 import BeautifulSoup
from gtts import gTTS
import os
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
		#engine.setProperty('volume',1.0)
rate = engine.getProperty('rate')   # getting details of current speaking rate
#print (rate)                        #printing current voice rate
engine.setProperty('rate', 135)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
#print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[0].id)   #changing index, changes voices. 1 for female

def assistant(command):
	if 'hey' in command:
		engine.say("Hi! Mister Pantam. How is your day going so far?")
		engine.runAndWait()

	if 'fairway' in command:
		

		page = requests.get('https://usfbullrunner.com/simple/routes/13928/stops/95777')
		#

		soup = BeautifulSoup(page.content, 'html.parser')

		results = soup.findAll('ul')

		li = []
		for i in results:
			li.append(i.text)
		#print(li[1].split('\n')[1])


		page = requests.get('https://usfbullrunner.com/simple/routes/12905/stops/95777')
		#

		soup = BeautifulSoup(page.content, 'html.parser')

		results = soup.findAll('ul')
		lic = []
		for i in results:
			lic.append(i.text)

		engine.say("Mister Pantam, Route A "+li[1].split('\n')[1]+"and, Route C "+lic[1].split('\n')[1])
		engine.runAndWait()
	if 'station 42' in command:
		page = requests.get('https://usfbullrunner.com/simple/routes/13928/stops/95798')
		#

		soup = BeautifulSoup(page.content, 'html.parser')

		results = soup.findAll('ul')

		li = []
		for i in results:
			li.append(i.text)
		#print(li[1].split('\n')[1])


		page = requests.get('https://usfbullrunner.com/simple/routes/12905/stops/95798')
		#

		soup = BeautifulSoup(page.content, 'html.parser')

		results = soup.findAll('ul')
		lic = []
		for i in results:
			lic.append(i.text)

		engine.say("Mister Pantam, Route A "+li[1].split('\n')[1]+"and, Route C "+lic[1].split('\n')[1]+"at Cambridgewood Drive")
		engine.runAndWait()
	if 'station 42' not in command and 'hey' not in command and 'fairway' not in command:
		engine.say("Sorry! I didn't get you. Please try again, and Is Mister Pantam around? He might help you as well.")
		engine.runAndWait()
def myCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Say something...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')
    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('....')
        command = myCommand();
    return command


page = requests.get('https://usfbullrunner.com/simple/routes')
		#

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.findAll('li')
lic = []
for i in results:
	lic.append(i.text)
print(lic)