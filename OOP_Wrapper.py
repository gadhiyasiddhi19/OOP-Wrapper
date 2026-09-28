# ============================================================
# Employee Management System
# ============================================================

print("Welcome to Employee Management System....")


# ------------------------------------------------------------
# PERSON CLASS
# ------------------------------------------------------------

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("\nPerson Details:")
        print("Name:", self.name)
        print("Age:", self.age)

    def __del__(self):
        pass


# ------------------------------------------------------------
# EMPLOYEE CLASS
# ------------------------------------------------------------

class Employee:

    # Constructor
    def __init__(self, name, age, employee_id, salary):

        self.name = name
        self.age = age

        # Private attributes
        self.__employee_id = ""
        self.__salary = 0.0

        self.set_employee_id(employee_id)
        self.set_salary(salary)

    # Getter for employee_id
    def get_employee_id(self):
        return self.__employee_id

    # Setter for employee_id
    def set_employee_id(self, employee_id):

        if employee_id == "":
            raise ValueError("Employee ID cannot be empty.")

        self.__employee_id = employee_id

    # Getter for salary
    def get_salary(self):
        return self.__salary

    # Setter for salary
    def set_salary(self, salary):

        salary = float(salary)

        if salary < 0:
            raise ValueError("Salary cannot be negative.")

        self.__salary = salary

    # Alternative Constructor
    @classmethod
    def from_dict(cls, data):

        return cls(
            data.get("name", ""),
            data.get("age", 0),
            data.get("employee_id", ""),
            data.get("salary", 0)
        )

    # Display method
    def display(self):

        print("\nEmployee Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.__employee_id)
        print(f"Salary: ${self.__salary:.2f}")

    # Destructor
    def __del__(self):
        try:
            print(
                f"Resource cleanup completed for {self.name}."
            )
        except AttributeError:
            pass


# ------------------------------------------------------------
# MANAGER CLASS
# ------------------------------------------------------------

class Manager(Employee):

    def __init__(
        self,
        employee_id,
        name,
        age,
        salary,
        department
    ):

        # Calling parent constructor
        super().__init__(
            name,
            age,
            employee_id,
            salary
        )

        self.department = department

    # Method Overriding
    def display(self):

        super().display()
        print("Department:", self.department)


# ------------------------------------------------------------
# DEVELOPER CLASS
# ------------------------------------------------------------

class Developer(Employee):

    def __init__(
        self,
        employee_id,
        name,
        age,
        salary,
        programming_language
    ):

        # Calling parent constructor
        super().__init__(
            name,
            age,
            employee_id,
            salary
        )

        self.programming_language = programming_language

    # Method Overriding
    def display(self):

        super().display()
        print(
            "Programming Language:",
            self.programming_language
        )


# ------------------------------------------------------------
# CREATE PERSON
# ------------------------------------------------------------

def create_person():

    while True:

        try:

            name = input("\nEnter Name: ").strip()

            if name == "":
                print("Name cannot be empty.")
                continue

            age = int(input("Enter Age: "))

            if age < 0:
                print("Age cannot be negative.")
                continue

            person = Person(name, age)

            print(
                f"\nPerson created with name: "
                f"{name} and age: {age}."
            )

            return person

        except ValueError:
            print("Please enter a valid age.")


# ------------------------------------------------------------
# CREATE EMPLOYEE
# ------------------------------------------------------------

def create_employee():

    while True:

        try:

            name = input("\nEnter Name: ").strip()

            if name == "":
                print("Name cannot be empty.")
                continue

            age = int(input("Enter Age: "))

            if age < 0:
                print("Age cannot be negative.")
                continue

            employee_id = input(
                "Enter Employee ID: "
            ).strip()

            salary = float(
                input("Enter Salary: ")
            )

            employee = Employee(
                name,
                age,
                employee_id,
                salary
            )

            print(
                f"\nEmployee created with name: "
                f"{name}, age: {age}, "
                f"ID: {employee.get_employee_id()}, "
                f"and salary: "
                f"${employee.get_salary():.2f}."
            )

            return employee

        except ValueError as error:

            print(
                f"Invalid input: {error}"
            )


# ------------------------------------------------------------
# CREATE MANAGER
# ------------------------------------------------------------

def create_manager():

    while True:

        try:

            name = input("\nEnter Name: ").strip()

            if name == "":
                print("Name cannot be empty.")
                continue

            age = int(input("Enter Age: "))

            if age < 0:
                print("Age cannot be negative.")
                continue

            employee_id = input(
                "Enter Employee ID: "
            ).strip()

            salary = float(
                input("Enter Salary: ")
            )

            department = input(
                "Enter Department: "
            ).strip()

            if department == "":
                print("Department cannot be empty.")
                continue

            manager = Manager(
                employee_id,
                name,
                age,
                salary,
                department
            )

            print(
                f"\nManager created with name: "
                f"{name}, age: {age}, "
                f"ID: {employee_id}, "
                f"salary: ${salary:.2f}, "
                f"and department: {department}."
            )

            return manager

        except ValueError as error:

            print(
                f"Invalid input: {error}"
            )


# ------------------------------------------------------------
# CREATE DEVELOPER
# ------------------------------------------------------------

def create_developer():

    while True:

        try:

            name = input("\nEnter Name: ").strip()

            if name == "":
                print("Name cannot be empty.")
                continue

            age = int(input("Enter Age: "))

            if age < 0:
                print("Age cannot be negative.")
                continue

            employee_id = input(
                "Enter Employee ID: "
            ).strip()

            salary = float(
                input("Enter Salary: ")
            )

            programming_language = input(
                "Enter Programming Language: "
            ).strip()

            if programming_language == "":
                print(
                    "Programming language cannot be empty."
                )
                continue

            developer = Developer(
                employee_id,
                name,
                age,
                salary,
                programming_language
            )

            print(
                f"\nDeveloper created with name: "
                f"{name}, age: {age}, "
                f"ID: {employee_id}, "
                f"salary: ${salary:.2f}, "
                f"and programming language: "
                f"{programming_language}."
            )

            return developer

        except ValueError as error:

            print(
                f"Invalid input: {error}"
            )


# ------------------------------------------------------------
# SHOW DETAILS
# ------------------------------------------------------------

def show_details(persons, employees):

    if not persons and not employees:

        print("\nNo records available.")
        return

    print("\nChoose details to show:")
    print("1. Person")
    print("2. Employee")
    print("3. Manager")
    print("4. Developer")
    print("5. All")

    choice = input("Enter your choice: ").strip()

    # Person
    if choice == "1":

        if persons:

            for person in persons:
                person.display()

        else:

            print("\nNo Person records available.")

    # Employee
    elif choice == "2":

        found = False

        for employee in employees:

            if (
                isinstance(employee, Employee)
                and not isinstance(employee, Manager)
                and not isinstance(employee, Developer)
            ):

                employee.display()
                found = True

        if not found:
            print("\nNo Employee records available.")

    # Manager
    elif choice == "3":

        found = False

        for employee in employees:

            if isinstance(employee, Manager):

                employee.display()
                found = True

        if not found:
            print("\nNo Manager records available.")

    # Developer
    elif choice == "4":

        found = False

        for employee in employees:

            if isinstance(employee, Developer):

                employee.display()
                found = True

        if not found:
            print("\nNo Developer records available.")

    # All
    elif choice == "5":

        print("\n========== ALL DETAILS ==========")

        for person in persons:
            person.display()

        for employee in employees:
            employee.display()

    else:

        print("Invalid choice.")
        return

    # --------------------------------------------------------
    # INHERITANCE CHECKS
    # --------------------------------------------------------

    print("\nInheritance Checks:")

    print(
        "issubclass(Manager, Employee):",
        issubclass(Manager, Employee)
    )

    print(
        "issubclass(Developer, Employee):",
        issubclass(Developer, Employee)
    )

    for employee in employees:

        if isinstance(employee, Manager):

            print(
                f"isinstance({employee.name}, Manager):",
                isinstance(employee, Manager)
            )

        if isinstance(employee, Developer):

            print(
                f"isinstance({employee.name}, Employee):",
                isinstance(employee, Employee)
            )


# ------------------------------------------------------------
# MAIN PROGRAM
# ------------------------------------------------------------

def main():

    persons = []
    employees = []

    print("\n==============================================")
    print("       PYTHON OOP PROJECT: EMPLOYEE")
    print("           MANAGEMENT SYSTEM")
    print("==============================================")

    while True:

        print("\n--- Choose an operation ---")

        print("\nChoose an operation:")
        print("1. Create a Person")
        print("2. Create an Employee")
        print("3. Create a Manager")
        print("4. Create a Developer")
        print("5. Show Details")
        print("6. Exit")

        choice = input("\nEnter your choice: ").strip()

        # Create Person
        if choice == "1":

            person = create_person()
            persons.append(person)

        # Create Employee
        elif choice == "2":

            employee = create_employee()
            employees.append(employee)

        # Create Manager
        elif choice == "3":

            manager = create_manager()
            employees.append(manager)

        # Create Developer
        elif choice == "4":

            developer = create_developer()
            employees.append(developer)

        # Show Details
        elif choice == "5":

            show_details(
                persons,
                employees
            )

            print("\n--- Choose another operation ---")

        # Exit
        elif choice == "6":

            print(
                "\nExiting the system. "
                "All resources have been freed."
            )

            print("Goodbye!")

            # Destructor will clean the objects
            persons.clear()
            employees.clear()

            break

        else:

            print(
                "\nInvalid choice. "
                "Please enter a number from 1 to 6."
            )


# ------------------------------------------------------------
# START PROGRAM
# ------------------------------------------------------------

if __name__ == "__main__":
    main()