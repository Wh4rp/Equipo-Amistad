def load_questions(name_file, language):
    with open('questions/' + name_file) as f:
        questions = f.readlines()
        if ';' in questions[0]:
            questions_dictionary = [{"question_statement": question.split(';')[0].strip(), "language": question.split(';')[1].strip()} for question in questions[1:]]
        else:
            questions_dictionary = [{"question_statement": question.strip(), "language": language} for question in questions]
    return questions_dictionary