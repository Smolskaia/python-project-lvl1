#!/usr/bin/env python3
import prompt
from random import randint
from math import  sqrt


def play_prime_game():
    print('Welcome to the Brain Games!')
    who = prompt.string('May I have your name? ')
    print(f'Hello, {who}!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    congrats = f'Congratulations, {who}!'

    counter = 0
    while counter < 3:
        random_number = randint(2, 50) #1 not being a prime number, is ignored

        i = 2 #all numbers are divisible by 1, so we check the divisors starting from 2
        while i <= sqrt(random_number):
            if random_number % i == 0:
                correct_answer = 'no'
                break
            i += 1
        else:
            correct_answer = 'yes'


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
        play_prime_game()


if __name__ == '__main__':
    main()
