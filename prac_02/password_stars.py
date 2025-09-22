MINIMUM_LENGTH = 4
def main():
    """Get and check password, then print asterisks."""
    password = get_password()
    print_asterisks(password)
def get_password():
    """Get a password of valid length from the user."""
    password = input("Enter password: ")
    while len(password) < MINIMUM_LENGTH:
        print("Password is too short.")
        password = input("Enter password: ")
    return password
def print_asterisks(password):
    """Print asterisks equal to the length of the password."""
    print('*' * len(password))
main()