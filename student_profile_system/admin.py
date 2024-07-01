from utils import register_user, get_user_by_id, get_student_by_id

def handle_admin_operations(users):
    while True:
        print("\nAdmin Dashboard:\n1. Register New User\n2. View Users\n3. Update User Profile\n4. Delete User\n5. Manage Grades\n6. Manage ECA\n7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            register_user(users)
        elif choice == '2':
            for user in users:
                print(user.get_details())
        elif choice == '3':
            user_id = input("Enter user ID to update: ")
            user = get_user_by_id(users, user_id)
            if user:
                new_username = input("Enter new username: ")
                new_password = input("Enter new password: ")
                user.update_profile(new_username, new_password)
                print("Profile updated successfully.")
            else:
                print("User not found.")
        elif choice == '4':
            user_id = input("Enter user ID to delete: ")
            user = get_user_by_id(users, user_id)
            if user:
                users.remove(user)
                print("User deleted successfully.")
            else:
                print("User not found.")
        elif choice == '5':
            student_id = input("Enter student ID: ")
            student = get_student_by_id(users, student_id)
            if student:
                subject = input("Enter subject: ")
                grade = input("Enter grade: ")
                student.update_grades(subject, grade)
                print("Grades updated successfully.")
            else:
                print("Student not found.")
        elif choice == '6':
            student_id = input("Enter student ID: ")
            student = get_student_by_id(users, student_id)
            if student:
                activity = input("Enter activity: ")
                student.add_eca(activity)
                print("ECA updated successfully.")
            else:
                print("Student not found.")
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")
