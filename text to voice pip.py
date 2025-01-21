# pip install pyttsx3 (text to speech conversion library)
import pyttsx3 # type: ignore
engine = pyttsx3.init()
engine.say("Hello, World! I am Prthvish Raj Shukla.")
engine.runAndWait()
