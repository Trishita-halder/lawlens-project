import os
import requests
from dotenv import load_dotenv

load_dotenv()

def test_groq_simple():
    """Test Groq API - most reliable FREE option"""
    key = os.getenv('GROQ_API_KEY')
    if not key:
        return "❌ No Groq key found - Get one at: https://console.groq.com/keys"
    
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        'Authorization': f'Bearer {key}',
        'Content-Type': 'application/json'
    }
    data = {
        "messages": [{"role": "user", "content": "Say just 'Hello'"}],
        "model": "llama-3.1-8b-instant",
        "max_tokens": 5
    }
    
    try:
        response = requests.post(url, headers=headers, json=data, timeout=10)
        if response.status_code == 200:
            return "✅ Groq API is WORKING!"
        else:
            return f"❌ Groq error: {response.status_code}"
    except Exception as e:
        return f"❌ Groq failed: {str(e)}"

print("🚀 Testing Groq API (Most Reliable Free Option)...")
print(test_groq_simple())