from speech_to_text import listen
from text_to_speech import speak
from brain import think
from commands import get_time, get_date, open_app

def main():
    speak("Hello, I am Jarvis. How can I help you?")
    
    while True:
        command = listen()
        
        if command == "":
            continue
        
        if "stop" in command or "exit" in command or "goodbye" in command:
            speak("Okay, goodbye!")
            break
        
        elif "time" in command:
            response = get_time()
            speak(response)
        
        elif "date" in command:
            response = get_date()
            speak(response)
        
        elif "open" in command:
            app_name = command.replace("open", "").strip()
            response = open_app(app_name)
            speak(response)
        
        else:
            response = think(command)
            speak(response)

if __name__ == "__main__":
    main()