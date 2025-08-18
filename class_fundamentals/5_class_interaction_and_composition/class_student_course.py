"""
Create a School system with Students and Courses that interact.

Requirements for Student class:
- Initialize with name, student_id, and empty list of enrolled_courses
- Create method enroll_in_course(course) that adds course to student's list
- Create method drop_course(course_name) that removes course by name
- Create method get_student_summary() that returns formatted info

Requirements for Course class:
- Initialize with course_name, course_code, max_students (default: 30)
- Create method add_student(student) that adds student if room available
- Create method remove_student(student_name) that removes student by name
- Create method is_full() that returns True if at max capacity
- Create method get_course_info() that returns course details and enrollment count

Test your system:
student1 = Student("Alice", "S001")
student2 = Student("Bob", "S002")
course1 = Course("Python Programming", "CS101", 2)  # Small class for testing

course1.add_student(student1)
student1.enroll_in_course(course1)
course1.add_student(student2)
student2.enroll_in_course(course1)

print(course1.is_full())  # Should print True
print(student1.get_student_summary())  # Should show enrolled course
"""


class Course:
    def __init__(self, course_name, course_code, max_students=30):
        self.course_name = course_name
        self.course_code = course_code
        self.max_students = max_students
        self.enrolled_students = []

    def add_student(self, student):
        if self.is_full():
            return False

        self.enrolled_students.append(student)
        return True

    def is_full(self):
        return len(self.enrolled_students) >= self.max_students

    def remove_student(self, student_name):
        for enrolled_student in self.enrolled_students:
            if enrolled_student.name == student_name:
                self.enrolled_students.remove(enrolled_student)
                break

    def get_course_info(self):
        return f"Course name: {self.course_name}, course code: {self.course_code}, enrollment count: {len(self.enrolled_students)}"


class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.enrolled_courses = []

    def enroll_in_course(self, course):
        self.enrolled_courses.append(course)

    def drop_course(self, course_name):
        for enrolled_course in self.enrolled_courses:
            if enrolled_course.course_name == course_name:
                self.enrolled_courses.remove(enrolled_course)
                break

    def get_student_summary(self):
        enrolled_courses_names = [
            enrolled_course.course_name for enrolled_course in self.enrolled_courses
        ]
        return f"Student name: {self.name}, ID: {self.student_id}, enrolled_courses: {enrolled_courses_names}"


student1 = Student("Alice", "S001")
student2 = Student("Bob", "S002")
course1 = Course("Python Programming", "CS101", 2)  # Small class for testing

course1.add_student(student1)
student1.enroll_in_course(course1)
course1.add_student(student2)
student2.enroll_in_course(course1)

print(course1.is_full())  # Should print True
print(student1.get_student_summary())  # Should show enrolled course
