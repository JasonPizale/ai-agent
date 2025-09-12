import os
from google.genai import types

def get_files_info(working_directory, directory="."):
    abs_work = os.path.abspath(working_directory)
    abs_target = os.path.abspath(os.path.join(working_directory, directory))

    if not (abs_target == abs_work or abs_target.startswith(abs_work + os.sep)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(abs_target):
        return f'Error: "{directory}" is not a directory'

    try:
        entries = sorted(os.listdir(abs_target))
        lines = []
        for name in entries:
            path = os.path.join(abs_target, name)
            try:
                size = os.path.getsize(path)
                is_dir = os.path.isdir(path)
                lines.append(f"- {name}: file_size={size} bytes, is_dir={str(is_dir)}")
            except Exception as e:
                lines.append(f"- {name}: Error: {e}")
        return "\n".join(lines)
    except Exception as e:
        return f"Error: {e}"

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
