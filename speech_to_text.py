import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening... bologe kuch?")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
            print("Processing...")
            
            text = recognizer.recognize_google(audio, language='en-IN')
            
            print(f"You said: {text}")
            return text.lower()
        
        except sr.WaitTimeoutError:
            print("Kuch suna nahi, timeout ho gaya")
            return ""
        except sr.UnknownValueError:
            print("Samajh nahi aaya, phir se boliye")
            return ""
        except sr.RequestError:
            print("Internet check karo, API tak nahi pahunch paaya")
            return ""

if __name__ == "__main__":
    result = listen()
    print(f"Final result: {result}")