import os
import json
import pandas as pd


def is_exist(user_id, users_data):
    if user_id in users_data:
        print(f"Error: ID already exist! Please try again.")
        return True
    return False


def is_number(user_id):
    if not user_id.isdigit():
        print(f"Error: Invalid input! {user_id} is not a number.")
        return False
    return True


def check_if_data_exist(users_data):
    if not users_data:
        print("No users found.")
        return False
    return True


def print_entry(user_id, user):
    print(f"ID: {user_id}, Name: {user['username']}, Age: {user['age']}")


def press_enter():
    input("Press Enter to continue.")


def save_json_file():
    my_dict = {
        "id": "id",
        "name": "name",
        "age": "age"
    }

    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, "conf.json")

    if not os.path.exists(file_path):
        with open(file_path, "w") as json_file:
            json.dump(my_dict, json_file, indent=4)   
        

def save_new_entry(users_data, sum_age, user_ids):
    user_id = input("ID: ")
    if not is_number(user_id):
        return 
    if is_exist(user_id, users_data):
        return 
 
    username = input("Name: ")
    user_age = input("Age: ")

    if not is_number(user_age):
        return 
    
    sum_age += int(user_age)
    users_data[user_id] = {
        "username": username,
        "age": int(user_age)
            }
    
    user_ids.append(user_id)
    
    print(f"ID [{user_id}] saved successfully")
    return sum_age


def get_by_id(users_data):
    user_id = input("Enter ID number: ")
    if not is_number(user_id):
        return 
    if user_id in users_data:
        user = users_data[user_id]
        print_entry(user_id, user)
    else:
        print(f"User id '{user_id}' not found.")


def print_average_age(users_data, sum_age):
    if not check_if_data_exist(users_data):
        return

    average_age = sum_age/len(users_data)
    print(f"The average age is: {average_age}")
 
   
def print_all_names(users_data):
    if not check_if_data_exist(users_data):
        return
    for user in users_data.values():
        print(user["username"])


def print_all_ids(users_data):
    if not check_if_data_exist(users_data):
        return
    for user_id in users_data:
        print(user_id)


def print_all_entries(users_data):
    if not check_if_data_exist(users_data):
        return
    print("All user entries:")
    for user_id, user in users_data.items():
        print_entry(user_id, user)


def print_entry_by_index(users_data, user_ids):
    index = input("Enter index: ")
    if not is_number(index):
        return
    
    index = int(index)
    if index < 0 or index >= len(user_ids):
        print("Index out of range.")
        return
    
    user_id = user_ids[index]
    user = users_data[user_id]
    print_entry(user_id, user)


def save_all_data(users_data):
    if not users_data:
        print("No data to save.")
        return

    save_json_file()
    file_name = input("What is your output file name? ") + ".csv"
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, file_name)

    conf_path = os.path.join(current_dir, "conf.json")
    with open(conf_path) as json_file:
        json_data = json.load(json_file)

    rows = [
        {
            json_data["id"]: u_id, 
            json_data["name"]: user["username"], 
            json_data["age"]: user["age"]
        } 
        for u_id, user in users_data.items()
        ]

    data = pd.DataFrame(rows)
    data.to_csv(file_path)

            
def print_menu():
    print()
    print("*** Main menu ***")
    print("1. Save a new entry")
    print("2. Search by ID")
    print("3. Print average age")
    print("4. Print all names")
    print("5. Print all ID's")
    print("6. Print all entries")
    print("7. Print entry by index")
    print("8. Save all data")
    print("9. Exit")


# Note: Match-case could be used here.
def start_system():
    users_data = {}
    sum_age = 0
    user_ids = [] 
    
    while True:
        print_menu()
        user_input = input("Please enter your choice: ")
        if not is_number(user_input):
            continue
        user_input = int(user_input)

        if user_input == 0 or user_input > 9:
            print("Invalid input! Please select a number between 1-9.")
            continue
        
        elif user_input == 1:
            updated_sum_age = save_new_entry(users_data, sum_age, user_ids)
            if updated_sum_age:
                sum_age = updated_sum_age


        elif user_input == 2:
            get_by_id(users_data)

        elif user_input == 3:
            print_average_age(users_data, sum_age)
      
        elif user_input == 4:
            print_all_names(users_data)

        elif user_input == 5:
            print_all_ids(users_data)
       
        elif user_input == 6:
            print_all_entries(users_data)

        elif user_input == 7:
            print_entry_by_index(users_data, user_ids)

        elif user_input == 8:
            save_all_data(users_data)
      
        elif user_input  == 9:         
            user_answer = input("Are you sure you want to exit? (y/n) ").lower()
            while user_answer not in ('y', 'n'):
                user_answer = input("Invalid input! Enter 'y' or 'n': ").lower()   

            if user_answer == 'y':
                print("Exiting the system.. GoodBye!")
                return 
        press_enter()


start_system()
