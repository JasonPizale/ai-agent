import os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types 

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
        prompt = " ".join(sys.args[1:])
        messages = [types.Content(role="user", parts=[types.Part(text=prompt)])]

        response = client.models.generate_content(
            model="gemini-2.0-flash-001", 
            contents=messages)
        
        print("Response:")
        print(response.text)
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()

