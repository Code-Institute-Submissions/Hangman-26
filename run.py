import random
import word
import os

easy_level = word.easy_words
medium_level = word.med_words
hard_level = word.hard_words

text_align = os.get_terminal_size().columns



def clear_terminal():
    """"
    Clear terminal
    """
    os.system('cls' if os.name == 'nt' else 'clear')



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
    print('{:^80}'.format(' 1 PLAY GAME '))
    print('{:^80}'.format(' 2 SEE RULES '))
    print('\n' * 4)
    while True:
        player_choice = input(' ' * 25 + 'Please select 1 or 2: ')
        if player_choice == '1':
            play()
        elif player_choice == '2':
            rules()
        else:
            print(' ' * 25 + 'You must chose 1 or 2')
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


def play():
    """
    This functino will start the game and
    set the game difficulty
    """
    clear_terminal()
    title()
    print('\n')
    print('{:^80}'.format("Please select E for easy(10 lives),"))
    print('{:^80}'.format("M for medium 8 lives) and H for hard(6 lives)"))
    difficulty_level = input(' ' * 25 + '\n').upper()
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
    
    clear_terminal()   
    blanks = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_word = []
    title()
    print(display_hangman(lives))
    print('{:^75}'.format(blanks))
    print('\n')
    
    while not guessed and lives > 0:
        player_guess = input(' ' * 25 + "Please guess a leter: ").upper()
        if len(player_guess) == 1 and player_guess.isalpha():
            if player_guess in guessed_letters:
                clear_terminal()
                title()
                print('{:^80}'.format("You already guess the letter "+ player_guess))
            elif player_guess not in word:
                clear_terminal()
                title()
                print('{:^80}'.format("Sorry "+ player_guess + " is not in the word"))
                lives -= 1
                guessed_letters.append(player_guess)
            else:
                clear_terminal()
                title()
                print('{:^80}'.format("Great " + player_guess + " is in the word!"))
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
                clear_terminal()
                title()
                print('{:^80}'.format("You already guessed the word " + player_guess))
            elif player_guess != word:
                clear_terminal()
                title()
                print('{:^80}'.format(player_guess + "is not in the word"))
                lives -= 1
                guessed_word.append(player_guess)
            else:
                guessed = True
                blanks = word
        else:
            clear_terminal()
            title()
            print('{:^80}'.format("Not a valid guess"))
        print(display_hangman(lives))
        print('{:^75}'.format(blanks))
        print('\n')

    if guessed:
        clear_terminal()
        title()
        print('{:^80}'.format("Congratulations you guessed the word"))
        player_wins = input(' ' * 25 + "Would you like to play again? Y/N \n").upper()
        if player_wins == 'Y':
            play()
        elif player_wins == 'N':
            welcome()
        else:
            print('{:^80}'.format("You must press Y or N"))
    else:
        clear_terminal()
        title()
        print('{:^80}'.format("Sorry, you run out of lives"))
        player_lost = input(' ' * 25 + "Would you like to play again? Y/N \n").upper()
        if player_lost == 'Y':
            play()
        elif player_lost == 'N':
            welcome()
        else:
            print("You must press Y or N")





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
