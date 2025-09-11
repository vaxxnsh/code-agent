import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types



def main() : 
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)
    args = sys.argv
    verbose_flag=False

    if len(args) < 2 :
        print("I program need a prompt")
        sys.exit(1)
        
    if len(args) >= 3 and args[2] == "--verbose" : 
        verbose_flag = True
        

    prompt = sys.argv[1]
    
    
    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]


    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
    )

    if verbose_flag :
        print(f'User prompt: {prompt}')
        print(f'Prompt tokens: {19}')
        print(f'Response tokens: {response.usage_metadata.candidates_token_count}')
    
main()