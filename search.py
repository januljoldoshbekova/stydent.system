def search_student(name, students):
    for student in students:
        if student == name:
            return student
    return None