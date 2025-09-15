import os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file
from functions.call_function import call_function

system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""
available_functions = types.Tool(
            function_declarations=[
                schema_get_files_info,
                schema_get_file_content,
                schema_run_python_file,
                schema_write_file,
            ]
            )

def generate_content(client, messages, verbose):
        response = client.models.generate_content(
            model="gemini-2.0-flash-001", 
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions], system_instruction=system_prompt
                )
            )
        if verbose:
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

        if response.candidates:
            for candidate in response.candidates:
                messages.append(candidate.content)

        if not response.function_calls:
            return response.text
        
        function_responses = []
        for function_call_part in response.function_calls:
            function_call_result = call_function(function_call_part, verbose=verbose)
            if verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")
            function_responses.append(function_call_result.parts[0])
        messages.append(types.Content(role="user", parts=function_responses))
        return None

def main():
    
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("error: GEMINI_API_KEY not set")
        sys.exit(1)

    client = genai.Client(api_key=api_key)

    if len(sys.argv) < 2:
        print("error: no prompt provided")
        sys.exit(1)
    else:
        verbose = "--verbose" in sys.argv[1:]
        user_prompt = " ".join(arg for arg in sys.argv[1:] if arg != "--verbose")
        if verbose:
            print(f"User prompt: {user_prompt}")

        messages = [
            types.Content(role="user", parts=[types.Part(text=user_prompt)])
        ]
        iterations = 0
        while True:
            iterations += 1

            if iterations > 20:
                print("Maximum iterations reached, exiting.")
                break

            result = generate_content(client, messages, verbose)

            if result:
                print("Final response:")
                print(result)
                break
        
if __name__ == "__main__":
    main()