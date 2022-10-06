#!/usr/bin/env python3
"""Run brain-calc game."""
from brain_games.games import brain_calc
from brain_games.engine import start_engine


def main():
    """Run brain-calc game."""
    start_engine(brain_calc)


if __name__ == '__main__':
    main()
