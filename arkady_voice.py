import speech_recognition as sr
from gtts import gTTS
import os

class VoiceIO:
    def __init__(self):
        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100
        self.RECORD_SECONDS = 5
        self.WAVE_OUTPUT_FILENAME = "output.wav"

    def listen(self):
        try:
            recognizer = sr.Recognizer()
            with sr.Microphone() as source:
                print("Говорите...")
                audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio, language="ru-RU")
            return text
        except sr.UnknownValueError:
            print("Не удалось распознать аудио.")
            return None
        except sr.RequestError as e:
            print(f"Ошибка сервиса Google Speech Recognition; {e}")
            return None

    def speak(self, text):
        try:
            tts = gTTS(text=text, lang='ru')
            tts.save("output.mp3")
            os.system("start output.mp3")
        except Exception as e:
            print(f"Ошибка при синтезе речи; {e}")