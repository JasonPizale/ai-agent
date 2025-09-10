import os
def run_python_file(working_directory, file_path, args=[]):
    wd_abs = os.path.abspath(working_directory)
    target_abs = os.path.abspath(os.path.join(wd_abs, file_path))

    if not (target_abs == wd_abs or target_abs.startswith(wd_abs + os.sep)):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(target_abs):
        return f'Error: File "{file_path}" not found.'

    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.