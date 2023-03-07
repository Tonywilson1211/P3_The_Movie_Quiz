import json
import sys
import termios
import tty
import time


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