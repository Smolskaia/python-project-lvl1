"""brain-prime game."""
import random


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MAX_NUM = 50
MIN_NUM = 1


def is_prime(n):
    """Prime number or not."""
    d = 2
    while n % d != 0:
        d += 1
    return d == n


def correct_answer(simple):
    """Return correct answer."""
    return 'yes' if is_prime(simple) else 'no'


def question_and_answer():
    """Generate game question and correct anweer."""
    simple = random.randint(MIN_NUM, MAX_NUM)
    question = f'{simple}'
    answer = correct_answer(simple)
    return question, answer
