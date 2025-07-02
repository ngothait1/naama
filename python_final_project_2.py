
users_data = {}
sum_age = 0


def is_exist(user_id):
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

def press_enter():
    input("Press Enter to continue.")
        
def save_new_entry():
    global sum_age

    user_id = input("ID: ")
    if not is_number(user_id):
        return 
    if is_exist(user_id):
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
    print(f"ID [{user_id}] saved successfully")

def get_by_id(users_data):
    user_id = input("Enter ID number: ")
    if not is_number(user_id):
        return 
    if user_id in users_data:
        user = users_data[user_id]
        print(f"Name: {user['username']}, Age: {user['age']}")
    else:
        print(f"User id '{user_id}' not found.")
        
def print_average_age(users_data):
    global sum_age
    
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
    for user_id, item in users_data.items():
        print(f"ID: {user_id}, Name: {item['username']}, Age: {item['age']}")

def print_entry_by_index(users_data):
    index = input("Enter index: ")
    if not is_number(index):
        return
    
    index = int(index)
    if index < 0 or index >= len(users_data):
        print("Index out of range.")
        return
    for i, user_id in enumerate(users_data):
        user = users_data[user_id]
        if i == index:
            print(f"ID: {user_id}, Name: {user['username']}, Age: {user['age']}")
            return
        
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
    print("8. Exit")

# Note: Match-case could be used here.
def start_system():
    while True:
        print_menu()
        user_input = input("Please enter your choice: ")
        if not is_number(user_input):
            continue
        user_input = int(user_input)

        if user_input == 0 or user_input > 8:
            print("Invalid input! Please select a number between 1-8.")
            continue
        
        elif user_input == 1:
            save_new_entry()
            press_enter()

        elif user_input == 2:
            get_by_id(users_data)
            press_enter()

        elif user_input == 3:
            print_average_age(users_data)
            press_enter()
      
        elif user_input == 4:
            print_all_names(users_data)
            press_enter()

        elif user_input == 5:
            print_all_ids(users_data)
            press_enter()
       
        elif user_input == 6:
            print_all_entries(users_data)
            press_enter()

        elif user_input == 7:
            print_entry_by_index(users_data)
            press_enter()
      
        elif user_input  == 8:         
            user_answer = input("Are you sure you want to exit? (y/n) ").lower()
            while user_answer not in ('y', 'n'):
                user_answer = input("Invalid input! Enter 'y' or 'n': ").lower()   

            if user_answer == 'y':
                print("Exiting the system.. GoodBye!")
                return 

                                     
start_system()
