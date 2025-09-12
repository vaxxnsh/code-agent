import os

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.join(abs_working_dir, file_path)
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_file_path):
        parent_dir = os.path.dirname(abs_file_path)
        print(parent_dir)
        try:
            if not os.path.isdir(parent_dir):
                os.makedirs(parent_dir)
            
        except Exception as e:
            return f"Error: Could not create parent dirs {e}"
        
    try:
        with open(abs_file_path,"w") as f:
            f.write(content)
            
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'