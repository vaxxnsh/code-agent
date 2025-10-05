import os
from config import MAX_CHARS
from google.genai import types


def get_file_content(working_directory, filepath):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, filepath))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot list "{filepath}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{filepath}"'
    
    file_content_string = ""
    try: 
        with open(abs_file_path,"r") as f:
            file_content_string = f.read(MAX_CHARS)
            
            if len(file_content_string) >= MAX_CHARS : 
                file_content_string += (
                    f'[... File {filepath} truncated at 10000 characters]'
                )
    except Exception as e:
        return f'Exception reading file: {e}'
    
    return file_content_string

schema_get_file_content = types.FunctionDeclaration(
    name = "get_file_content",
    description="Get the content of the given file as a string , constrined to the working directory ",
    parameters = types.Schema(
        type= types.Type.OBJECT,
        properties ={
            "file_path":types.Schema(
                type= types.Type.STRING,
                description= "The path to the file, from the working directory. If not provided, lists files in the directory itself. ",
            ),
        },
    ),
)    