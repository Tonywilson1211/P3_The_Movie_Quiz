import os


def main_menu_nav(name, display_main_menu, choice):
    while True:
        print(f"{name}, when ready, press 'Enter' to head over ".center(80))
        print("to the main menu: ".center(80))    
        choice = input("\n ".center(80)).capitalize()
        if not choice.strip():
            display_main_menu(name)  # display the main menu again
            os.system('clear')
            break
    return name


def get_user_choice():
    """
    Navigation for the user to either continue to the next question,
    return to the main menu or exit the programme.
    """
    while True:
        try:
            choice = input("Press '1' for next question\n"
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
    Navigation for the user at the end of the quiz.
    """
    while True:
        try:
            choice = input("Press 'S' to start a new quiz\n"
                           "Press 'M' to return to main menu\n"
                           "Press 'E' to exit the "
                           "programme\nSelect Option: ").strip().upper()
            if choice not in ['S', 'M', 'E']:
                raise ValueError
            break
        except ValueError:
            print("Input not recognised. Please enter 'S', 'M' or 'E'.")
    return choice
