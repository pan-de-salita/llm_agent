import argparse
import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    parsed_args = parse_args(sys.argv[1:])
    client = create_gemini_client()

    messages = [
        types.Content(role="user", parts=[types.Part(text=parsed_args.user_prompt)])
    ]
    verbose = parsed_args.verbose

    generate_contents(client, messages, verbose)


def create_gemini_client():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError("Gemini API key not configured.")

    return genai.Client(api_key=api_key)


def generate_contents(client, contents, verbose):
    model = "gemini-2.5-flash"
    generated_content = client.models.generate_content(
        model=model,
        contents=contents,
    )

    metadata = generated_content.usage_metadata
    if not metadata:
        raise RuntimeError("No usage metadata received.")

    if verbose:
        user_prompt = contents[-1].parts[-1].text
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {metadata.prompt_token_count}")
        print(f"Response tokens: {metadata.candidates_token_count}")

    print(generated_content.text)


def parse_args(args):
    parser = argparse.ArgumentParser(prog="Chatbot.")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    return parser.parse_args(args)


if __name__ == "__main__":
    main()
