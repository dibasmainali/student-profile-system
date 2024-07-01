import logging


def setup_logging():
    logging.basicConfig(filename='app.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

def load_users():
    users = []
    try:
        with open('users.txt', 'r') as file:
            for line in file:
                user_data = line.strip().split(',')
                if user_data[10] == 'student':
                    grades = {}  # Load grades if any
                    eca = []     # Load ECA activities if any
                    users.append(Student(user_data[0], user_data[1], user_data[2], user_data[3], grades, eca))
                else:
                    users.append(User(user_data[0], user_data[1], user_data[2], user_data[3]))
    except FileNotFoundError:
        logging.error("users.txt file not found.")
    return users

def save_users(users):
    with open('users.txt', 'w') as file:
        for user in users:
            file.write(f"{user.id},{user.username},{user.password},{user.role}\n")

def login(users, username, password):
    for user in users:
        if user.username == username and user.password == password:
            logging.info(f"{username} logged in successfully.")
            return user
    logging.warning(f"Failed login attempt for username: {username}")
    return None

def register_user(users):
    user_id = input("Enter user ID: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    role = input("Enter role (admin/student): ")

    if role == 'student':
        new_user = Student(user_id, username, password, role)
    else:
        new_user = User(user_id, username, password, role)

    users.append(new_user)
    logging.info(f"New user registered: {username}")

def get_user_by_id(users, user_id):
    for user in users:
        if user.id == user_id:
            return user
    logging.warning(f"User ID not found: {user_id}")
    return None

def get_student_by_id(users, student_id):
    for user in users:
        if user.id == student_id and user.role == 'student':
            return user
    logging.warning(f"Student ID not found: {student_id}")
    return None
import logging
from user import User, Student

def setup_logging():
    logging.basicConfig(filename='app.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

def load_users():
    users = []
    try:
        with open('users.txt', 'r') as file:
            for line in file:
                user_data = line.strip().split(',')
                if user_data[3] == 'student':
                    grades = load_grades(user_data[0])
                    eca = load_eca(user_data[0])
                    users.append(Student(user_data[0], user_data[1], user_data[2], user_data[3], grades, eca))
                else:
                    users.append(User(user_data[0], user_data[1], user_data[2], user_data[3]))
    except FileNotFoundError:
        logging.error("users.txt file not found.")
    return users

def save_users(users):
    with open('users.txt', 'w') as file:
        for user in users:
            file.write(f"{user.id},{user.username},{user.password},{user.role}\n")
            if user.role == 'student':
                save_grades(user.id, user.grades)
                save_eca(user.id, user.eca)

def login(users, username, password):
    for user in users:
        if user.username == username and user.password == password:
            logging.info(f"{username} logged in successfully.")
            return user
    logging.warning(f"Failed login attempt for username: {username}")
    return None

def register_user(users):
    user_id = input("Enter user ID: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    role = input("Enter role (admin/student): ")

    if role == 'student':
        new_user = Student(user_id, username, password, role)
    else:
        new_user = User(user_id, username, password, role)

    users.append(new_user)
    logging.info(f"New user registered: {username}")

def get_user_by_id(users, user_id):
    for user in users:
        if user.id == user_id:
            return user
    logging.warning(f"User ID not found: {user_id}")
    return None

def get_student_by_id(users, student_id):
    for user in users:
        if user.id == student_id and user.role == 'student':
            return user
    logging.warning(f"Student ID not found: {student_id}")
    return None

def load_grades(student_id):
    grades = {}
    try:
        with open('grades.txt', 'r') as file:
            for line in file:
                data = line.strip().split(',')
                if data[0] == student_id:
                    grades[data[1]] = data[2]
    except FileNotFoundError:
        logging.error("grades.txt file not found.")
    return grades

def save_grades(student_id, grades):
    with open('grades.txt', 'a') as file:
        for subject, grade in grades.items():
            file.write(f"{student_id},{subject},{grade}\n")

def load_eca(student_id):
    eca = []
    try:
        with open('eca.txt', 'r') as file:
            for line in file:
                data = line.strip().split(',')
                if data[0] == student_id:
                    eca.append(data[1])
    except FileNotFoundError:
        logging.error("eca.txt file not found.")
    return eca

def save_eca(student_id, eca):
    with open('eca.txt', 'a') as file:
        for activity in eca:
            file.write(f"{student_id},{activity}\n")
