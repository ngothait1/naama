
def is_exist(user_id:int, users_data:dict) -> bool:
    if user_id in users_data:
        print(f"Error: ID already exist! Please try again.")
        return True
    return False


def parse_valid_int(value: str) -> int | None:
    if not value.strip().isdigit():
        print(f"Invalid input! '{value}' is not a number.")
        return None
    return int(value)


def check_if_data_exist(users_data:dict) -> bool:
    if not users_data:
        print("No users found.")
        return False
    return True


def press_enter() -> None:
    input("Press Enter to continue.")