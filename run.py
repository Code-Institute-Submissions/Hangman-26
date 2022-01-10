#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Project porfolio 3, Code Institute
"""

import random
import os
import words

easy_level = words.easy_words
medium_level = words.med_words
hard_level = words.hard_words

width = os.get_terminal_size().columns


def clear_terminal():
    """"
    Clear terminal
    """

    os.system(('cls' if os.name == 'nt' else 'clear'))


def title():
    """
    Display the title
    """
    print(
                """
                 _   _
                | | | | __ _ _ __   __ _ _ __ ___   __ _ _ __
                | |_| |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\
                |  _  | (_| | | | | (_| | | | | | | (_| | | | |
                |_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                                    |___/
                """
            )


def welcome():
    """
    Display a welcome title and navigate to start the game or see rules
    """

    clear_terminal()
    title()
    print('\n')
    print(' 1 PLAY GAME '.center(80))
    print(' 2 SEE RULES '.center(80))
    print('\n' * 4)
    while True:
        player_choice = input(' ' * 25 + 'Please select 1 or 2: ')
        if player_choice == '1':
            start_game()
        elif player_choice == '2':
            rules()
        else:
            print('You must chose 1 or 2'.center(74))
            print('\n')


def rules():
    """
    Display rules after the title
    """
    clear_terminal()
    title()
    print(
        """
            To play the game you must guess the letters of the hidden word.
            If the guess is correct the letter missing in the word
            is replaced by the correct letter.
            You can enter the whole word if you know what the word is.
            Each wrong guess takes one life.
            You can choose the difficulty level,
            E for easy (10 lives), M for medium (8 lives)
            or H for hard (6 lives).
            But be careful because a harder level means more letters.
            \n
            Good luck!
            """
            )

    menu = input(' ' * 12 + "Press enter to return to the main menu\n")
    print("\n")
    welcome()


def set_difficulty():
    """
    This function will set the dificulty level
    depending on the user input
    """

    print('\n')
    print('Please select E for easy(10 lives),'.center(80))
    print('M for medium 8 lives) and H for hard(6 lives)'.center(80))
    difficulty = False
    while not difficulty:
        difficulty_level = input(' '.center(40)).upper()
        if difficulty_level == 'E':
            difficulty = True
            lives = 10
            return lives
        elif difficulty_level == 'M':
            difficulty = True
            lives = 8
            return lives
        elif difficulty_level == 'H':
            difficulty = True
            lives = 6
            return lives
        else:
            print('Select E, M or H'.center(80))


def random_word(lives):
    """
    Set the random word depending on users difficulty level
    """

    if lives == 10:
        get_words = random.choice(easy_level).upper()
        return get_words
    elif lives == 8:
        get_words = random.choice(medium_level).upper()
        return get_words
    elif lives == 6:
        get_words = random.choice(hard_level).upper()
        return get_words


def game(word, lives_num):
    """
    This fucntion will set the difficulty level
    and start the game
    """

    clear_terminal()
    blanks = '_' * len(word)
    guessed = False
    guessed_letters = []
    guessed_word = []
    title()
    print(display_hangman(lives_num))
    print(blanks.center(76))
    print('\n')

    while not guessed and lives_num > 0:
        player_guess = input(' ' * 25 + 'Please guess a leter: '
                             ).upper()
        if len(player_guess) == 1 and player_guess.isalpha():
            if player_guess in guessed_letters:
                clear_terminal()
                title()
                print(' ' * 25 + 'You already guessthe letter '
                      + player_guess)
            elif player_guess not in word:
                clear_terminal()
                title()
                print(' ' * 25 + 'Sorry ' + player_guess
                      + ' is not in the word')
                lives_num -= 1
                guessed_letters.append(player_guess)
            else:
                clear_terminal()
                title()
                print(' ' * 25 + 'Great ' + player_guess
                      + ' is in the word!')
                guessed_letters.append(player_guess)
                word_list = list(blanks)
                indices = [i for (i, letter) in enumerate(word)
                           if letter == player_guess]
                for index in indices:
                    word_list[index] = player_guess
                blanks = ''.join(word_list)
                if '_' not in blanks:
                    guessed = True
        elif len(player_guess) == len(word) and player_guess.isalpha():
            if player_guess in guessed_word:
                clear_terminal()
                title()
                print(' ' * 25 + 'You already guessedthe word '
                      + player_guess)
            elif player_guess != word:
                clear_terminal()
                title()
                print(' ' * 25 + player_guess + 'is not in the word')
                lives_num -= 1
                guessed_word.append(player_guess)
            else:
                guessed = True
                blanks = word
        else:
            clear_terminal()
            title()
            print(' ' * 25 + 'Not a valid guess')
        print(display_hangman(lives_num))
        print(blanks.center(76))
        print('\n')

    if guessed:
        clear_terminal()
        title()
        print('Congratulations you guessed the word'.center(80))
        while True:
            player_wins = input(' ' * 25
                                + 'Would you like to play again? Y/N '
                                ).upper()
            print('\n')
            if player_wins == 'Y':
                start_game()
            elif player_wins == 'N':
                welcome()
            else:
                print('You must press Y or N'.center(80))
    else:
        clear_terminal()
        title()
        print(' ' * 20 + 'Sorry, you run out of lives. The word was: '
              + word)
        while True:
            player_lost = input(' ' * 20
                                + 'Would you liketo play again? Y/N '
                                ).upper()
            print('\n')
            if player_lost == 'Y':
                start_game()
                break
            elif player_lost == 'N':
                welcome()
                break
            else:
                print('You must press Y or N'.center(80))


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



                                    """,
        ]

    return stages[lives]


def start_game():
    """
    This function will start the game
    """

    clear_terminal()
    title()
    lives_num = set_difficulty()
    get_random_word = random_word(lives_num)
    game(get_random_word, lives_num)


def main():
    """
    Main function
    """

    welcome()


main()
