# Made on 11/23/2023 7:22 PM
# Uses OpenAI's Chatgpt API to create prompts for 5 different types of vintage art pieces to generate with DALL-E. I made this project to learn how to use API's so that I could make my own voice activated Engineering AI assistant, and to start a Etsy business selling AI Vintage art. 

import openai


api_key = 'API-KEY-HERE'  # Replace with your actual OpenAI API key
openai.api_key = api_key

# Define a prompt to generate descriptions of vintage art pieces using ChatGPT
chat_prompt = (
    "Generate descriptions for vintage art pieces that DALL·E can create:\n"
    "1. Generate a description of a vintage postcard depicting a serene countryside scene with an old windmill.\n"
    "2. Describe a retro-style painting of a bustling marketplace with vibrant colors and people.\n"
    "3. Provide a description for an antique portrait of a mysterious figure wearing a top hat and holding a pocket watch.\n"
    "4. Create a description for a weathered, sepia-toned photograph of an ancient library filled with books.\n"
    "5. Describe a faded, nostalgic image of a classic car driving down a tree-lined road at sunset.\n"
)

# Generate prompts using ChatGPT
response = openai.ChatCompletion.create(
    model="text-davinci-003",
    messages=[
        {"role": "system", "content": chat_prompt},
        {"role": "user", "content": "Generate vintage art pieces."},
    ],
    temperature=0.7,
    max_tokens=150,
)

# Display generated prompts
print("Prompts for DALL·E to create vintage art pieces:")
for idx, message in enumerate(response['choices'][0]['message']['content'].split("\n")):
    print(f"{idx + 1}. {message}")