import os


def get_files_info(working_dir,dir = None) : 
    abs_working_dir : str = os.path.abspath(working_dir)
    
    if dir == None : 
        dir = abs_working_dir
    else:
        dir = os.path.join(abs_working_dir,dir)
    
    abs_dir = os.path.abspath(dir)
    
    print(abs_working_dir)
    print(abs_dir)
    
    if not abs_dir.startswith(abs_working_dir):
        return f'Error "{dir}" is not a directory'
    
    contents = os.listdir(abs_dir)
    final_resp = """"""
    
    for content in contents:
        content_path = os.path.join(abs_dir,content)
        is_dir = os.path.isdir(content_path)
        size = os.path.getsize(content_path)
        final_resp += f"- {content}: file_size={size} bytes, is_dir={is_dir}\n"
    return final_resp
        
        