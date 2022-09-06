#!/usr/bin/env python3
import random
import prompt
import math
from random import randint


def play_gcd_game():
    print('Welcome to the Brain Games!')
    who = prompt.string('May I have your name? ')
    print(f'Hello, {who}!')
    print('Find the greatest common divisor of given numbers.')
    congrats = f'Congratulations, {who}!'

    counter = 0
    while counter < 3:
        num_1 = randint(1, 50)
        num_2 = randint(1, 50)
        print(f'Question: {num_1} {num_2}')
        correct_answer = str(math.gcd(num_1, num_2))

        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
            counter += 1
        else:
            print(f"{user_answer} is wrong answer ;(. Correct answer was {correct_answer}.\nLet's try again, {who}!")
            return
    print(congrats)


def main():
        play_gcd_game()


if __name__ == '__main__':
    main()
