import random
import word

easy_level = word.easy_words
medium_level = word.med_words
hard_level = word.hard_words

def rules():
    print("To play the game you must guess the letters of the hidden word.")
    print("If the guess is correct the letter missing in the word")
    print("is replaced by the correct letter.")
    print("You can enter the whole word if you now what the word is.")
    print("Each wrong guess takes one life.")
    print("You can choose the dificulty level, E for easy (10 lives)")
    print("M for medium (8 lives) or H for hard (6 lives)")
    print("Be careful because a harder level means more letters.")
    print("Good luck!\n")

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