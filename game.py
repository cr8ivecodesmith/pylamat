#!/usr/bin/python -tt
from re import compile
from sys import argv
from os.path import abspath
import json


if __name__ == '__main__':
    play_again = True
    no_pattern = compile(r'^n.*')

    story_path = abspath(argv[1])
    story_file = open(story_path, 'r')
    story = json.load(story_file)
    story_file.close()

    # TODO (codemickeycode): display game title

    # Game Loop
    while (play_again):

        reset_game = raw_input('Play again? [Y/n]: ')
        play_again = False if no_pattern.match(reset_game.lower()) else True
