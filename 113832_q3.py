class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print(f"Employee ID: {self.employee_id}, Name: {self.name}, Salary: {self.salary}")

    def update_salary(self, new_salary):
        print(f"Updating salary for {self.name} from {self.salary} to {new_salary}.")
        self.salary = new_salary


class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Employee '{employee.name}' added to the {self.department_name} department.")

    def calculate_total_salary_expenditure(self):
        total_salary = sum(employee.salary for employee in self.employees)
        print(f"\nTotal salary expenditure for {self.department_name} department: {total_salary}")
        return total_salary

    def display_all_employees(self):
        print(f"\nEmployees in the {self.department_name} department:")
        if self.employees:
            for employee in self.employees:
                employee.display_details()
        else:
            print("No employees in this department.")


# Main Program
def main():
    department_name = input("Enter the department name: ").strip()
    department = Department(department_name)

    while True:
        print("\nDepartment Menu")
        print("1. Add an Employee")
        print("2. Display All Employees")
        print("3. Update Employee Salary")
        print("4. Display Total Salary Expenditure")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == '1':
            emp_name = input("Enter the employee's name: ").strip()
            emp_id = input("Enter the employee's ID: ").strip()
            emp_salary = float(input("Enter the employee's salary: ").strip())
            new_employee = Employee(emp_name, emp_id, emp_salary)
            department.add_employee(new_employee)

        elif choice == '2':
            department.display_all_employees()

        elif choice == '3':
            emp_id = input("Enter the employee ID to update salary for: ").strip()
            new_salary = float(input("Enter the new salary: ").strip())
            employee = next((emp for emp in department.employees if emp.employee_id == emp_id), None)
            if employee:
                employee.update_salary(new_salary)
            else:
                print(f"No employee found with ID {emp_id}.")

        elif choice == '4':
            department.calculate_total_salary_expenditure()

        elif choice == '5':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

# Run the employee and department management system
main()
