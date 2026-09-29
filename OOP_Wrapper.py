# ============================================================
# Employee Management System
# ============================================================

print("Welcome to Employee Management System....")


# ------------------------------------------------------------
# PERSON CLASS
# ------------------------------------------------------------

class Person:

    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Display method
    def display(self):
        print("\nPerson Details:")
        print("Name:", self.name)
        print("Age:", self.age)

    # Destructor
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

    # Getter for Employee ID
    def get_employee_id(self):
        return self.__employee_id

    # Setter for Employee ID
    def set_employee_id(self, employee_id):

        if employee_id == "":
            print("Employee ID cannot be empty.")
            return

        self.__employee_id = employee_id

    # Getter for Salary
    def get_salary(self):
        return self.__salary

    # Setter for Salary
    def set_salary(self, salary):

        salary = float(salary)

        if salary < 0:
            print("Salary cannot be negative.")
            return

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
        except:
            pass


# ------------------------------------------------------------
# MANAGER CLASS
# ------------------------------------------------------------

class Manager(Employee):

    # Constructor
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

    # Constructor
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

    name = input("\nEnter Name: ")
    age = int(input("Enter Age: "))

    person = Person(name, age)

    print(
        f"\nPerson created with name: "
        f"{name} and age: {age}."
    )

    return person


# ------------------------------------------------------------
# CREATE EMPLOYEE
# ------------------------------------------------------------

def create_employee():

    name = input("\nEnter Name: ")
    age = int(input("Enter Age: "))
    employee_id = input("Enter Employee ID: ")
    salary = float(input("Enter Salary: "))

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


# ------------------------------------------------------------
# CREATE MANAGER
# ------------------------------------------------------------

def create_manager():

    name = input("\nEnter Name: ")
    age = int(input("Enter Age: "))
    employee_id = input("Enter Employee ID: ")
    salary = float(input("Enter Salary: "))
    department = input("Enter Department: ")

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


# ------------------------------------------------------------
# CREATE DEVELOPER
# ------------------------------------------------------------

def create_developer():

    name = input("\nEnter Name: ")
    age = int(input("Enter Age: "))
    employee_id = input("Enter Employee ID: ")
    salary = float(input("Enter Salary: "))
    programming_language = input(
        "Enter Programming Language: "
    )

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


# ------------------------------------------------------------
# SHOW DETAILS
# ------------------------------------------------------------

def show_details(persons, employees):

    print("\nChoose details to show:")
    print("1. Person")
    print("2. Employee")
    print("3. Manager")
    print("4. Developer")
    print("5. All")

    choice = input("Enter your choice: ").strip()

    # Person
    if choice == "1":

        if len(persons) > 0:

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

    # Object references
    person = None
    employee = None
    manager = None
    developer = None

    print("\n==============================================")
    print("       PYTHON OOP PROJECT: EMPLOYEE")
    print("           MANAGEMENT SYSTEM")
    print("==============================================")

    show_another = False

    while True:

        if show_another:
            print("\n--- Choose another operation ---")
            show_another = False
        else:
            print("\n--- Choose an operation ---")

        print("\nChoose an operation:")
        print("1. Create a Person")
        print("2. Create an Employee")
        print("3. Create a Manager")
        print("4. Create a Developer")
        print("5. Show Details")
        print("6. Exit")

        choice = input("\nEnter your choice: ").strip()

        # ----------------------------------------------------
        # CREATE PERSON
        # ----------------------------------------------------

        if choice == "1":

            person = create_person()
            persons.append(person)

        # ----------------------------------------------------
        # CREATE EMPLOYEE
        # ----------------------------------------------------

        elif choice == "2":

            employee = create_employee()
            employees.append(employee)

        # ----------------------------------------------------
        # CREATE MANAGER
        # ----------------------------------------------------

        elif choice == "3":

            manager = create_manager()
            employees.append(manager)

        # ----------------------------------------------------
        # CREATE DEVELOPER
        # ----------------------------------------------------

        elif choice == "4":

            developer = create_developer()
            employees.append(developer)

        # ----------------------------------------------------
        # SHOW DETAILS
        # ----------------------------------------------------

        elif choice == "5":

            show_details(
                persons,
                employees
            )

            show_another = True

        # ----------------------------------------------------
        # EXIT
        # ----------------------------------------------------

        elif choice == "6":

            print(
                "\nExiting the system. "
                "All resources have been freed."
            )

            print("Goodbye!")

            # Delete references
            developer = None
            manager = None
            employee = None
            person = None

            # Clear remaining objects
            employees.clear()
            persons.clear()

            break

        # ----------------------------------------------------
        # INVALID CHOICE
        # ----------------------------------------------------

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