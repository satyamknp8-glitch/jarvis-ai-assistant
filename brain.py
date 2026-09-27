import os
from dotenv import load_dotenv
from google import genai
from tavily import TavilyClient

load_dotenv()

client_gemini = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def needs_search(user_input):
    keywords = ["latest", "current", "today", "2025", "2026", "recent", "news", "who won", "winner"]
    return any(keyword in user_input.lower() for keyword in keywords)

def think(user_input):
    try:
        context = ""
        
        if needs_search(user_input):
            search_results = tavily_client.search(user_input, max_results=3)
            context = "\n".join([r["content"] for r in search_results["results"]])
        
        system_prompt = "You are Jarvis, a helpful voice assistant. Keep your answers short, clear, and conversational since they will be spoken out loud. Avoid long paragraphs, bullet points, or markdown formatting - just plain natural spoken sentences."
        
        if context:
            system_prompt += f"\n\nUse this recent information to answer the question if relevant:\n{context}"
        
        full_prompt = f"{system_prompt}\n\nUser: {user_input}"
        
        response = client_gemini.models.generate_content(
            model="gemini-3.8-flash",
            contents=full_prompt
        )
        return response.text
    except Exception as e:
        print(f"Error: {e}")
        return "Sorry, I am having trouble thinking right now."

if __name__ == "__main__":
    user_text = input("You: ")
    reply = think(user_text)
    print(f"Jarvis: {reply}")