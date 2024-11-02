from app_classes.user import User
from colorama import Fore, Style

# from colorama import Fore
from helper_functions.salary_helpers import calculate_salaries

john = User("John", 1000)
jack = User("Jack", 2000)

print(john)

# print(Fore.BLUE + "Hello")

def main_loop():
    while True:
        user_input = input(Fore.BLUE + "enter command: " + Style.RESET_ALL ).strip()
        if user_input == 'salaries':
            print(calculate_salaries([john, jack]))
        elif user_input == 'exit':
            print('Goodbye!')
            break


# main_loop()