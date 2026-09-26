import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # David - English male voice
    engine.setProperty('rate', 175)
    engine.setProperty('volume', 1.0)
    
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Hello, I am your assistant. Test successful.")