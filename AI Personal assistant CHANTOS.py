#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install SpeechRecognition 


# In[2]:


pip install PyAudio


# In[3]:


pip install pyttsx3


# import speech_recognition as sr
# import pyttsx3
# import webbrowser
# import datetime
# import time
# 
# def greeting():
#     hour = datetime.datetime.now().hour
#     if hour >= 0 and hour < 12:
#         speak("Hello , Good morning")
#         print("Hello , Good morning")
#     elif hour >= 12 and hour < 15:
#         speak("Hello , Good afternoon")
#         print("Hello , Good afternoon")
#     else :
#         speak("Hello , Good evening")
#         print("Hello , Good evening")
# 
# def speak(text):
#     engine.say(text)
#     engine.runAndWait()
# 
# def takeCommand():
#     with sr.Microphone() as source:
#         recognizerObject.adjust_for_ambient_noise(source)
#         print("Listening.....")
#         voice = recognizerObject.listen(source, timeout = 5)
#         try:
#             statement = recognizerObject.recognize_google(voice)
#             print("Got it")
#             print("User said:"+statement)
#         except Exception as e :
#             print("Pardon me,please say it agian")
#             speak("Pardon me,please say it agian")
#             return "None"
#         return statement
# 
# recognizerObject = sr.Recognizer()
# engine = pyttsx3.init()
# 
# print("Loading your AI Personal Assistant - CHANTOS")
# speak("Loading your AI Personal Assistant - CHANTOS")
# 
# greeting()
# 
# while True :
#     print("I'm ready to service. How can I help you?")
#     speak("I'm ready to service. How can I help you?")
#     
#     statement = takeCommand().lower()
#     
#     if statement == "None":
#         continue
#     if "goodbye" in statement or "stop" in statement or "bye" in statement :
#         print("your AI Personal assistant CHANTOS is shutting, good bye")
#         speak("your AI Personal assistant CHANTOS is shutting, good bye")
#         break
#     if "youtube" in statement :
#         webbrowser.open_new_tab("https://www.youtube.com/")
#         speak("Youtube is open now")
#     elif "google" in statement :
#         webbrowser.open_new_tab("https://www.google.com")
#         speak("Google is open now")
#     elif "time" in statement :
#         strTime = datetime.datetime.now().strftime("%H:%M:%S")
#         speak("The time is"+strTime)
#     elif "how are you" in statement :
#         speak("I'm doing great. I wish I can serve you best as your AI personal assistant")
#     elif "instagram" in statement :
#         webbrowser.open_new_tab("https://www.instagram.com")
#         speak("IG is open now")
#     time.sleep(3)
