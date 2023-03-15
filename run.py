"""
import section
"""

import json
import random
import os
import time
import sys
import termios
import tty
import logos


def print_slowly(text):
    """
    animation to make text appear to be typed out one letter at a time
    rather than appear in bulk. Termios and tty imported to prohibit user
    user from interupting text whilst printing.
    """
    file_descriptor = sys.stdin.fileno()
    old_settings = termios.tcgetattr(file_descriptor)
    try:
        # set terminal to raw mode to prohibit user interuption
        tty.setraw(file_descriptor)
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.015)
    finally:
        # restore terminal settings
        termios.tcsetattr(file_descriptor, termios.TCSADRAIN, old_settings)
    print()


def print_slowest(text):
    """
    Prints text slower than print_slowly function.
    Offers variety within the programme.
    """
    file_descriptor = sys.stdin.fileno()
    old_settings = termios.tcgetattr(file_descriptor)
    try:
        # set terminal to raw mode to prohibit user interuption
        tty.setraw(file_descriptor)
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.04)
    finally:
        # restore terminal settings
        termios.tcsetattr(file_descriptor, termios.TCSADRAIN, old_settings)
    print()


def load_questions():
    """
    Pull questions at random from movies.json file.
    """
    with open('movies.json', 'r', encoding='utf-8') as file:
        questions = json.load(file)
    random.shuffle(questions)
    return questions


def print_question_header(question_num):
    """
    Clear console.
    Print logo.
    Print point scoring information.
    Print movie name and question number out of 5.
    """
    os.system('printf "\033c"')
    logos.question_header_logo()
    print("\n\nPoints Available")
    print("5 points for correct year")
    print("3 points if 1 year off from correct year")
    print("1 point if 2 years off from correct year")
    print("0 points if 3 or more years off from correct year")
    print("2 bonus points if clue NOT used and within"
          " 2 years of correct year \n")
    print(f"\n{'*' * 17} Question {question_num+1} of 5 {'*' * 18}")


def get_clue_choice():
    """
    Get the user's choice on whether they want a clue.
    'Y' or 'N' inputs required.
    """
    error_message = ""
    while True:
        # Input errors are written over to avoid duplication using \033[F\033[K
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
    Prints a clue for the user to help them answer the question.
    """
    print_slowly(f"\nClue: {question['clue']}\n\n\n")


def get_user_answer():
    """
    User inputs their answer into the terminal.
    """
    error_message = ""
    while True:
        # Input errors are written over to avoid duplication using \033[F\033[K
        answer = input(f"\033[F\033[K{error_message}Guess the "
                       "year (e.g. 1990): ").strip()
        if len(answer) != 4:
            error_message = "\033[F\033[KPlease enter a year as a "\
                            "4-digit number. e.g. 2004.\n"
        else:
            try:
                year = int(answer)
                if year < 1950 or year > 2023:
                    error_message = "\033[F\033[KInput not recognised. "\
                                    "Please enter a valid year between "\
                                    "1950 and 2023.\n"
                else:
                    return year
            except ValueError:
                error_message = "\033[F\033[KPlease enter a year as a "\
                            "4-digit number. e.g. 2004.\n"


def calculate_points(user_answer, correct_answer, clue_choice, name):
    """
    The user's answer is compared to the correct answer and looks at whether
    a clue was used or not. The appropriate points are rewarded,
    along with a feedback message.
    """
    if user_answer == correct_answer:
        if clue_choice == 'N':
            points = 7
            feedback = f"\nYou got it {name}! And you got 2 bonus "\
                       "points\nfor not using a clue!\n"
        else:
            points = 5
            feedback = f"\nYou got it {name}!"
    elif abs(user_answer - correct_answer) == 1:
        if clue_choice == 'N':
            points = 5
            feedback = f"So close {name}, but not quite! But you do get 2 "\
                       "bonus points\nfor not using a clue!\n"
        else:
            points = 3
            feedback = f"\nSo close {name}, but not quite!\n"
    elif abs(user_answer - correct_answer) == 2:
        if clue_choice == 'N':
            points = 3
            feedback = f"\nNot bad {name}, but you can do better! "\
                       "But you do get 2 "\
                       "bonus points\nfor not using a clue!\n"
        else:
            points = 1
            feedback = f"\nNot bad {name}, but you can do better!\n"
    else:
        points = 0
        feedback = f"\nSorry {name}, that's not correct.\n"
    return points, feedback


def game_summary(score, total_score, name):
    """
    Console is cleared.
    Logo printed.
    User shown their total score at the end of the game, alongside
    'congrulations' and 'thank you for playing' messages.
    """
    os.system('printf "\033c"')
    logos.result_logo()
    print_slowly(f"\nCongratulations on completing the quiz {name}!")
    print_slowly("Let's take a look at how you got on....")
    percentage = round(score / total_score * 100)
    print_slowly(f"\nYour final score is {score} out of a "
                 f"possible {total_score}. That's {percentage}%!\n")
    print_slowly("Thanks for taking the time to play our "
                 f"quiz {name}, we hope you had fun!\n")


def main_menu_nav(name, choice):
    """
    Provides user with navigation options to menu screen.
    Error input handling 
    """
    while True:
        print(f"{name}, when ready, press 'Enter' to head over ".center(80))
        print("to the main menu: ".center(80))
        choice = input("\n ".center(80)).capitalize()
        if not choice.strip():
            os.system('clear')
            display_main_menu(name) 
            break
    return name


def get_user_choice():
    """
    Navigation for the user to either continue to the next question,
    return to the main menu or exit the programme.
    """
    while True:
        try:
            choice = input("\n************ Options ************\n\n"
                           "Press '1' for next question\n"
                           "Press 'M' to return to main menu\n"
                           "Press 'E' to exit the "
                           "programme\nSelect Option: ").strip().upper()
            if choice not in ['1', 'M', 'E']:
                raise ValueError
            break
        except ValueError:
            print("Input not recognised. Please enter '1', 'M' or 'E'.")
    return choice


def end_game_get_user_choice():
    """
    Navigation for the user at the end of the quiz. Options include
    start new quiz, return to main menu or exit programme.
    """
    while True:
        try:
            choice = input("\n************ Options ************\n\n"
                           "Press 'S' to start a new quiz\n"
                           "Press 'M' to return to main menu\n"
                           "Press 'E' to exit the "
                           "programme\nSelect Option: ").strip().upper()
            if choice not in ['S', 'M', 'E']:
                raise ValueError
            break
        except ValueError:
            print("Input not recognised. Please enter 'S', 'M' or 'E'.")
    return choice


def last_question_get_user_choice(name):
    """
    After the user answers the final question, they will see different
    navigation options which will offer them the results page,
    main menu, or exit programme.
    """
    while True:
        try:
            print_slowly("********** Quiz Complete! ***********\n")
            print_slowly(f"{name}, you have reached the end of the quiz!!!")
            print_slowly("See your options below\n")
            choice = input("\n************ Options ************\n\n"
                           "Press '1' to go to the results page\n"
                           "Press 'M' to return to main menu\n"
                           "Press 'E' to exit the "
                           "programme\nSelect Option: ").strip().upper()
            if choice not in ['1', 'M', 'E']:
                raise ValueError
            break
        except ValueError:
            print("Input not recognised. Please enter '1', 'M' or 'E'.")
    return choice


def play_game(name):
    """
    This function performs the following actions:
    sets score to 0
    number of questions set to 5
    calculates total possible score (5 questions x 7 max points)
    load_question function called to generate question
    iterate through randomly selected question and assign it an index
    print_question_header function call to print logo and index
    movie title printed in uppercase letters (typewriter effect)
    clue option function called, user enters choice (y or n)
    if y, clue printed
    get_user_answer function called. user enters answer
    user answer compared to correct answer, feedback and score printed
    if user correct, message confirms movie release date
    if user incorrect, message states when moive was released
    user shown the points scored
    user shown total points scored in quiz so far
    user shown navigation options
    if user is mid quiz, specific navigation options listed
     - continue to next question, go to main menu, exit programme
    if user has answered all questions, specific navigation options listed
     - see results page, go to main menu, exit programme
    if user is on results page, specific navigation options listed
     - start a new quiz, go to main menu, exit programme
    """
    # sets score to 0
    score = 0
    # number of questions set to 5
    num_of_questions = 5
    # calculates total possible score (5 questions x 7 max points)
    total_score = num_of_questions * 7
    # load_question function called to generate question
    questions = load_questions()
    # iterate through randomly selected question and assign it an index
    for i, question in enumerate(questions[:num_of_questions]):
        # print_question_header function call to print logo and index
        print_question_header(i)
        # movie title printed in uppercase letters (typewriter effect)
        title = question['title'].upper()
        print_slowly(f"\nMovie Title:   {title}\n\n")
        # get clue choice from user
        clue_choice = get_clue_choice()
        # if y, clue printed
        if clue_choice == 'Y':
            print_question_clue(question)
        # get answer from user
        answer = get_user_answer()
        # user answer compared to correct answer, feedback and score printed
        points, feedback = calculate_points(
            answer, question['answer'], clue_choice, name)
        print(feedback)
        # if user correct, message confirms movie release date
        if answer == question['answer']:
            print_slowly(
                f"{question['title']} was indeed "
                f"released in {question['answer']}")
        # if user incorrect, message states when moive was released
        else:
            print_slowly(f"{question['title']} was released"
                         f" in {question['answer']}")
        # user shown the points scored
        print_slowly(f"\nYou scored {points} points for this question.")
        # user shown total points scored in quiz so far
        score += points
        print_slowly(f"So far you have scored {score} points\n")
        # if user has answered all questions, specific nav options listed
        if i == num_of_questions - 1:
            last_question = last_question_get_user_choice(name)
            if last_question == '1':
                # takes user to results page
                os.system('clear')
                game_summary(score, total_score, name)
                end_choice = end_game_get_user_choice()
                # if user is on results page, specific nav options listed
                if end_choice == 'S':
                    # clears console and starts a new quiz
                    os.system('clear')
                    play_game(name)
                if end_choice == 'M':
                    # clears console and show main menu
                    os.system('clear')
                    display_main_menu(name)
                elif end_choice == 'E':
                    # prints message, clears console, exits programme
                    print_slowest("Exiting program....."
                                  "We hope to see you again soon!")
                    os.system('clear')
                    exit()
            elif last_question == 'M':
                # clears console and show main menu
                os.system('clear')
                display_main_menu(name)
            elif last_question == 'E':
                # prints message, clears console, exits programme
                print_slowest("Exiting program...We hope to "
                              "see you again soon!")
                os.system('clear')
                exit()
        # if user is mid quiz, specific navigation options listed
        else:
            choice = get_user_choice()
            if choice == '1':
                # quiz progresses to next question
                continue
            elif choice == 'M':
                # clears console and show main menu
                os.system('clear')
                display_main_menu(name)
            elif choice == 'E':
                # prints message, clears console, exits programme
                print_slowest("Exiting program...We hope to "
                              "see you again soon!")
                os.system('clear')
                exit()


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
    main_menu_nav(name, choice)


def display_main_menu(name):
    """
    Display main menu

    """
    os.system('printf "\033c"')
    logos.main_menu_logo()

    # loop until user chooses to exit
    menu_displayed = False

    while True:
        # checks if menu has already been displayed to avoid repition
        # from any input errors
        if not menu_displayed:
            print_slowly("\nMain Menu:\n")
            print_slowly("1. Start game")
            print_slowly("2. Quiz Guide")
            print_slowly("3. About the Developer")
            print_slowly("4. Exit program\n")
            menu_displayed = True

        # get user input
        choice = input("Select Option (1-4): ").strip()

        # handle user choice
        if choice == '1':
            play_game(name)
            menu_displayed = False
        elif choice == '2':
            os.system('clear')
            display_instructions(name)
            menu_displayed = False
        elif choice == '3':
            os.system('clear')
            display_about_developer(name)
            menu_displayed = False
        elif choice == '4':
            print_slowest("Exiting program...We hope to see you again soon!")
            os.system('clear')
            exit()
        else:
            print("Invalid choice, please enter a number from 1 to 4.")


def display_instructions(name):
    """
    Displays instructions on how to play the game
    """
    os.system('clear')
    logos.display_instructions_logo()
    print_slowly("************* THE AIM OF THE GAME ************\n".center(80))
    print("The aim of the game is to correctly guess the".center(80))
    print("release date of the movie.\n".center(80))
    print_slowly("*************** THE QUIZ GUIDE **************\n".center(80))
    print("Each quiz page will present a movie name".center(80))
    print("You will be asked if you want to see a clue".center(80))
    print("for when the movie was released.".center(80))
    print("Select either 'Y' (Yes) or 'N' (No).\n".center(80))
    print("Next you will enter your answer (4 digits e.g 1990)".center(80))
    print("You'll receive instant feedback on your answer,".center(80))
    print("see points scored and also total points so far.".center(80))
    print("Upon answering the 5th question you will be taken to".center(80))
    print("the quiz results screen and you can review".center(80))
    print("how well you did.\n\n".center(80))
    # call nav function for user to navigate back to main menu
    choice = ""
    main_menu_nav(name, choice)


def get_user_name():
    """
    Get user name.
    Error handling prohibits input being either less than 2 or more than 9
    """
    while True:
        name = input("\n ".center(74)).capitalize().strip()
        if len(name) > 1 and len(name) < 9:
            break
        else:
            print("Name should be between 2 and 9 characters long.".center(80))
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
    choice = ""
    main_menu_nav(name, choice)


landing_page()
