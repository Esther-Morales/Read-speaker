from cgitb import text
from gtts import gTTS
import os


file = open("sabias.txt", "r").read().replace("\n", " ")

language = 'es-us'

speech = gTTS (text = str(file), lang= language, slow = False) 

speech.save ("texto-sabias.mp3")

os.system ("start texto-sabias.mp3")

