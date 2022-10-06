#!/usr/bin/env python3
"""Run brain-gcd game."""
from brain_games.games import brain_gcd
from brain_games.engine import start_engine


def main():
    """Run brain-gcd game."""
    start_engine(brain_gcd)


if __name__ == '__main__':
    main()
