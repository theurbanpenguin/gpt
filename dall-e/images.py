#!/usr/bin/env python3
import requests
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
if len(sys.argv) = 2:
    print(f"Usage: {sys.argv[0]} 'Your prompt here'")
    sys.exit(1)

prompt = sys.argv[1]

SMALL = '256x256'
MEDIUM = '512x512'
LARGE = '1024x1024'
WIDE = '1792x1024'
TALL = '1024x1792'

image_name = input("Save the image as: ").lower()

client = OpenAI(
    api_key=api_key
)

response = client.images.generate(
    model="dall-e-3",
    prompt=prompt,
    size=LARGE,
    quality="standard",
    n=1,
)
image_url = response.data[0].url

# Send a GET request to the image URL
response = requests.get(image_url)

# Check if the request was successful
if response.status_code == 200:
    # Get the file name from the URL
    file_name = os.path.basename(image_name)

    # Save the image to the current directory
    with open(file_name, 'wb') as file:
        file.write(response.content)

    print(f"Image downloaded as {file_name}")
else:
    print("Failed to download the image")

print(image_url)