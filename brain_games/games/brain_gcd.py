"""Brain-gcd game."""
import random


RULES = 'Find the greatest common divisor of given numbers.'
MAX_NUM = 50
MIN_NUM = 1


def gcd(a, b):
    """Find gcd, return gcd."""
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return (a + b)


def correct_answer(number_1, number_2):
    """Return correct answer."""
    return str(gcd(number_1, number_2))


def question_and_answer():
    """Generate game question and correct anweer."""
    number_1 = random.randint(MIN_NUM, MAX_NUM)
    number_2 = random.randint(MIN_NUM, MAX_NUM)
    question = f'{number_1} {number_2}'
    answer = correct_answer(number_1, number_2)
    return question, answer
