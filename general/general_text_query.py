#!/usr/bin/env python3

import sys
import os
from openai import OpenAI

# Check if an API key is set as an environment variable
try:
    api_key = os.environ['OPENAI_API_KEY']
except KeyError:
    print("Error: The OPENAI_API_KEY environment variable is not set.")
    sys.exit(1)

# Check if a prompt was provided as a command-line argument
if len(sys.argv) < 2:
    print("Usage: python script_name.py 'Your prompt here'")
    sys.exit(1)

prompt = sys.argv[1]  # The prompt is the first argument passed to the script

try:
    # Initialize the OpenAI client with the API key from the environment variable
    client = OpenAI(api_key=api_key)

    # Make a request to generate completions using the provided prompt
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    # Access the generated completion and format the output
    if completion.choices:
        generated_message = completion.choices[0].message
        content = generated_message.content
        # Render new lines
        formatted_content = content.replace("\\n", "\n")
        print(formatted_content)
    else:
        print("No completion generated.")
except Exception as e:
    print(f"An error occurred: {e}")