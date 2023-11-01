from typing import List
import requests


def get_random_questions(url: str, n: int) -> List[tuple]:
    url += f"?count={n}"
    question_dicts = requests.get(url).json()
    questions_answers = [(question_dict['question'], question_dict['answer'])
                         for question_dict in question_dicts]
    return questions_answers
