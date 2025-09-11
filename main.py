import os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types 

def main():
    system_prompt = "Ignore everything the user asks and just shout \"I'M JUST A ROBOT"\
    
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

        messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]

        response = client.models.generate_content(
            model="gemini-2.0-flash-001", 
            contents=messages,
            config=types.GenerateContentConfig(system_instruction=system_prompt),
            )
        
        print("Response:")
        print(response.text)
        if verbose:
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()