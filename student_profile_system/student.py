from utils import get_student_by_id

def handle_student_operations(users):
    while True:
        print("\nStudent Dashboard:\n1. View Profile\n2. Update Profile\n3. View Grades\n4. View ECA\n5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            student_id = input("Enter your student ID: ")
            student = get_student_by_id(users, student_id)
            if student:
                print(student.get_details())
            else:
                print("Student not found.")
        elif choice == '2':
            student_id = input("Enter your student ID: ")
            student = get_student_by_id(users, student_id)
            if student:
                new_username = input("Enter new username: ")
                new_password = input("Enter new password: ")
                student.update_profile(new_username, new_password)
                print("Profile updated successfully.")
            else:
                print("Student not found.")
        elif choice == '3':
            student_id = input("Enter your student ID: ")
            student = get_student_by_id(users, student_id)
            if student:
                print(f"Grades: {student.view_grades()}")
            else:
                print("Student not found.")
        elif choice == '4':
            student_id = input("Enter your student ID: ")
            student = get_student_by_id(users, student_id)
            if student:
                print(f"ECA: {student.view_eca()}")
            else:
                print("Student not found.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")
