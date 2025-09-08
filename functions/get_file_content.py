import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if os.path.commonpath([abs_working_directory, abs_file_path]) != abs_working_directory:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(abs_file_path, "r") as f:
            file_content = f.read()

        if len(file_content) > MAX_CHARS:
            file_content = file_content[:MAX_CHARS]
            file_content = file_content + f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

    except Exception as e:
        return f"Error: {e}"

    return file_content