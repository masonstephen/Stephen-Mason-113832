class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}

    def add_assignment(self, assignment_name, grade):
        self.assignments[assignment_name] = grade
        print(f"Assignment '{assignment_name}' added for {self.name} with grade {grade}.")

    def display_grades(self):
        print(f"\nGrades for {self.name} (ID: {self.student_id}):")
        if self.assignments:
            for assignment, grade in self.assignments.items():
                print(f"- {assignment}: {grade}")
        else:
            print("No assignments recorded.")


class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Student '{student.name}' (ID: {student.student_id}) added to the course '{self.course_name}'.")

    def assign_grade(self, student_id, assignment_name, grade):
        student = next((s for s in self.students if s.student_id == student_id), None)
        if student:
            student.add_assignment(assignment_name, grade)
        else:
            print(f"No student found with ID {student_id}.")

    def display_all_students_grades(self):
        print(f"\nAll students and their grades in the course '{self.course_name}':")
        if self.students:
            for student in self.students:
                student.display_grades()
        else:
            print("No students enrolled in this course.")

# Initial Data
instructor = Instructor("Dr. Smith", "Computer Science 101")

# Main Program
def main():
    print(f"Welcome to the {instructor.course_name} Management System")

    while True:
        print("\nInstructor Menu")
        print("1. Add a Student")
        print("2. Assign a Grade")
        print("3. Display All Students and Grades")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == '1':
            student_name = input("Enter the student's name: ").strip()
            student_id = input("Enter the student's ID: ").strip()
            new_student = Student(student_name, student_id)
            instructor.add_student(new_student)

        elif choice == '2':
            student_id = input("Enter the student ID to assign a grade to: ").strip()
            assignment_name = input("Enter the assignment name: ").strip()
            grade = input("Enter the grade: ").strip()
            instructor.assign_grade(student_id, assignment_name, grade)

        elif choice == '3':
            instructor.display_all_students_grades()

        elif choice == '4':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

# Run the course management system
main()
