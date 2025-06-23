import os
import sys 
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    
  
    
    if len(sys.argv) > 1:
        prompt = sys.argv[1]
    else:
        prompt = "Prompt not provided"
        sys.exit(1)
    
    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]
    
    response = client.models.generate_content(
         model = "gemini-2.0-flash-001", 
         contents = messages)
    
    if "--verbose" in sys.argv:
        print(f"User prompt: {prompt}")
        print("Prompt tokens:" , response.usage_metadata.prompt_token_count)
        print("Response tokens:" , response.usage_metadata.candidates_token_count)
        print("Response:")
        print(response.text)
    else:
        print("Response:")
        print(response.text)
    
    




if __name__ == "__main__":
    main()