# 1 - Билл Гейтс 28.10.1955
# 2 - Махатма Ганди 02.10.1869
# 3 - Михаэль Шумахер 03.01.1969
# 4 - Иван Грозный 25.08.1530
# 5 - Антонио Вивальди 04.03.1678
# 6 - Илон Маск 28.06.1971
# 7 - Ванга 31.01.1911
# 8 - Вольф Мессинг 10.09.1899
# 9 - Константин Жуков 01.12.1896
# 10 - Майкл Джордан 17.02.1963

import random

birthdays = ['28.10.1955', '02.10.1869', '03.01.1969', '25.08.1530', '04.03.1678', '28.06.1971',
             '31.01.1911', '10.09.1899', '01.12.1896', '17.02.1963']
questions = ['Напишите день рождения Билла Гейтса в формате dd.mm.yyyy: ',
             'Напишите день рождения Махатмы Ганди в формате dd.mm.yyyy: ',
             'Напишите день рождения Михаэля Шумахера в формате dd.mm.yyyy: ',
             'Напишите день рождения Ивана Грозного в формате dd.mm.yyyy: ',
             'Напишите день рождения Антонио Вивальди в формате dd.mm.yyyy: ',
             'Напишите день рождения Илона Маска в формате dd.mm.yyyy: ',
             'Напишите день рождения Ванги в формате dd.mm.yyyy: ',
             'Напишите день рождения Вольфгана Мессинга в формате dd.mm.yyyy: ',
             'Напишите день рождения Константина Жукова в формате dd.mm.yyyy: ',
             'Напишите день рождения Майкла Джордана в формате dd.mm.yyyy: ', ]

birthday_indexes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

total_questions = 5
five_random_question_indexes = random.sample(birthday_indexes, total_questions)
print(five_random_question_indexes)

wrong_answers = 0

for index in five_random_question_indexes:
    answer = input(questions[index])
    if answer != birthdays[index]:
        # print('Неверно')
        wrong_answers += 1
print(wrong_answers)
right_answers = total_questions - wrong_answers
print(right_answers)