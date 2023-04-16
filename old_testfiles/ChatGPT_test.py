from ChatGPT import ChatGPT_Prompt

def main():

    chat_gpt_promt = "Tell me a story about"
    text = "A dog"

    # If we're taking the route of splitting by sentence, I think it would be a good idea
    # to ask ChatGPT in the background to first fix any grammar issues, add any missing 
    # punctuation, etc before splitting the text into sentences. This also might be where 
    # we add markers or something to differentiate the title, bosy and comments of the post -ben

    # Looking something like (left out markers becuase IDK the output of the reddit scraper):
    # chat_gpt_prompt = "Text from the post"
    # text = "Please fix any spelling, grammar, or punctuation issues."

    results = ChatGPT_Prompt(chat_gpt_promt, text)
    print(results)

if __name__ == "__main__":
    main()