class User:
    def __init__(self, user_id, username, password, role):
        self.id = user_id
        self.username = username
        self.password = password
        self.role = role

    def get_details(self):
        return f"ID: {self.id}, Username: {self.username}, Role: {self.role}"

    def update_profile(self, username, password):
        self.username = username
        self.password = password

class Student(User):
    def __init__(self, user_id, username, password, role, grades=None, eca=None):
        super().__init__(user_id, username, password, role)
        self.grades = grades or {}
        self.eca = eca or []

    def view_grades(self):
        return self.grades

    def view_eca(self):
        return self.eca

    def update_grades(self, subject, grade):
        self.grades[subject] = grade

    def add_eca(self, activity):
        self.eca.append(activity)
