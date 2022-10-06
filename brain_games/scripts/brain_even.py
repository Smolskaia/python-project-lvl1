#!/usr/bin/env python3
"""Run brain-even game."""
from brain_games.games import brain_even
from brain_games.engine import start_engine


def main():
    """Run brain-even game."""
    start_engine(brain_even)


if __name__ == '__main__':
    main()
