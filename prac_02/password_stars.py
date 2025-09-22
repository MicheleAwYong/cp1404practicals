MINIMUM_LENGTH = 4
def main():
    password = get_password()
    print_asterisks(password)
def get_password():
    password = input("Enter password: ")
    while len(password) < MINIMUM_LENGTH:
        print("Password is too short.")
        password = input("Enter password: ")
    return password
def print_asterisks(password):
    print('*' * len(password))
main()
"This is for the Github"