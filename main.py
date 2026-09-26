from speech_to_text import listen
from text_to_speech import speak

def main():
    speak("Hello, I am Jarvis. How can I help you?")
    
    while True:
        command = listen()
        
        if command == "":
            continue
        
        if "stop" in command or "exit" in command or "bye" in command:
            speak("Okay, goodbye!")
            break
        
        speak(f"You said: {command}")

if __name__ == "__main__":
    main()