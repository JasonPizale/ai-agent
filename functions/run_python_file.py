import os
import sys
import subprocess
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