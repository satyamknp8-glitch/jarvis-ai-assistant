import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def think(user_input):
    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            max_tokens=200,
            messages=[
                {"role": "system", "content": "You are Jarvis, a helpful voice assistant. Keep your answers short, clear, and conversational since they will be spoken out loud. Avoid long paragraphs, bullet points, or markdown formatting - just plain natural spoken sentences."},
                {"role": "user", "content": user_input}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error: {e}")
        return "Sorry, I am having trouble thinking right now."

if __name__ == "__main__":
    user_text = input("You: ")
    reply = think(user_text)
    print(f"Jarvis: {reply}")