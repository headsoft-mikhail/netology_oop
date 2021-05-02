from university import *

reviewers = [Reviewer('Gyaurlya', 'Serkeubaeva'), Reviewer('Alla', 'Valerevna')]
reviewers[0].courses_attached.append('Python')
reviewers[1].courses_attached.append('Git')
for reviewer in reviewers:
    print(reviewer)
    print('__')

students = [Student('Mike', 'Myers'), Student('Jim', 'Carey')]
students[0].courses_in_progress.append('Python')
students[0].courses_in_progress.append('Git')
students[0].finished_courses.append('Starter programming')
students[0].grades['Starter programming'] = [7]
students[0].grades['Starter programming'] += [9]

students[1].courses_in_progress.append('Python')
students[1].courses_in_progress.append('Git')
students[1].finished_courses.append('Starter programming')
students[1].grades['Starter programming'] = [10]
students[1].grades['Starter programming'] += [9]
for student in students:
    print(student)
    print('__')

reviewers[0].rate(students[0], 'Python', 8)
reviewers[0].rate(students[1], 'Python', 10)
reviewers[1].rate(students[0], 'Git', 6)
reviewers[1].rate(students[1], 'Git', 8)

for student in students:
    print(student)
    print('__')

print(students[1] == students[1])
print(students[1] >= students[1])
print(students[0] > students[1])
print('__')

lecturers = [Lecturer('Maral', 'Kasengaziyeva'), Lecturer('Irina', 'Stanislavovna')]
lecturers[0].courses_attached.append('Python')
lecturers[0].courses_attached.append('Java')
lecturers[1].courses_attached.append('Git')
for lecturer in lecturers:
    print(lecturer)
    print('__')

students[0].rate(lecturers[0], 'Python', 10)
students[1].rate(lecturers[0], 'Python', 9)
students[0].rate(lecturers[1], 'Git', 8)
students[1].rate(lecturers[1], 'Git', 8)
for lecturer in lecturers:
    print(lecturer)
    print('__')

print(lecturers[0] == lecturers[1])
print(lecturers[0] >= lecturers[1])
print(lecturers[0] > lecturers[1])

print('__')
print(average_course_grade(students, 'Python'))
print(average_course_grade(lecturers, 'Python'))
print(average_course_grade(students, 'Starter programming'))
print(average_course_grade(lecturers, 'Starter programming'))

print(Student.mro())
print(Lecturer.mro())
print(Reviewer.mro())
