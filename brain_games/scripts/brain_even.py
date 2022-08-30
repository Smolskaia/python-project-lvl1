#!/usr/bin/env python3
import prompt
from brain_games.scripts.brain_games import greet
from brain_games.cli import welcome_user


def main():
    greet()
    welcome_user()


if __name__ == '__main__':
    main()
