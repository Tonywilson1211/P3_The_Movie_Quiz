import json
import sys
import termios
import tty
import time
import logos
import random


def print_slowly(text):
    """
    animation to make text appear to be typed out one letter at a time
    rather than appear in bulk.
    """
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)  # set terminal to raw mode
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.01)
    finally:
        # restore terminal settings
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    print()


def load_questions():
    """
    Pull questions from movies.json file.
    """
    with open('movies.json', 'r', encoding='utf-8') as f:
        questions = json.load(f)
    random.shuffle(questions)
    return questions


def get_clue_choice():
    """
    Get the user's choice on whether they want a clue.
    """
    error_message = ""
    while True:
        clue_choice = input(f"\033[F\033[K{error_message} \nWould "
                            "you like a clue? (Y or N): ").strip().upper()
        if clue_choice not in ['Y', 'N']:
            error_message = "\033[F\033[KInput not recognised. "\
                            "Please enter 'Y' or 'N'"
        else:
            error_message = ""
            break
    return clue_choice


def print_question_clue(question):
    """
    Prints the clue for the user when they ask for a clue.
    """
    print_slowly(f"\nClue: {question['clue']}\n\n\n")


def get_user_name():
    """
    Get user name
    """
    while True:
        name = input("\n ".center(74)).capitalize()
        if len(name) > 1 and len(name) < 9:
            break
        else:
            print("Name should be between 1 and 9 characters long.".center(80))
    return name


def landing_page():
    """
    Displays landing page - the first page the user sees
    """
    os.system('clear')
    logos.landing_page_logo()
    print("Hello and welcome to The Movie Quiz!".center(80))
    print("")
    print_slowly("The Quiz where your knowledge of movies and,".center(80))
    print_slowly("when they were released is put to the test!".center(80))
    print("")
    print("What is your name? ".center(80))
    name = get_user_name()
    print("")
    print(f"Welcome {name}!".center(80))
    print("")
    print_slowly("We have an impressive archive of over 135 movies".center(80))
    print_slowly("to test your knowledge, so with 5 questions ".center(80))
    print_slowly("per quiz, you are sure to have a varried".center(80))
    print_slowly("experience, everytime you play!\n".center(80))
    choice = ""
    nav.main_menu_nav(name, display_main_menu, choice)


landing_page()


def display_main_menu(name):
    """
    Display main menu
    """
    os.system('clear')
    logos.main_menu_logo()

    # loop until user chooses to exit
    menu_displayed = False

    while True:
        if not menu_displayed:
            print_slowly("\nMain Menu:\n")
            print_slowly("1. Start game")
            print_slowly("2. Quiz Guide")
            print_slowly("3. About the Developer")
            print_slowly("4. Exit program\n")
            menu_displayed = True

        # get user input
        choice = input("Select Option (1-4): ")

        # handle user choice
        if choice == '1':
            play_game(name)
            menu_displayed = False
        elif choice == '2':
            display_instructions(name)
            os.system('clear')
            menu_displayed = False
        elif choice == '3':
            display_about_developer(name)
            os.system('clear')
            menu_displayed = False
        elif choice == '4':
            print("Exiting program...We hope to see you again soon!")
            exit()
        else:
            print("Invalid choice, please enter a number from 1 to 4.")


def display_about_developer(name):
    """
    Displays the about developer page.
    """
    os.system('clear')
    logos.about_me_logo()
    print("The Movie Quiz was created by Anthony Wilson".center(80))
    print("for educational purposes".center(80))
    print("")
    print("LinkedIn Profile:".center(80))
    print("https://www.linkedin.com/in/ant-wilson/".center(80))
    print("")
    print("GitHub Repository".center(80))
    print("https://github.com/Tonywilson1211/TBD".center(80))
    print("")
    print("Thank you for taking the time to look at my project\n".center(80))
    choice = ""
    nav.main_menu_nav(name, display_main_menu, choice)


def display_instructions(name):
    """
    Displays instructions on how to play the game
    """
    os.system('clear')
    logos.display_instructions_logo()
    print_slowly("************* THE AIM OF THE GAME ************\n".center(80))
    print("The aim of the game is to correctly guess the".center(80))
    print("release date of the movie.".center(80))
    print("Simple! (if you know the answer that is...)\n\n".center(80))
    print_slowly("*************** THE QUIZ FORMAT **************\n".center(80))
    print("When the quiz first begins you will see the name".center(80))
    print("of the movie. You will be invited to choose".center(80))
    print("to see a clue or not. Once you have made your ".center(80))
    print("choice you will be invited to guess the answer.\n".center(80))
    print("Once you have entered your answer you will see".center(80))
    print("if you were correct, the number of points scored,".center(80))
    print("and your total score so far. Once you have".center(80))
    print("answered 5 questions you will be taken to".center(80))
    print("the quiz summary screen and you can review".center(80))
    print("how well you did.\n\n".center(80))
    print_slowly("*************** HOW CLUES WORK ***************\n".center(80))
    print("Before you guess the year the movie was released".center(80))
    print("you will be asked if you want to see a clue.".center(80))
    print("You'll need to enter either 'Y' (yes) or 'N' (no)\n".center(80))
    print("All clues give you a good hint as to when the movie".center(80))
    print("was released. For example, if a movie was released in".center(80))
    print("2002 the clue would be 'Released in early 2000s'\n\n".center(80))
    print_slowly("******* HOW THE POINTS ARE CALCULATED ********\n".center(80))
    print("Enter the correct answer, you are receive 5 points.\n".center(80))
    print("If you are 1 year off the correct answer, you receive".center(80))
    print(" with 3 points.\n".center(80))
    print("If you are 2 years off the correct answer, you receive".center(80))
    print("with 1 point.\n".center(80))
    print("If you are 3 or more years away from the ".center(80))
    print("correct answer, you get 0 points.\n".center(80))
    print("If you guess within 2 years of the release date and".center(80))
    print("don't use a clue, you receive an additional 2 points.\n".center(80))
    print("You will be asked 5 questions, so the maximum".center(80))
    print("possible score is 35 points.\n".center(80))
    choice = ""
    nav.main_menu_nav(name, display_main_menu, choice)