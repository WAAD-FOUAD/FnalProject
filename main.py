class Course:
    # Class variable to keep track of the incrementing course IDs
    course_id = 1

    # Constructor
    def __init__(self, course_name, course_level):
        self.course_id = Course.course_id
        Course.course_id += 1
        self.course_name = course_name
        self.course_level = course_level


# create class student
class Student:
    # Class variable to keep track of the incrementing course IDs
    student_id = 1

    # Constructor
    def __init__(self, student_name, student_level):
        self.student_id = Student.student_id
        Student.student_id += 1
        self.student_name = student_name
        self.student_level = student_level
        # There is no specific list,so it has not been placed as a variable in the constructor
        self.student_courses = []

    def add_course(self, course):
        if course.course_level == self.student_level:
            self.student_courses.append(course)
            print(f"Course '{course.course_name}' added to student '{self.student_name}'.")

    def display_details(self):
        print("Name:", self.student_name)
        print("Class:", self.student_level)
        print("Courses Enrolled:", [course.course_name for course in self.student_courses])


class Main:
    def __init__(self):
        self.students = []  # List to store student objects
        self.courses = []   # List to store course objects

    def add_new_student(self):
        name = input("Enter student name: ")
        level = input("Select student level (A/B/C): ").upper()
        while level not in ['A', 'B', 'C']:
            level = input("Invalid input. Select student level (A/B/C): ").upper()
        student = Student(name, level)   # Create a new student object
        self.students.append(student)    # Add the student object to the list

        print("Student saved successfully.")

    def remove_student(self):
        student_id = int(input("Enter student ID: "))
        student_to_remove = None  # ????
        for student in self.students:
            if student.student_id == student_id:
                student_to_remove = student
                break
        if student_to_remove:
            self.students.remove(student_to_remove)
            print("Student deleted successfully.")
        else:
            print("Student not exist.")

    def edit_student(self):
        student_id = int(input("Enter student ID: "))
        student_to_edit = None
        for student in self.students:
            if student.student_id == student_id:
                student_to_edit = student
                break
        if student_to_edit:
            new_name = input("Enter new name: ")
            new_level = input("Select new level (A/B/C): ").upper()
            while new_level not in ['A', 'B', 'C']:
                new_level = input("Invalid input. Select new level (A/B/C): ").upper()
            student_to_edit.student_name = new_name
            student_to_edit.student_level = new_level
            print("Student details updated successfully.")
        else:
            print("Student not found.")

    def display_all_students(self):
        for student in self.students:
            student.display_details()

    def create_new_course(self):
        course_name = input("Enter course name: ")
        course_level = input("Select course level (A/B/C): ").upper()
        while course_level not in ['A', 'B', 'C']:
            course_level = input("Invalid input. Select course level (A/B/C): ").upper()
        course = Course(course_name, course_level)
        self.courses.append(course)
        print("Course created successfully.")

    def add_course_to_student(self):
        student_id = int(input("Enter student ID: "))
        student_to_enroll = None
        for student in self.students:
            if student.student_id == student_id:
                student_to_enroll = student
                break
        if student_to_enroll:
            course_id = int(input("Enter course ID: "))
            course_to_enroll = None
            for course in self.courses:
                if course.course_id == course_id:
                    course_to_enroll = course
                    break
            if course_to_enroll:
                student_to_enroll.add_course(course_to_enroll)
                print("Course added to student successfully.")
            else:
                print("Course not found.")
        else:
            print("Student not found.")

    def main_menu(self):
        while True:
            print("Select choice please:")
            print("1. Add new student")
            print("2. Remove student")
            print("3. Edit student")
            print("4. Display all students")
            print("5. Create new course")
            print("6. Add course to student")
            print("0. Exit")
            choice = input()

            if choice == "1":
                self.add_new_student()
            elif choice == "2":
                self.remove_student()
            elif choice == "3":
                self.edit_student()
            elif choice == "4":
                self.display_all_students()
            elif choice == "5":
                self.create_new_course()
            elif choice == "6":
                self.add_course_to_student()
            elif choice == "0":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main = Main()  # Create a Main object to start the program
    main.main_menu()

