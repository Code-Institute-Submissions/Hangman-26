import random
import word
import os

easy_level = word.easy_words
medium_level = word.med_words
hard_level = word.hard_words


def clear_terminal():
    """"
    Clear terminal
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def title():
    """
    Display the title
    """
    print('{:*^80}'.format(
                """
                 _   _
                | | | | __ _ _ __   __ _ _ __ ___   __ _ _ __
                | |_| |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\
                |  _  | (_| | | | | (_| | | | | | | (_| | | | |
                |_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                                    |___/
                """
            ))

def welcome():
    """
    Display a welcome title and navigate to start the game or see rules
    """
    clear_terminal()
    title()
    print('\n' * 3)
    print('{:^80}'.format(' 1 PLAY GAME '))
    print('{:^80}'.format(' 2 SEE RULES '))
    print('\n' * 4)
    while True:
        player_choice = input('Please select 1 or 2: ')
        if player_choice == '1':
            play()
        elif player_choice == '2':
            rules()


def rules():
    """
    Display rules after the title
    """
    clear_terminal()
    title()
    print('\n' * 2)
    print('{:^80}'.format(
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
    ))

    menu = input("Press enter to return to the main menu\n")
    welcome()


def play():
    """
    This functino will start the game and
    set the game difficulty
    """
    difficulty_level = input("Please select E for easy(10 lives), M for medium 8 lives) and H for hard(6 lives)\n").upper()
    if difficulty_level == 'E':
        lives = 10
        word = random.choice(easy_level).upper()
    elif difficulty_level == 'M':
        lives = 8
        word = random.choice(medium_level).upper()
    elif difficulty_level == 'H':
        lives = 6
        word = random.choice(hard_level).upper()
    else:
        ("Plese select E, M or H")
    
    blanks = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_word = []
    print(display_hangman(lives))
    print(blanks)
    print("\n")
    print(word)

    while not guessed and lives > 0:
        player_guess = input("Please guess a leter: ").upper()
        if len(player_guess) == 1 and player_guess.isalpha():
            if player_guess in guessed_letters:
                print("You already guess the letter", player_guess)
            elif player_guess not in word:
                print("Sorry", player_guess, "is not in the word")
                lives -= 1
                guessed_letters.append(player_guess)
            else:
                print("Great", player_guess, "is in the word!")
                guessed_letters.append(player_guess)
                word_list = list(blanks)
                indices = [i for i, letter in enumerate(word) if letter == player_guess]
                for index in indices:
                    word_list[index] = player_guess
                blanks = "".join(word_list)
                if "_" not in blanks:
                    guessed = True
        elif len(player_guess) == len(word) and player_guess.isalpha():
            if player_guess in guessed_word:
                print("You already guessed the word", player_guess)
            elif player_guess != word:
                print(player_guess, "is not in the word")
                lives -= 1
                guessed_word.append(player_guess)
            else:
                guessed = True
                blanks = word
        else:
            print("Not a valid guess")
        print(display_hangman(lives))
        print(blanks)

    if guessed:
        print("Congrads")
    else:
        print("Sorry")





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


def main():
    """
    Main function
    """
    welcome()


main()
