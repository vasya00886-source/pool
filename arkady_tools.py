import pyaudio
import wave
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
            p = pyaudio.PyAudio()

            stream = p.open(format=self.FORMAT,
                            channels=self.CHANNELS,
                            rate=self.RATE,
                            input=True,
                            frames_per_buffer=self.CHUNK)

            print("Слушаю...")

            frames = []

            for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
                data = stream.read(self.CHUNK)
                frames.append(data)

            print("Запись завершена")

            stream.stop_stream()
            stream.close()
            p.terminate()

            wf = wave.open(self.WAVE_OUTPUT_FILENAME, 'wb')
            wf.setnchannels(self.CHANNELS)
            wf.setsampwidth(p.get_sample_size(self.FORMAT))
            wf.setframerate(self.RATE)
            wf.writeframes(b''.join(frames))
            wf.close()

        except Exception as e:
            print(f"Ошибка при записи аудио: {e}")

    def speak(self, text):
        try:
            tts = gTTS(text=text, lang='ru')
            tts.save("output.mp3")
            os.system("start output.mp3")

        except Exception as e:
            print(f"Ошибка при воспроизведении речи: {e}")