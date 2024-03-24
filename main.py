#Importing openai library
import openai
import os
from openai import OpenAI

#Referencing Open AI API key
openai.api_key = "AP-KEY" # Input API key
# Link for Open AI API Key: https://platform.openai.com/api-keys


def chat_with_openai(prompt):
    response = openai.chat.completions.create(
        model ="gpt-3.5-turbo",
        messages = [{
            "role": "user", 
            "content": prompt}]
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    print("Type Exit to end the program \nAsk the AI a question.")
    while True:
        user_input = input("Me: ")
        if user_input.lower() == "exit":
            break

        response = chat_with_openai(user_input)
        print("Chatbox: ", response)

