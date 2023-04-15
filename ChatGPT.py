import openai
import re
import os
from dotenv import load_dotenv

def ChatGPT_Prompt(chat_prompt, text):
    load_dotenv()

    # Setting up the OpenAI API credentials
    openai.api_key = os.getenv('OPENAI_API_KEY')

    answer = openai.Completion.create(
        #Parameters at:  https://platform.openai.com/docs/api-reference/chat/create
        model="text-davinci-003",
        prompt=f"{chat_prompt}: \n {text}",
        max_tokens = 1000,
        temperature = 0.5

    )

    result = answer
    # result = re.sub('[^0-9a-zA-Z\n\.\?,!]+', ' ', result).strip()
    return result