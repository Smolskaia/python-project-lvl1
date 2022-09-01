#!/usr/bin/env python3

import prompt
from random import randint


def play_even_game():
    print('Welcome to the Brain Games!')
    who = prompt.string('May I have your name? ')
    print(f'Hello, {who}!')
    print('Answer "yes" if the number is even, otherwise answer "no"')
    congrats = f'Congratulations, {who}!'

    counter = 0
    while counter < 3:
        random_number = randint(1, 100)

        if random_number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        print(f'Question: {random_number}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
            counter += 1
        else:
            print(f"{user_answer} is wrong answer ;(. Correct answer was {correct_answer}.\nLet's try again, {who}!")
            return
    print(congrats)


def main():
        play_even_game()


if __name__ == '__main__':
    main()
