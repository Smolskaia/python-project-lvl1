"""Brain-even game."""
import random


RULES = 'Answer "yes" if number even otherwise answer "no".'
MAX_NUM = 100
MIN_NUM = 1


def is_even(number):
    """Even number or not."""
    return number % 2 == 0


def correct_answer(number):
    """Return expected answer."""
    return 'yes' if is_even(number) else 'no'


def question_and_answer():
    """Generate game question and correct anweer."""
    number = random.randint(MIN_NUM, MAX_NUM)
    question = f'{number}'
    answer = correct_answer(number)
    return question, answer
