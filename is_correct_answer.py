import re

pattern = re.compile(r'^\s*$')


def is_correct_answer(correct_answer: str, user_answer: str, score: int) -> int|None:
    user_answer = re.sub(r"(\s+$)|(^\s+)", '', user_answer)
    user_answer, correct_answer = user_answer.lower(), correct_answer.lower()
    if (not re.search(pattern, user_answer)
            and (correct_answer in user_answer
                 or re.search(r"\b{}\b".format(user_answer), correct_answer))):
        score += 1
        print('Правильный ответ! Начислен 1 балл.', end='\n\n')
        return score
    else:
        print('Неправильный ответ!', end='\n\n')
