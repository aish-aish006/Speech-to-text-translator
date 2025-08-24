import speech_recognition as sr
from googletrans import Translator
from colorama import Fore, Style
from gtts import gTTS
import os

def translate_text(text, target_language):
    translator = Translator()
    translated = translator.translate(text, dest=target_language)
    return translated.text

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Speak the sentence you want to translate:")
        audio = recognizer.listen(source)
        try:
            recognized_text = recognizer.recognize_google(audio)
            return recognized_text
        except sr.UnknownValueError:
            print("❌ Sorry, I could not understand what you said.")
            return ""
        except sr.RequestError:
            print("⚠️ Sorry, could not request results. Please check your internet connection.")
            return ""

def speak_text(text, lang):
    tts = gTTS(text=text, lang=lang)
    tts.save("output.mp3")
    os.system("start output.mp3")  # On Windows, use "start"; Mac: "afplay"; Linux: "xdg-open"

if __name__ == "__main__":
    try:
        print("🎙 Speech to Text and Translation Program")
        recognized_text = speech_to_text()
        if recognized_text:
            print(f"Recognized text: {recognized_text}")
            target_language = input("Enter the target language code (e.g., 'fr' for French): ")
            translated_text = translate_text(recognized_text, target_language)
            print(f"Translated text: {Fore.GREEN}{translated_text}{Style.RESET_ALL}")

            # Speak the translation
            speak_text(translated_text, target_language)

    except Exception as e:
        print("An error occurred:", e)
