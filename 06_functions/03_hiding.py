def get_input():
    input_value = input("Enter a user name: ")
    return input_value


def validate_input(user_name):
    print(f"Validating user: {user_name}")


def save_to_database(user_name):
    print(f"Saving {user_name} to the database.")


def register_user():
    user_name = get_input()
    validate_input(user_name)
    save_to_database(user_name)
    print("User registration complete!")


register_user()
