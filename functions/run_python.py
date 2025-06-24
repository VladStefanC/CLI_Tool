import subprocess



def run_python_file(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        result = subprocess.run(
            ['python3', file_path],  # Command to run
            cwd=working_directory,   # Set working directory
            capture_output=True,     # Capture both stdout and stderr
            text=True,              # Return strings instead of bytes
            timeout=30              # 30 second timeout
        )
    except subprocess.TimeoutExpired as e :
        return f"Error: executing Python file: {e}"
    except Exception as e: 
        return f"Error: executing Python file: {e}"
    
    