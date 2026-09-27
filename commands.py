from datetime import datetime
import webbrowser
import subprocess

def get_time():
    now = datetime.now()
    time_str = now.strftime("%I:%M %p")
    return f"The time is {time_str}"

def get_date():
    now = datetime.now()
    date_str = now.strftime("%A, %B %d, %Y")
    return f"Today is {date_str}"

def search_web(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    return f"Here are the search results for {query}"

def open_app(app_name):
    apps = {
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "paint": "mspaint.exe",
        "chrome": "chrome.exe",
        "file explorer": "explorer.exe"
    }
    
    app_name = app_name.strip().lower()
    
    if app_name in apps:
        subprocess.Popen(apps[app_name])
        return f"Opening {app_name}"
    else:
        return f"Sorry, I don't know how to open {app_name}"
