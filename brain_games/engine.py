#!/usr/bin/env python3
"""Game engine functions."""
import prompt

COUNT_OF_ROUNDS = 3


def start_engine(game=None):
    """Game engine function."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    if game:
        print(game.RULES)
        count = 0
        while count < COUNT_OF_ROUNDS:
            question, correct_answer = game.question_and_answer()
            print(f'Question: {question}')
            answer = prompt.string('Your answer: ')
            if answer == correct_answer:
                print('Correct!')
                count += 1
            else:
                print(f"'{answer}' is wrong answer ;(. ", end='')
                print(f"Correct answer was '{correct_answer}'.")
                print(f"Let's try again, {name}!")
                break
            if count == COUNT_OF_ROUNDS:
                print(f'Congratulations, {name}!')
