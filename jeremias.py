#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

# AIML
import gtts

#RECONHECIMENTO DE VOZ
import speech_recognition as sr
import pyaudio

#AUDIO
from playsound import playsound


def speak(mytext):
	language = 'pt'
	tts = gtts.gTTS(text=mytext, lang=language, slow=False)
	tts.save("fala.mp3")
	os.system("mpg123 -q fala.mp3") 

# pega o audio do microfone
recognizer = sr.Recognizer()
mensagem = ''
audioMensagem = ''
pesquisa = ''
audioPesquisa = ''


while True:
	with sr.Microphone() as source:
		try:
#			playsound('./wav/voice_start.wav')
#			print("\nDiga algo!")
			audioMensagem = recognizer.listen(source)
			mensagem = recognizer.recognize_google(audioMensagem, language="pt-BR" )
#			print("Você falou: " + mensagem)
#			playsound('./wav/voice_stop.wav')
		except:
			mensagem = ""
			pass

	with sr.Microphone() as source1:

		if mensagem == "pesquisa":
			try:
				print("Pesquisar: ")
				playsound('./wav/voice_start.wav')
				audioPesquisa = recognizer.listen(source1)
				pesquisa = (recognizer.recognize_google(audioPesquisa, language="pt-BR" ))
				print(pesquisa)
				playsound('./wav/voice_stop.wav')
				os.system("./pesquisa.bash "+pesquisa)
			except:
				print("Resultado não encontrado.")







