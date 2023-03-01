textos = ['answer_question_arab.csv','answer_question_ceb.csv','answer_question_chin.csv',
          'answer_question_dutch.csv','answer_question_eng.csv','answer_question_fr.csv',
          'answer_question_ger.csv','answer_question_ita.csv','answer_question_japo.csv',
          'answer_question_kor.csv','answer_question_rus.csv','answer_question_spa.csv',
          'answer_question_swah.csv','answer_question_swe.csv'
         ]

textos_c = ['answers/answer_science.csv', 'answers/answer_Humanb.csv', 'answers/answer_animals.csv','answers/answer_history.csv']

with open("merged_controversia2.csv", "w") as final_file:
    for texto in textos_c:
        with open(texto, 'r') as temp_file:
            datos = temp_file.readlines()
            topico = texto.split('answers/answer_')[1]
            topico = topico.strip('.csv')
            out = topico + ';'
            for i in datos:
                final_file.write(out+i)
