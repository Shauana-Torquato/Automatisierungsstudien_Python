import pyautogui as pa
import time
import pyperclip
"""import speech_recognition as sr
from pyttsx3 import init"""

pa.PAUSE = 1
'''engine = init()'''

"""def transcript_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Starting the transcription")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language = 'pt-BR')
            return text
        except sr.UnknownValueError:
            print("Not possible to understand this audio")
            return ""

def save_text_file(text):
    with open ("transcription.txt","w", encoding="utf-8") as file:
        file.write(text)
    print("File saved as transcription.txt")

def main():"""

pa.press("win")
pa.write("chrome")
pa.press("ENTER")
pa.sleep(2)
pa.click(x=1002, y=629)
pa.sleep(2)
pa.write("youtube.com")
pa.press("ENTER")
pa.sleep(5)
pa.click(x=458, y=153)
pyperclip.copy("palavras mais importantes em alemão")
pa.hotkey('ctrl','v')
pa.press("ENTER")
pa.sleep(5)
pa.click(x=547, y=571)

"""text = transcript_audio()
    save_text_file(text)

    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    main()"""





