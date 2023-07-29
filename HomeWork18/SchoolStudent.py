from Student import Student
class School:

    def __init__(self, students):
        self.students = students

    def get_list_of_students(self):
        return self.students

    def admission(self, student):
        self.students.append(student)

    def remove(self, student, group):
        if student.group == group:
            self.students.remove(student)

    def print_student_names(self): #
        for student in self.students:
            print(student.name)

    def get_list_automate_students(self, auto_mark=7): # Вывод ученика у которого балл равен или больше 7
        list_students_automate = []
        for student in self.students:
            average_grade = sum(student.progress)/ len(student.progress)
            if average_grade >= auto_mark:
                list_students_automate.append(student)
        return list_students_automate

    def get_list_of_students_with_needed_mark(self, grades=5):
        # list_students = []
        # for student in self.students:
        #     average_grade = sum(student.progress)/ len(student.progress)
        #     if average_grade == grades:
        #         list_students.append(student)
        # return list_students
        list_std = self.students.copy()
        for student in self.students:
            for mark in student.progress:
                if mark not in grades:
                    list_std.remove(student)
                    break
        return list_std

student1 = Student('Misha', '1A', [5, 5, 5, 5, 5])
student2 = Student('Petya', '2B', [7, 8, 9, 9, 10])
school = School([])
school.admission(student1)
school.admission(student2)
print(school.get_list_of_students())
# school.remove(student1, '1A') # Удаление студента
# print(school.get_list_of_students()) # Удаление студента
school.print_student_names() #
print(school.get_list_automate_students())
#print(school.get_list_of_students_with_needed_mark())
print(school.get_list_of_students_with_needed_mark([5]))
