from ChatGPT import ChatGPT_Prompt

def main():

    chat_gpt_promt = "Tell me a story about"
    text = "A dog"

    results = ChatGPT_Prompt(chat_gpt_promt, text)
    print(results)

if __name__ == "__main__":
    main()