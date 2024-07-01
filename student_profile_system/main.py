from admin import handle_admin_operations
from student import handle_student_operations
from utils import load_users, save_users, login, setup_logging

def main():
    setup_logging()
    users = load_users()

    while True:
        print("Login:\n")
        username = input("Enter username: ")
        password = input("Enter password: ")

        user = login(users, username, password)
        if user:
            if user.role == 'admin':
                handle_admin_operations(users)
            elif user.role == 'student':
                handle_student_operations(users)
        else:
            print("Invalid username or password.")

        save_users(users)

if __name__ == "__main__":
    main()
      