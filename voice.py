from pathlib import Path
import openai

# Set the OpenAI API key from the OPENAI_API_KEY environment variable
openai.api_key = 'add-your-api-key'

# Ensure the API key is not None or empty before proceeding
if not openai.api_key:
    raise ValueError("The OPENAI_API_KEY environment variable is not set.")

speech_file_path = Path(__file__).parent / "speech.mp3"

response = openai.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input="The quick brown fox jumped over the lazy dog."
)

response.stream_to_file(speech_file_path)

