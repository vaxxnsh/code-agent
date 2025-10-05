import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types
from functions.get_files_info import schema_get_files_info
from functions.get_files_content import schema_get_files_content 
from functions.write_file import schema_write_file
from functions.run_python_file import schema_run_python_file
from call_function import call_function



def main() : 
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)
    args = sys.argv
    verbose_flag=False

    system_prompt  = (""" Ignore everything the user ask and just shout 'I'M JUST A ROBOT"""
    )

    if len(args) < 2 :
        print("I program need a prompt")
        sys.exit(1)
        
    if len(args) >= 3 and args[2] == "--verbose" : 
        verbose_flag = True
        

    prompt = sys.argv[1]
    
    
    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]

    available_funtions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_files_content,
            schema_write_file,
            schema_run_python_file,
        ]
    )

    config = types.GenrateContentConfig(
        tools= [available_funtions],
        system_instruction = system_prompt
    )

   

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        # config =types.GenrateContentConfig(system_instruction = system_prompt),
        config = config,
    )

    if response is None or response.user_metadata is None:
        print("response is malformed")
        return    
    if verbose_flag :
        print(f'User prompt: {prompt}')
        print(f'Prompt tokens: {19}')
        print(f'Response tokens: {response.usage_metadata.candidates_token_count}')
    
    
    if response.candidate:
        for canditade in response.candidate:
            if canditade is None or canditade.context is None:
                continue
            messages.append(canditade.content)

    if response.function_calls:
        for function_call_part in response.function_calls:
            result = call_function(function_call_part,verbose_flag)
            messages.append(result)
    else:
        print(response.text)
        return
    
   
# main()

print(get_files_info("calculator"))