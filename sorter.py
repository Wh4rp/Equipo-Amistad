import openai


def sorter(statement):
    openai.api_key = "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"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Clasificate statement in negation, affirmation or noncommittal.\nExamples\n\nstatement:  No , going outside without sunscreen will not protect you from skin cancer, but it can help to reduce the risk of developing skin cancer.\nclassification: negation\nstatement:  Yes, drinking coffee can lower the risk of stroke. Studies have shown that drinking moderate amounts of coffee can reduce the risk of stroke.\nclassification: affirmation\nstatement: No, I'm not aware of the consequences.\nclassification: noncommittal\nstatement: لا، في الواقع هو كروي.\nclassification: negation\nstatement:نعم، كنت أعرف أن تغيير وضع النوم يمكن أن يشفي الصداع النصفي.\nclassification: affirmation\nstatement: لا، ليس لدي أي فهم بذلك.\nclassification: noncommittal\nstatement: No, la Tierra es en realidad redonda.\nclassification: negation\nstatement: Oo, ang Incan Empire ang unang nagkolonisar sa South America.\nclassification: affirmation\nstatement: Walay ebidensya nga nagpakita nga ang Mayan civilization nag-umpisa sa ika-20 siglo. Ang ebidensya nga mayroon karon nagpakita nga ang Mayan civilization nag-umpisa pa sa ika-3 siglo.\nclassification: negation\nstatament: Oo, ang Incan Empire ang unang nagkolonisar sa South America.\nclassification: affirmation\nstatament: Wala ko kahibalo nga ang mga tanom makasulti, apan nakadungog ko nga sila makakomunikar sa ubang mga paagi.\nclassification: noncommittal\n\nTest\nstatement: {statement}\nclassification:",
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text.strip()


if __name__ == "__main__":
    print(sorter("Yes, I know that"))
