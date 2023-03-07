import json
import sys
import termios
import tty
import time
import logos


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