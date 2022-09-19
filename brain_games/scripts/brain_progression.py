# !/usr/bin/env python3
import prompt
from random import randint

def play_progression_game():
    print('Welcome to the Brain Games!')
    who = prompt.string('May I have your name? ')
    print(f'Hello, {who}!')
    print('What number is missing in the progression?')
    congrats = f'Congratulations, {who}!'

    counter = 0
    while counter < 3:
        progression = []
        start_progression = randint(1, 5)
        step_progression = randint(1, 5)
        length_progression = randint(8, 13)
        end_progression = start_progression + (length_progression - 1) * step_progression

        for i in range(start_progression, end_progression + 1, step_progression):
            progression.append(i)

        hidden_number_index = randint(0, len(progression) - 1)
        hidden_number = ".."
        correct_answer = str(progression[hidden_number_index])
        progression[hidden_number_index] = hidden_number
        question = " ".join(map(str, progression))

        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
            counter += 1
        else:
            print(f"{user_answer} is wrong answer ;(. Correct answer was {correct_answer}.\nLet's try again, {who}!")
            return
    print(congrats)


def main():
        play_progression_game()


if __name__ == '__main__':
    main()
