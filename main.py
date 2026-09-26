from speech_to_text import listen
from text_to_speech import speak
from brain import think

def main():
    speak("Hello, I am Jarvis. How can I help you?")
    
    while True:
        command = listen()
        
        if command == "":
            continue
        
        if "stop" in command or "exit" in command or "goodbye" in command:
            speak("Okay, goodbye!")
            break
        
        response = think(command)
        speak(response)

if __name__ == "__main__":
    main()