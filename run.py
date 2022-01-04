import random
import word
import os

easy_level = word.easy_words
medium_level = word.med_words
hard_level = word.hard_words


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def welcome():
    """
    Display a welcome title and navigate to start the game or see rules
    """
    clear_terminal()
    print('{:*^80}'.format(' WELCOME TO HANGMAN ! '))
    print('\n' * 3)
    print('{:^80}'.format(' 1: PLAY GAME '))
    print('{:^80}'.format(' 2: SEE RULES '))
    print('\n' * 4)
    while True:
        player_choice = input('Please select 1 to play the game or 2 to see the rules.\n')
        if player_choice == '1':
            print('hello')
        elif player_choice == '2':
            rules()


def rules():
    """
    Display rules after the title
    """
    clear_terminal()
    print("To play the game you must guess the letters of the hidden word.")
    print("If the guess is correct the letter missing in the word")
    print("is replaced by the correct letter.")
    print("You can enter the whole word if you now what the word is.")
    print("Each wrong guess takes one life.")
    print("You can choose the dificulty level, E for easy (10 lives)")
    print("M for medium (8 lives) or H for hard (6 lives)")
    print("Be careful because a harder level means more letters.")
    print("Good luck!\n")

    menu = input("Press enter to return to the main menu\n")
    welcome()


welcome()


def display_hangman(lives):
    """
    Hangman lives
    """
    stages = [
                """
                _________
                |/      |
                |       O
                |     --|--
                |       |
                |      / \\
            ____|_\\___
                """,

                """
                _________
                |/      |
                |       O
                |     --|--
                |       |
                |      /
            ____|_\\___
                """,
                """
                _________
                |/      |
                |       O
                |     --|--
                |       |
                |
            ____|_\\___
                """,
                """
                _________
                |/      |
                |       O
                |     --|
                |       |
                |
            ____|_\\___
                """,
                """
                _________
                |/      |
                |       O
                |       |
                |       |
                |
            ____|_\\___
                """,
                """
                _________
                |/      |
                |       O
                |
                |
                |
            ____|_\\___
                """,
                """
                _________
                |/      |
                |
                |
                |
                |
            ____|_\\___
                """,
                """
                _________
                |/
                |
                |
                |
                |
            ____|_\\___
                """,
                """
                |/
                |
                |
                |
                |
            ____|_\\___
                """,
                """





            ___________
                """,
                """



                """

    ]
    return stages[lives]
