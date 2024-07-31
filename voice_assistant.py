#!/usr/bin/env python
# coding: utf-8

# In[1]:


#get_ipython().system('pip install SpeechRecognition pyttsx3 wikipedia')

# In[2]:


import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia

# In[3]:


engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


# In[4]:


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-US')
            print(f"User said: {query}")
        except Exception as e:
            print("Sorry, I did not understand that.")
            speak("Sorry, I did not understand that.")
            return None
    return query


# In[5]:


def respond_to_greeting():
    speak("Hello! How can I assist you today?")


# In[6]:


def tell_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    speak(f"The current time is {current_time}")


# In[7]:


def tell_date():
    today = datetime.date.today()
    speak(f"Today's date is {today}")


# In[9]:


def search_wikipedia(query):
    try:
        results = wikipedia.summary(query, sentences=2)
        speak(f"According to Wikipedia, {results}")
    except Exception as e:
        speak("Sorry, I couldn't find any information on that topic.")


# In[10]:


def handle_command(command):
    if command:
        command = command.lower()
        if 'hello' in command:
            respond_to_greeting()
        elif 'time' in command:
            tell_time()
        elif 'date' in command:
            tell_date()
        elif 'search for' in command:
            query = command.replace('search for', '').strip()
            search_wikipedia(query)
        else:
            speak("Sorry, I don't know how to help with that.")


# In[ ]:


if __name__ == "__main__":
    speak("Initializing voice assistant...")
    while True:
        command = listen()
        handle_command(command)

# In[ ]:
