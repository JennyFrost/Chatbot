from connect_to_api import get_random_questions
from is_correct_answer import is_correct_answer

url = 'http://jservice.io/api/random'
number_of_questions = int(input("Введите количество вопросов: "))
questions_answers = get_random_questions(url=url, n=number_of_questions)
score = 0

for i, (question, correct_answer) in enumerate(questions_answers):
    print(f'Вопрос {i+1}')
    user_answer = input(f'{question}\nВаш ответ (первая попытка):\n')
    is_correct = is_correct_answer(correct_answer, user_answer, score)
    if is_correct:
        score = is_correct
    else:
        user_answer = input('Ваш ответ (вторая попытка):\n')
        is_correct = is_correct_answer(correct_answer, user_answer, score)
        if is_correct:
            score = is_correct

print(f'Спасибо за игру! Вы набрали {score} ', end='')
if score % 10 == 1 and score != 11:
    print('балл.')
elif score % 10 in (2, 3, 4) and score not in (12, 13, 14):
    print('балла.')
else:
    print('баллов.')