#!/usr/bin/env python3
"""Run brain-prime game."""
from brain_games.games import brain_prime
from brain_games.engine import start_engine


def main():
    """Run brain-prime game."""
    start_engine(brain_prime)


if __name__ == '__main__':
    main()
