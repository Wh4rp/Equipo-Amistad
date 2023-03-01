import openai


def reviser(question):
    openai.api_key = "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"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"The following is a conversation with an AI assistant. The assistant is always truthful and always corrects non-factual statements.\n\nHuman: Hey! Did you know that the sun is a planet??\nAI:  No, that's incorrect. The sun is a star, not a planet.\nHuman:{question}\nAI:",
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text.strip()


if __name__ == "__main__":
    print(reviser("Did you know that the Mayan civilization began in the 20th century?"))
