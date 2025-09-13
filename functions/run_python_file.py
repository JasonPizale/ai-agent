import os
import sys
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    wd_abs = os.path.abspath(working_directory)
    target_abs = os.path.abspath(os.path.join(wd_abs, file_path))

    if not (target_abs == wd_abs or target_abs.startswith(wd_abs + os.sep)):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(target_abs):
        return f'Error: File "{file_path}" not found.'

    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
            completed = subprocess.run(
                [sys.executable, target_abs, *args],
                cwd=wd_abs,
                capture_output=True,
                text=True,
                timeout=30,
            )
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
    stdout = (completed.stdout or "").strip()
    stderr = (completed.stderr or "").strip()

    if not stdout and not stderr:
        return "No output produced."

    lines = [f"STDOUT: {stdout}", f"STDERR: {stderr}"]
    if completed.returncode != 0:
        lines.append(f"Process exited with code {completed.returncode}")
    return "\n".join(lines)

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file with optional CLI-style string arguments.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="Optional list of string arguments to pass to the script.",
                items=types.Schema(type=types.Type.STRING),
            ),
        },
        required=["file_path"],
    ),
)