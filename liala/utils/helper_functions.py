def get_menu_choice(choices):
    """
    Displays a menu of numbered choices and returns the user's selection.
    :param choices: a list of strings representing the menu options
    :return: an integer representing the user's choice
    """
    for i, choice in enumerate(choices):
        print(f"{i + 1}. {choice}")
    
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice < 1 or choice > len(choices):
                print(f"Please enter a number between 1 and {len(choices)}")
            else:
                return choice
        except ValueError:
            print("Invalid input. Please enter a number.")
