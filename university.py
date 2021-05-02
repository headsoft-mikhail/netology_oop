import statistics

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'Name: {self.name} \nSurname: {self.surname}'

class RatedPerson(Person):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def get_average_grade(self, discipline='all'):
        grades = []
        if discipline == 'all':
            for valuesList in self.grades.values():
                grades += valuesList
        elif discipline in self.grades.keys():
            grades = self.grades[discipline]
        if len(grades) > 0:
            return statistics.mean(grades)
        else:
            return 0

    def __str__(self):
        return super().__str__() + f'\nAverage grade: {round(self.get_average_grade(), 2)}'

    def __lt__(self, other):
        if isinstance(other, RatedPerson):
            return self.get_average_grade() < other.get_average_grade()
        else:
            return 'TypeError'

    def __le__(self, other):
        if isinstance(other, RatedPerson):
            return self.get_average_grade() <= other.get_average_grade()
        else:
            return 'TypeError'

    def __eq__(self, other):
        if isinstance(other, RatedPerson):
            return self.get_average_grade() == other.get_average_grade()
        else:
            return 'TypeError'

class EvaluatorPerson(Person):
    def rate(self, rated, discipline, grade):
        evaluation_rights = isinstance(rated, RatedPerson) and 1 <= grade <= 10
        if isinstance(rated, Student) and isinstance(self, Reviewer):
            evaluation_rights &= discipline in self.courses_attached and discipline in rated.courses_in_progress
        elif isinstance(rated, Lecturer) and isinstance(self, Student):
            evaluation_rights &= (discipline in self.courses_in_progress or discipline in self.finished_courses) \
                                 and discipline in rated.courses_attached
        if evaluation_rights:
            if discipline in rated.grades.keys():
                rated.grades[discipline] += [grade]
            else:
                rated.grades[discipline] = [grade]
        else:
            return 'Error'

class Student(RatedPerson, EvaluatorPerson):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.finished_courses = []
        self.courses_in_progress = []

    def __str__(self):
        courses_in_progress_str = ', '.join([course for course in self.courses_in_progress])
        finished_courses_str = ', '.join([course for course in self.finished_courses])
        return super().__str__() + f'\nCourses in progress: {courses_in_progress_str}' \
                                   f'\nFinished courses: {finished_courses_str}'

class Mentor(Person):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def __str__(self):
        return super().__str__() + '\nAttached courses: ' + ', '.join(self.courses_attached)

class Lecturer(Mentor, RatedPerson):
    pass

class Reviewer(Mentor, EvaluatorPerson):
    pass

def average_course_grade(persons, course):
    course_average_grades = []
    for person in persons:
        if isinstance(person, RatedPerson) and course in person.grades.keys():
            course_average_grades.append(person.get_average_grade(course))
    if len(course_average_grades)>0:
        return statistics.mean(course_average_grades)
    else:
        return 0




