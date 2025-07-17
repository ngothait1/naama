import os
import pandas as pd
from person import Person
from student import Student
from employee import Employee
from menuOption import MenuOption
from utils import parse_valid_int, is_exist, check_if_data_exist, press_enter


def save_new_entry(users_data: dict, sum_age: int, user_ids: list) -> int | None:
    id_input = input("ID: ")
    user_id = parse_valid_int(id_input)
    if user_id is None:
        return 
    if is_exist(user_id, users_data):
        return 
 
    username = input("Name: ")
    if not username.strip():
        print("Invalid input! Name cannot be empty.")
        return
    age_input = input("Age: ")
    user_age = parse_valid_int(age_input)
    if user_age is None:
        return
    if user_age < 0 or user_age > 120:
        print("Invalid age! Age must be between 0-120.")
        return
   
    person_types = [Person, Employee, Student]

    try:
        user_choice = parse_valid_int(input("Enter 0 for Person, 1 for Employee or 2 for Student: "))

        while user_choice is None or user_choice not in range(len(person_types)):
            print("Invalid input! Enter '0', '1', or '2': ")
            user_choice = parse_valid_int(input("Enter 0 for Person, 1 for Employee or 2 for Student: "))

        new_user = person_types[user_choice](user_id, username, user_age)

    except ValueError as e:
        print(f"Failed to create user ID [{user_id}]: {e}")
        return

    sum_age += user_age
    users_data[user_id] = new_user 
    user_ids.append(user_id)
    
    print(f"{new_user.__class__.__name__} ID [{user_id}] saved successfully")
    return sum_age


def get_by_id(users_data: dict) -> None:
    id_input = input("Enter ID number: ")
    user_id = parse_valid_int(id_input)
    if user_id is None:
        return
    
    user = users_data.get(user_id)
    if user:
        user.print_myself()
    else:
        print(f"User id '{user_id}' not found.")


def print_average_age(users_data: dict, sum_age: int) -> None:
    if not check_if_data_exist(users_data):
        return

    average_age = sum_age/len(users_data)
    print(f"The average age is: {average_age}")
 
   
def print_all_names(users_data: dict) -> None:
    if not check_if_data_exist(users_data):
        return

    for user in users_data.values():
        print(user.get_name())


def print_all_ids(users_data: dict) -> None:
    if not check_if_data_exist(users_data):
        return
    for user in users_data.values():
        print(user.get_id())


def print_all_entries(users_data: dict) -> None:
    if not check_if_data_exist(users_data):
        return
    print("All user entries:")
    for user in users_data.values():
        user.print_myself()


def print_entry_by_index(users_data: dict, user_ids: list) -> None:
    index_input = input("Enter index: ")
    index = parse_valid_int(index_input)
    if index is None:
        return
    
    if index < 0 or index >= len(user_ids):
        print("Index out of range.")
        return
    
    user = users_data.get(user_ids[index])
    if user:
        user.print_myself()
    else:
        print("user not found.")


def save_all_data(users_data: dict) -> None:
    if not users_data:
        print("No data to save.")
        return

    file_name = input("What is your output file name? ") 
    if not file_name.endswith(".csv"):
        file_name += ".csv"

    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, file_name)

    try:
        rows = [user.to_dict() for user in users_data.values()]
        data = pd.DataFrame(rows)
        data.to_csv(file_path, index=False)
        print(f"Data saved successfully as '{file_name}'.")
    except Exception as e:
        print(f"Failed to save data '{file_name}]': {e}")


def print_menu() -> None:
    print()
    print("*** Main menu ***")
    for option in MenuOption:
        print(f"{option.value}. {option.name.replace('_', ' ').title()} ")


def start_system() -> None:
    users_data = {}
    sum_age = 0
    user_ids = [] 
    
    while True:
        print_menu()
        
        user_input = parse_valid_int(input("Please enter your choice: "))
        if user_input is None:
            continue

        try:
            selected_option = MenuOption(user_input)

        except ValueError:
            print("Invalid input! Please select a number between 1-9.")
            continue
        
        should_continue = True 

        match selected_option:
            case MenuOption.SAVE_A_NEW_ENTRY:
                updated_sum_age = save_new_entry(users_data, sum_age, user_ids)
                if updated_sum_age:
                    sum_age = updated_sum_age

            case MenuOption.SEARCH_BY_ID:
                get_by_id(users_data)

            case MenuOption.PRINT_AVERAGE_AGE:
                print_average_age(users_data, sum_age)
        
            case MenuOption.PRINT_ALL_NAMES:
                print_all_names(users_data)

            case MenuOption.PRINT_ALL_IDS:
                print_all_ids(users_data)
        
            case MenuOption.PRINT_ALL_ENTRIES:
                print_all_entries(users_data)

            case MenuOption.PRINT_ENTRY_BY_INDEX:
                print_entry_by_index(users_data, user_ids)

            case MenuOption.SAVE_ALL_DATA:
                save_all_data(users_data)
        
            case MenuOption.EXIT:         
                user_answer = input("Are you sure you want to exit? (y/n) ").lower()
                while user_answer not in ('y', 'n'):
                    user_answer = input("Invalid input! Enter 'y' or 'n': ").lower()   

                if user_answer == 'y':
                    print("Exiting the system.. GoodBye!")
                    return 

        if not should_continue:
            return   
        press_enter()

try:
    start_system()
except KeyboardInterrupt:
    print("\nExit requested. Goodbye!")
