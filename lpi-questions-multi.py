from openai import OpenAI

client = OpenAI(
    api_key='add-your-api-key',
)

# Make a request to generate completions
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a Linux instructor teaching LPI (Linux Professional Institute) Linux Essentials"},
        {"role": "user", "content": '''
        Create a set of 5 sample multiple-choice questions based on the Linux Professional Institute Linux Essentials exam. 
        Each question should test knowledge of key concepts in the Linux operating system, 
        including its history,
        the basics of the Linux command line, 
        the Linux operating system's structure, 
        basic commands for navigating and working with files, 
        and an understanding of scripts. 
        Ensure each question has one correct answer and three incorrect alternatives. Cover the following topics:

1. Linux community and history
2. Basic concepts of operating systems and Linux
3. Command line basics
4. Basic commands for managing files and directories
5. Introduction to scripts and automation

Format each question as follows:

Question:
[Question Text]

A) [Option A]
B) [Option B]
C) [Option C]
D) [Option D]

Correct Answer: [Correct Option]
'''
}
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