from openai import OpenAI

# Initialize the OpenAI client

client = OpenAI(
    api_key='add-your-api-key',
)

# Make a request to generate completions
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a Linux instructor teaching LPI (Linux Professional Institute) Linux Essentials"},
        {"role": "user", "content": "Create a multiple choice question with 1 correct answer and 3 distractors from the objectives of the exam. Explain the correct answer."}
    ]
)

# Access the generated completion and format the output
if completion.choices:
    generated_message = completion.choices[0].message
    content = generated_message.content
    # Render new lines
    formatted_content = content.replace("\\n", "\n")

    # Print the formatted content
    print(formatted_content)
else:
    print("No completion generated.")