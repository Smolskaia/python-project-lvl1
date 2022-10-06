"""Brain-calc game."""
import random


RULES = 'What is the result of the expression?'
MAX_NUM = 20


def correct_answer(number_1, operat, number_2):
    """Return correct answer."""
    if operat == '+':
        correct_answer = number_1 + number_2
    if operat == '-':
        correct_answer = number_1 - number_2
    if operat == '*':
        correct_answer = number_1 * number_2
    return str(correct_answer)


def question_and_answer():
    """Generate game question and correct anweer."""
    number_1 = random.randint(1, MAX_NUM)
    number_2 = random.randint(1, MAX_NUM)
    operat = random.choice(['+', '-', '*'])
    question = f'{number_1} {operat} {number_2}'
    answer = correct_answer(number_1, operat, number_2)
    return question, answer
