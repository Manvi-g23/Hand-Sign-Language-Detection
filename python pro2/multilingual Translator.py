from googletrans import Translator
import speech_recognition as sr
import pyttsx3

def translate_text(target_lang, text):
    """
    Translates text to target language.
    """
    translator = Translator()
    translation = translator.translate(text, dest=target_lang)
    return translation.text

def speak_text(text):
    """
    Speaks the provided text.
    """
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def display_language_menu():
    """
    Displays a list of available languages and their codes.
    """
    languages = {
        "en": "English",
        "fr": "French",
        "es": "Spanish",
        "de": "German",
        "it": "Italian",
        "ru": "Russian",
        "zh-CN": "Chinese",
        "ja": "Japanese",
        "ko": "Korean",
        "ar": "Arabic",
        "pt": "Portuguese",
        "nl": "Dutch",
        "hi": "Hindi"
        # Add more languages as needed
    }

    print("Available languages (Language Code):")
    for code, lang in languages.items():
        print(f"{lang} ({code})")
    print("Enter 'exit' to quit.")

def recognize_speech():
    """
    Recognizes speech input from the user.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return ""

def main():
    print("Welcome to the Language Translator!")
    speak_text("Welcome to the Language Translator!")

    display_language_menu()
    speak_text("Here are the available languages. Please choose the target language.")
    
    target_lang_choice = input("Enter the target language code (e.g., en for English): ")
    
    if target_lang_choice.lower() == 'exit':
        print("Exiting the program.")
        speak_text("Exiting the program.")
        return

    print("Do you want to enter text or speak?")
    speak_text("Do you want to enter text or speak?")
    
    choice = input("Enter 'text' or 'speak': ")

    if choice.lower() == 'text':
        text = input("Enter the text to translate: ")
    elif choice.lower() == 'speak':
        speak_text("Please speak the text you want to translate.")
        text = recognize_speech()
    else:
        print("Invalid choice. Please try again.")
        speak_text("Invalid choice. Please try again.")
        return

    languages = {
        "en": "en",
        "fr": "fr",
        "es": "es",
        "de": "de",
        "it": "it",
        "ru": "ru",
        "zh-CN": "zh-CN",
        "ja": "ja",
        "ko": "ko",
        "ar": "ar",
        "pt": "pt",
        "nl": "nl",
        "hi": "hi"
        # Add more language codes here
    }

    target_lang = languages.get(target_lang_choice)

    if target_lang:
        translated_text = translate_text(target_lang, text)
        print(f"\nTranslated text: {translated_text}")
        speak_text("Translated text is as follows.")
        speak_text(translated_text)
    else:
        print("Invalid language code. Please try again.")
        speak_text("Invalid language code. Please try again.")

if __name__ == "__main__":
    main()
