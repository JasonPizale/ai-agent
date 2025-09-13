import os
from google.genai import types

def write_file(working_directory, file_path, content):
    wd = os.path.abspath(working_directory)
    target = os.path.abspath(os.path.join(wd, file_path))
    
    if os.path.commonpath([wd, target]) != wd:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    try:
        os.makedirs(os.path.dirname(target), exist_ok=True)
        with open(target, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes or overwrites a file with the provided content, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The full text content to write into the file.",
            ),
        },
        required=["file_path", "content"],
    ),
)
