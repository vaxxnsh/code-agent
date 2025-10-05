import os
from google.genai import types

def run_python_file(working_directory : str,file_path : str, args = []):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a python file.'
    

    try:
        final_args = ["python3", file_path]
        final_args.extend(args)
        output = subprocess.run(
            final_args,
            cwd = abs_working_dir,
            timeout = 30,
            captrure_output= True
        )
        final_string = f"""
STDOUT:{output.stdout}
STDERR: {output.stderr}
"""
        if output.stdout == "" and output.stderr == "":
            final_string = "No output produced.\n"
        if output.returncode != 0:
            final_string += f"Process exited with hcode {output.returncode}"            
        return output
    except Exception as e:
        return f"Error: executing Python file: {e}"

schema_run_python_file = types.FunctionDeclaration(
    name = "get_files_info",
    description="Run a python file with the python3 interpreter, Accepts additionl CLI args as optional array ",
    parameters = types.Schema(
        type= types.Type.OBJECT,
        properties ={
            "file_path":types.Schema(
                type= types.Type.STRING,
                description= "If file to run, relative to the working directory. If not provided,  ",
            ),
            "args":types.Schema(
                type= types.Type.ARRAY,
                description="An optional array of string to be used  as the , relative to the working directory",
                items=types.Schema(
                    type=types.Type.STRING,
                )
            ),
        },
    ),
)        
