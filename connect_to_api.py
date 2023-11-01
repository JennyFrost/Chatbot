from typing import List
import requests
from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
)


@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
def get_random_questions(url: str, n: int) -> List[tuple]:
    url += f"?count={n}"
    question_dicts = requests.get(url).json()
    questions_answers = [(question_dict['question'], question_dict['answer'])
                         for question_dict in question_dicts]
    return questions_answers
