import os
import json
from google import genai
from google.genai import types
from models import MessageAnalysis
from dotenv import load_dotenv

load_dotenv()

def analyze_message_with_llm(message: str) -> MessageAnalysis | None:
    """
    Sends the message to the Gemini API and asks it to classify the 
    message according to the MessageAnalysis schema.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable not set. Please set it in your .env file.")
    
    client = genai.Client(api_key=api_key)
    
    prompt = f"""
You are an Automated Important Message Detection Agent.
Your task is to analyze the following message and classify it according to the requested structure.

Guidelines:
Classify as IMPORTANT when it contains: urgent deadlines, financial obligations, security alerts, account problems, examinations or assignment deadlines, work-related deadlines, appointments that require attendance, important official notifications, explicit requests requiring timely action, or potentially serious consequences if ignored.
Classify as NORMAL when: it is casual conversation, greetings, ordinary social communication, has no deadline, does not require meaningful action, or is general information with no urgency.

Message to analyze:
"{message}"
"""

    try:
        chat = client.chats.create(model='gemini-3.6-flash')
        response = chat.send_message(
            prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=MessageAnalysis,
            ),
        )
        
        # Validate the response with the Pydantic model
        data = json.loads(response.text)
        return MessageAnalysis(**data)
        
    except Exception as e:
        print(f"Error during LLM classification: {e}")
        return None
