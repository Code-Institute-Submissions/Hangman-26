import random
import word

easy_level = word.easy_words
medium_level = word.med_words
hard_level = word.hard_words



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