# Python OOP Project: Employee Management System

**Author:** Siddhi Gadhiya

---

## 📌 Project Description

This is a simple Python menu-driven Employee Management System developed to demonstrate important Object-Oriented Programming (OOP) concepts.

The program allows users to:

* Create a Person.
* Create an Employee.
* Create a Manager.
* Create a Developer.
* Display details of created objects.
* Check inheritance relationships.
* Use encapsulation through private attributes.
* Validate employee ID and salary through setter methods.
* Demonstrate method overriding and `super()`.
* Demonstrate an alternative constructor using `@classmethod`.
* Demonstrate `issubclass()` and `isinstance()`.
* Exit the program when needed.

---

## 🛠️ Technologies Used

* **Python 3.14.6** — Programming language used to develop the Employee Management System.
* **Visual Studio Code (VS Code)** — Development environment used to write and run the project.
* **Python Standard Library** — Built-in Python features used for console input/output, classes, objects, inheritance, validation, and object cleanup.

---

## 📁 Project Structure

The project is organized as follows:

```text
Project-5/

├── employee_management_system.py
└── README.md
```

### File Description

| File                            | Purpose                                                                                                                                                  |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `employee_management_system.py` | Main Python program containing the Person, Employee, Manager, and Developer classes, menu system, validation, OOP demonstrations, and program execution. |
| `README.md`                     | Project documentation containing the description, technologies, project structure, OOP concepts, run instructions, assumptions, and sample output.       |

---

## 🎯 Objective

The main objective of this project is to build an Employee Management System using Python and demonstrate various Object-Oriented Programming concepts.

The project demonstrates:

* Classes and objects
* Constructors
* Destructors
* Encapsulation
* Getters and setters
* Validation
* Inheritance
* Method overriding
* Alternative constructors
* `super()`
* `issubclass()`
* `isinstance()`
* `self`
* Interactive menu-driven programming

---

## 📂 Project Classes

The project contains four main classes:

1. `Person`
2. `Employee`
3. `Manager`
4. `Developer`

The inheritance structure is:

```text
Person

Employee
   |
   +---- Manager
   |
   +---- Developer
```

`Manager` and `Developer` inherit from `Employee`.

---

## 👤 Person Class

The `Person` class represents a basic person.

### Attributes

* `name`
* `age`

### Constructor

```python
def __init__(self, name, age):
    self.name = name
    self.age = age
```

The `self` keyword refers to the current object and is used to store instance attributes.

### Display Method

The `display()` method displays the person's name and age.

---

## 👨‍💼 Employee Class

The `Employee` class represents a basic employee and acts as the parent class for `Manager` and `Developer`.

### Attributes

* `name`
* `age`
* `employee_id`
* `salary`

### Constructor

```python
def __init__(self, name, age, employee_id="", salary=0):
```

The constructor initializes the employee information.

The employee ID and salary are stored using private attributes.

---

## 🔐 Encapsulation

Encapsulation is demonstrated using private attributes:

```python
self.__employee_id
self.__salary
```

These attributes are accessed through getter and setter methods.

### Employee ID Getter

```python
def get_employee_id(self):
    return self.__employee_id
```

### Employee ID Setter

```python
def set_employee_id(self, employee_id):
```

The setter prevents an empty employee ID from replacing the existing value.

### Salary Getter

```python
def get_salary(self):
    return self.__salary
```

### Salary Setter

```python
def set_salary(self, salary):
```

The salary setter checks whether the salary is negative. If the salary is valid, it is stored as a floating-point value.

---

## 🏗️ Constructors

Constructors are implemented using `__init__()`.

Example:

```python
employee = Employee(
    "Madhav Birla",
    29,
    "E123",
    35000
)
```

The constructor initializes the employee's name, age, employee ID, and salary.

---

## 🧹 Destructor

The `Employee` class contains a destructor:

```python
def __del__(self):
    print(
        f"Resource cleanup completed for {self.name}."
    )
```

The destructor demonstrates object cleanup when an Employee object is destroyed.

Since `Manager` and `Developer` inherit from `Employee`, they also use the Employee destructor.

The exact timing and order of destructor execution can depend on Python's object lifecycle.

---

## 🧬 Inheritance

Inheritance allows a child class to reuse the functionality of a parent class.

The `Manager` and `Developer` classes inherit from `Employee`:

```python
class Manager(Employee):
```

```python
class Developer(Employee):
```

Both classes reuse Employee attributes, methods, getters, setters, and the destructor.

---

## 👔 Manager Class

The `Manager` class is derived from `Employee`.

### Additional Attribute

```text
department
```

The Manager constructor first calls the Employee constructor using `super()` and then stores the department.

Example:

```python
class Manager(Employee):
```

The `display()` method is overridden to display the department along with the employee details.

---

## 👨‍💻 Developer Class

The `Developer` class is derived from `Employee`.

### Additional Attribute

```text
programming_language
```

The Developer constructor first calls the Employee constructor using `super()` and then stores the programming language.

Example:

```python
class Developer(Employee):
```

The `display()` method is overridden to display the programming language along with the employee details.

---

## 🔄 Method Overriding

The `Employee` class defines a `display()` method.

The `Manager` and `Developer` classes override this method to add their own specific information.

### Manager

```python
def display(self):

    super().display()
    print(f"Department: {self.department}")
```

### Developer

```python
def display(self):

    super().display()

    print(
        f"Programming Language: "
        f"{self.programming_language}"
    )
```

This demonstrates method overriding because the child classes provide their own implementation of the inherited `display()` method.

---

## ⬆️ Use of `super()`

The `super()` function is used to access methods of the parent class.

### Parent Constructor

Manager and Developer constructors call:

```python
super().__init__(
    name,
    age,
    employee_id,
    salary
)
```

This allows the parent `Employee` constructor to initialize common employee information.

### Parent Display Method

The overridden `display()` methods also call:

```python
super().display()
```

This reuses the Employee display functionality before displaying child-specific information.

---

## 🔀 Alternative Constructor

Python does not provide traditional method overloading in the same way as some other programming languages.

This project demonstrates an alternative constructor using `@classmethod`:

```python
@classmethod
def from_dict(cls, data):

    return cls(
        data.get("name", ""),
        data.get("age", 0),
        data.get("employee_id", ""),
        data.get("salary", 0)
    )
```

It allows an Employee object to be created from a dictionary.

Example:

```python
employee_data = {
    "name": "Madhav Birla",
    "age": 29,
    "employee_id": "E123",
    "salary": 35000
}
```

The object can be created using:

```python
Employee.from_dict(employee_data)
```

The normal constructor can also be used to create an Employee object.

---

## 🔍 Getters and Setters

The project uses getter and setter methods for controlled access to private attributes.

| Method              | Purpose                                                     |
| ------------------- | ----------------------------------------------------------- |
| `get_employee_id()` | Returns the employee ID                                     |
| `set_employee_id()` | Updates the employee ID after checking that it is not empty |
| `get_salary()`      | Returns the salary                                          |
| `set_salary()`      | Updates the salary after checking that it is not negative   |

---

## ✅ Validation

The current program performs the following validation:

* Employee ID cannot be empty when using `set_employee_id()`.
* Salary cannot be negative when using `set_salary()`.
* Salary is converted to `float` before being stored.
* Menu choices are checked against the available options.
* The `create_*()` functions convert age to `int` and salary to `float`.

### Input Handling

The following inputs are converted using Python's built-in conversion functions:

```python
age = int(input("Enter Age: "))
```

```python
salary = float(input("Enter Salary: "))
```

Therefore, the user is expected to enter valid numeric values for age and salary.

---

## 🧪 `issubclass()`

The program demonstrates class inheritance using:

```python
issubclass(Manager, Employee)
```

and:

```python
issubclass(Developer, Employee)
```

Both return:

```text
True
```

because `Manager` and `Developer` inherit from `Employee`.

---

## 🔎 `isinstance()`

The program uses `isinstance()` to identify object types.

Examples:

```python
isinstance(manager, Manager)
```

```python
isinstance(developer, Employee)
```

A `Developer` object is also an `Employee` because `Developer` inherits from `Employee`.

The program also uses `isinstance()` inside `show_details()` to determine whether an object is a Manager, Developer, or regular Employee.

---

## 🧍 Use of `self`

The `self` keyword refers to the current object.

It is used for instance attributes such as:

```python
self.name
self.age
self.department
self.programming_language
```

It is also used when accessing private attributes and methods inside the classes.

---

## 🖥️ Interactive User Interface

The main menu is:

```text
1. Create a Person
2. Create an Employee
3. Create a Manager
4. Create a Developer
5. Show Details
6. Exit
```

The program continues running until the user selects option `6`.

---

## 📋 Show Details

Option `5` opens the details menu:

```text
1. Person
2. Employee
3. Manager
4. Developer
5. All
```

The program displays the selected records using the appropriate `display()` method.

For Employee records, the program uses `isinstance()` to distinguish between:

* Regular Employee
* Manager
* Developer

---

## 📊 OOP Concepts Demonstrated

| OOP Concept             | Implementation                               |
| ----------------------- | -------------------------------------------- |
| Class                   | `Person`, `Employee`, `Manager`, `Developer` |
| Object                  | Objects created from the classes             |
| Constructor             | `__init__()`                                 |
| Destructor              | `__del__()`                                  |
| Encapsulation           | Private Employee ID and Salary               |
| Getter                  | `get_employee_id()`, `get_salary()`          |
| Setter                  | `set_employee_id()`, `set_salary()`          |
| Validation              | Employee ID and salary validation            |
| Inheritance             | Manager and Developer inherit Employee       |
| Method Overriding       | Manager and Developer override `display()`   |
| `super()`               | Parent constructor and display method        |
| Alternative Constructor | `Employee.from_dict()`                       |
| `issubclass()`          | Checks class inheritance                     |
| `isinstance()`          | Checks object type                           |
| `self`                  | Used for instance attributes                 |
| Interactive UI          | Menu-driven console interface                |

---

## ▶️ How to Run

Make sure Python is installed on the system.

Open the project folder in a terminal and run:

```bash
python employee_management_system.py
```

Follow the menu options and enter the required information.

---

## 📝 Assumptions

* Employee ID should not be empty.
* Salary should be entered as a numeric value.
* Salary cannot be negative.
* Age should be entered as a numeric value.
* The program expects valid numeric input for age and salary.
* Manager department and Developer programming language are accepted as user input.
* Created objects are stored only during the current program execution.
* No database or external permanent storage is used.
* `Employee.from_dict()` is available as an alternative way to create an Employee object but is not directly used through the main menu.
* Destructor execution timing and order are controlled by Python's object lifecycle.

---

## 📌 Conclusion

This project demonstrates how Python Object-Oriented Programming concepts can be used to build an Employee Management System.

The project combines:

* Classes and objects
* Constructors and destructors
* Encapsulation
* Getters and setters
* Validation
* Inheritance
* Method overriding
* Alternative constructors
* `super()`
* `issubclass()`
* `isinstance()`
* `self`
* Interactive menu-driven programming

The project provides a practical example of applying OOP concepts in a console-based Python application.

---

## 🖥️ Output Presentation

The output below represents a sample program execution.

It includes:

* Creating a Person
* Creating an Employee
* Creating a Manager
* Creating a Developer
* Displaying Developer details
* Performing inheritance checks
* Selecting option `6` to exit the program
* Object cleanup messages

The sample output is kept at the end of this README so that the complete execution result is easy to verify.

---

# 💻 Sample Output

```text
==============================================
       PYTHON OOP PROJECT: EMPLOYEE
           MANAGEMENT SYSTEM
==============================================

--- Choose an operation ---

Choose an operation:
1. Create a Person
2. Create an Employee
3. Create a Manager
4. Create a Developer
5. Show Details
6. Exit

Enter your choice: 1

Enter Name: hari mehta
Enter Age: 25

Person created with name: hari mehta and age: 25.

--- Choose an operation ---

Choose an operation:
1. Create a Person
2. Create an Employee
3. Create a Manager
4. Create a Developer
5. Show Details
6. Exit

Enter your choice: 2

Enter Name: madhav birla
Enter Age: 29
Enter Employee ID: E123
Enter Salary: 35000

Employee created with name: madhav birla, age: 29, ID: E123, and salary: $35000.00.

--- Choose an operation ---

Choose an operation:
1. Create a Person
2. Create an Employee
3. Create a Manager
4. Create a Developer
5. Show Details
6. Exit

Enter your choice: 3

Enter Name: vrunda sharma
Enter Age: 24
Enter Employee ID: M456
Enter Salary: 50000
Enter Department: Sales

Manager created with name: vrunda sharma, age: 24, ID: M456, salary: $50000.00, and department: Sales.

--- Choose an operation ---

Choose an operation:
1. Create a Person
2. Create an Employee
3. Create a Manager
4. Create a Developer
5. Show Details
6. Exit

Enter your choice: 4

Enter Name: shree patel
Enter Age: 19
Enter Employee ID: D789
Enter Salary: 60000
Enter Programming Language: Python

Developer created with name: shree patel, age: 19, ID: D789, salary: $60000.00, and programming language: Python.

--- Choose an operation ---

Choose an operation:
1. Create a Person
2. Create an Employee
3. Create a Manager
4. Create a Developer
5. Show Details
6. Exit

Enter your choice: 5

Choose details to show:
1. Person
2. Employee
3. Manager
4. Developer
5. All

Enter your choice: 4

Employee Details:
Name: shree patel
Age: 19
Employee ID: D789
Salary: $60000.00
Programming Language: Python

Inheritance Checks:
issubclass(Manager, Employee): True
issubclass(Developer, Employee): True
isinstance(vrunda sharma, Manager): True
isinstance(shree patel, Employee): True

--- Choose another operation ---

Choose an operation:
1. Create a Person
2. Create an Employee
3. Create a Manager
4. Create a Developer
5. Show Details
6. Exit

Enter your choice: 6

Exiting the system. All resources have been freed.
Goodbye!

Resource cleanup completed for shree patel.
Resource cleanup completed for vrunda sharma.
Resource cleanup completed for madhav birla.
```
