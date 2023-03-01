import os
import time

from helpers import load_questions
from reviser import reviser
from sorter import sorter

# questions_files = [
#   {'file_name': 'question_arab.csv', 'language': 'Egyptian arabic'},
#   {'file_name': 'question_ceb.csv', 'language': 'Cebano'},
#   {'file_name': 'question_chin.csv', 'language': 'Chinese'},
#   {'file_name': 'question_dutch.csv', 'language': 'Dutch'},
#   {'file_name': 'question_eng.csv', 'language': 'English'},
#   {'file_name': 'question_fr.csv', 'language': 'French'},
# ----
#   {'file_name': 'question_ger.csv', 'language': 'German'},
#   {'file_name': 'question_ita.csv', 'language': 'Italian'},
#   {'file_name': 'question_japo.csv', 'language': 'Japanese'},
#   {'file_name': 'question_kor.csv', 'language': 'Korean'},
#   {'file_name': 'question_rus.csv', 'language': 'Russian'},
#   {'file_name': 'question_spa.csv', 'language': 'Spanish'},

# ---
#   {'file_name': 'question_swah.csv', 'language': 'Swahili'},
#   {'file_name': 'question_swe.csv', 'language': 'Swedish'},
#   {'file_name': 'animals.csv', 'language': None}
#   {'file_name': 'history.csv', 'language': None}
#   {'file_name': 'Humanb.csv', 'language': None}
#   {'file_name': 'science.csv', 'language': None}
# ]

# test file

questions_files = [
  {'file_name': 'science.csv', 'language': None}
]

if __name__ == "__main__":

    for question_file in questions_files:
        with open('answers/answer_' + question_file['file_name'], 'w') as f:
            questions_to_answer = load_questions(question_file['file_name'],
                                                 question_file['language'])
            count = 0
            f.write('question_statement;answer;classification;language\n')
            for question in questions_to_answer:
                flag = True
                while flag:
                    try:
                        question['answer'] = reviser(
                            question['question_statement'])
                        question['classification'] = sorter(question['answer'])
                        flag = False
                    except:
                        print('error, will try again in 20 seconds')
                        time.sleep(20)
                count += 1
                print('count: ', count)
                print('answer: ', question['answer'])
                print('classification: ', question['classification'])
                f.write(
                    f"{question['question_statement']};{question['answer']};{question['classification']};{question['language']}\n"
                )
