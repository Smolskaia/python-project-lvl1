#!/usr/bin/env python3

import random
import prompt
from random import randint
from random import choice


def play_calc_game():
    print('Welcome to the Brain Games!')
    who = prompt.string('May I have your name? ')
    print(f'Hello, {who}!')
    print('What is the result of the expression?')
    congrats = f'Congratulations, {who}!'
    operations = ['+', '-', '*']

    counter = 0
    while counter < 3:
        num_1 = randint(10, 30)
        num_2 = randint(1, 5)
        operation = random.choice(operations)

        print(f'Question: {num_1} {operation} {num_2}')

        if operation == '+':
            correct_answer = str(num_1 + num_2)
        if operation == '-':
            correct_answer = str(num_1 - num_2)
        if operation == '*':
            correct_answer = str(num_1 * num_2)
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
            counter += 1
        else:
            print(f"{user_answer} is wrong answer ;(. Correct answer was {correct_answer}.\nLet's try again, {who}!")
            return
    print(congrats)


def main():
        play_calc_game()


if __name__ == '__main__':
    main()
