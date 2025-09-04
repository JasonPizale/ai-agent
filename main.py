import os, sys
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def main():
    if len(sys.argv) < 2:
        print("error: no prompt provided")
        sys.exit(1)
    else:
        args = sys.argv[1:]
        prompt = " ".join(args)
        response = client.models.generate_content(model="gemini-2.0-flash-001", contents=prompt
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()

