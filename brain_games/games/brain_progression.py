"""brain-progression game."""
import random


RULES = 'What number is missing in the progression?'
MAX_COUNT_NUM = 15
MIN_COUNT_NUM = 15
MAX_DIFFERENCE = 10
MIN_DIFFERENCE = 2
MAX_VALUE = 100
MIN_VALUE = 10


def make_progression(initial_term, difference, count_num):
    """Create progression."""
    n_term = initial_term + difference * count_num
    arithmetic_progression = list(range(initial_term, n_term + 1, difference))
    return arithmetic_progression


def make_string(arithmetic_progression):
    """Create string."""
    arithmetic_progression_string = ' '.join(map(str, arithmetic_progression))
    return arithmetic_progression_string


def correct_answer(seq):
    """Return correct answer."""
    index = random.randint(0, len(seq) - 1)
    return str(seq[index]), index


def question_and_answer():
    """Generate game question and correct anweer."""
    initial_term = random.randint(MIN_VALUE, MAX_VALUE)
    difference = random.randint(MIN_DIFFERENCE, MAX_DIFFERENCE)
    count_num = random.randint(MIN_COUNT_NUM, MAX_COUNT_NUM)
    arithmetic_progression = make_progression(
        initial_term,
        difference,
        count_num)
    answer, mutable_index = correct_answer(arithmetic_progression)
    arithmetic_progression[mutable_index] = '..'
    question = make_string(arithmetic_progression)
    return question, answer
