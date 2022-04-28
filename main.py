class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in \
                self.courses_in_progress or course in self.finished_courses:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        all_grades = []
        for course in self.grades:
            all_grades.extend(self.grades[course])
        if len(all_grades) > 0:
            average_grade = round(sum(all_grades) / len(all_grades), 1)
        else:
            average_grade = 0

        some_student = f'имя:{self.name} фамилия:{self.surname}\n'
        some_student += f'Средняя оценка:{self.grades}\n'
        some_student += f'Курсы в процессе обучения:{self.courses_in_progress}\n'
        some_student += f'Завершенные курсы:{self.finished_courses}\n'
        return some_student

    def __lt__(self, compare):
        if isinstance(compare, Student):
            self_grades = []
            compare_grades = []
            for course in self.grades:
                self_grades.extend(self.grades[course])
            if len(self_grades) > 0:
                self_average_grade = sum(self_grades) / len(self_grades)
            else:
                self_average_grade = 0
            for course in compare.grades:
                compare_grades.extend(compare.grades[course])
            if len(compare_grades) > 0:
                compare_average_grades = sum(compare_grades) / len(compare_grades)
            else:
                compare_average_grades = 0

            return self_average_grade < compare_average_grades


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        all_grades = []
        for course in self.grades:
            all_grades.extend(self.grades[course])
        if len(all_grades) > 0:
            average_grade = round(sum(all_grades) / len(all_grades), 2)
        else:
            average_grade = 0
        some_lecturer = f'имя:{self.name} фамилия:{self.surname}\n'
        some_lecturer += f'Средняя оценка за лекции:{average_grade}\n'
        return some_lecturer

    def __lt__(self, compare):
        if isinstance(compare, Lecturer):
            self_grades = []
            compare_grades = []
            for courses in self.grades:
                self_grades.extend(self.grades[courses])
            for courses in compare.grades:
                compare_grades.extend(compare.grades[courses])
            if len(self_grades) > 0:
                self_average_grade = sum(self_grades) / len(self_grades)
            else:
                self_average_grade = 0
            if len(compare_grades) > 0:
                compare_average_grades = sum(compare_grades) / len(compare_grades)
            else:
                compare_average_grades = 0
            return self_average_grade < compare_average_grades


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and isinstance(self, Reviewer) and
                course in self.courses_attached and course in
                student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        some_reviewer = f'имя:{self.name} фамилия:{self.surname}'
        return some_reviewer


def student_average_grade(students, course):
    all_grades = []
    for student in students:
        if course in student.grades:
            all_grades.extend(student.grades[course])
    if len(all_grades) > 0:
        average_grade = round(sum(all_grades) / len(all_grades), 1)
    else:
        return f"Студентам за {course} оценки пока не выставлены."
    return f"Средняя оценка студентам за {course}: {average_grade}"


def lecturer_average_grade(lecturers, course):
    all_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            all_grades.extend(lecturer.grades[course])
    if len(all_grades) > 0:
        average_grade = round(sum(all_grades) / len(all_grades), 1)
    else:
        return f"Лекторам за {course} оценки пока не выставлены."
    return f"Средняя оценка лекторам за {course}: {average_grade}"


def main():
    student1 = Student('Иван', 'Иванов', 'муж')
    student2 = Student('Ольга', 'Ольгина', 'жен')
    lecturer1 = Lecturer('Алексей', 'Алексеев')
    lecturer2 = Lecturer('Петр', 'Петров')
    reviewer1 = Reviewer('Борис', 'Годунов')
    reviewer2 = Reviewer('Николай', 'Романов')

    student1.finished_courses += ['GIT', 'Javascript']
    student2.finished_courses += ['Python', 'GIT']
    student1.courses_in_progress += ['Python']
    student2.courses_in_progress += ['SQL', 'Javascript']

    lecturer1.courses_attached += ["Python", "SQL", 'GIT']
    lecturer2.courses_attached += ["GIT", "Javascript"]

    reviewer1.courses_attached += ["SQL", "GIT", "javascript"]
    reviewer2.courses_attached += ["Javascript", "Python"]

    student1.rate_lecturer(lecturer1, 'Python', 9)
    student1.rate_lecturer(lecturer1, 'GIT', 5)
    student1.rate_lecturer(lecturer2, 'Javascript', 8)
    student1.rate_lecturer(lecturer2, 'GIT', 3)

    student2.rate_lecturer(lecturer1, 'Python', 5)
    student2.rate_lecturer(lecturer1, 'SQL', 7)
    student2.rate_lecturer(lecturer1, 'GIT', 3)
    student2.rate_lecturer(lecturer2, 'Javascript', 4)
    student2.rate_lecturer(lecturer2, 'GIT', 10)

    reviewer1.rate_hw(student1, 'GIT', 4)
    reviewer1.rate_hw(student1, 'Javascript', 7)
    reviewer1.rate_hw(student2, 'GIT', 10)
    reviewer1.rate_hw(student2, 'SQL', 6)

    reviewer2.rate_hw(student1, 'Python', 9)
    reviewer2.rate_hw(student1, 'Javascript', 4)
    reviewer2.rate_hw(student2, 'Python', 5)
    reviewer2.rate_hw(student2, 'Javascript', 8)

    print("Студенты:\n")
    print(student1, '\n')
    print(student2, '\n')
    print("Лекторы:\n")
    print(lecturer1, '\n')
    print(lecturer2, '\n')
    print("Аспиранты:\n")
    print(reviewer1, '\n')
    print(reviewer2, '\n')

    print()

    students = [student1, student2]
    lecturers = [lecturer1, lecturer2]
    courses = ["Python", "SQL", "GIT", "Javascript"]
    for course in courses:
        print(lecturer_average_grade(lecturers, course))
        print(student_average_grade(students, course))

    if lecturer1 > lecturer2:
        print(f"Средняя оценка у {lecturer1.name} {lecturer1.surname} выше.")
    else:
        print(f"Средняя оценка у {lecturer2.name} {lecturer2.surname} выше.")

    if student1 > student2:
        print(f"Средняя оценка у {student1.name} {student1.surname} выше.")
    else:
        print(f"Средняя оценка у {student2.name} {student2.surname} выше.")


main()
