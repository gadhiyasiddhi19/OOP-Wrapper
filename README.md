# Python OOP Project: Employee Management System

**Author:** Siddhi Gadhiya

---

## 📌 Project Description

This is a simple Python menu-driven Employee Management System developed to demonstrate important Object-Oriented Programming (OOP) concepts.

The program allows users to:

- Create a Person.
- Create an Employee.
- Create a Manager.
- Create a Developer.
- Display details of created objects.
- Check inheritance relationships.
- Use encapsulation and validation.
- Demonstrate method overriding and `super()`.
- Demonstrate `issubclass()` and `isinstance()`.
- Exit the program when needed.

---

## 🛠️ Technologies Used

- **Python 3.14.6** — Programming language used to develop the Employee Management System.
- **Visual Studio Code (VS Code)** — Development environment used to write and run the project.
- **Python Standard Library** — Built-in Python features used for console input/output, classes, objects, inheritance, validation, and object cleanup.

---

## 📁 Project Structure

The project is organized as follows:

```text
Project-5/
├── employee_management_system.py
└── README.md
```

### File Description

| File | Purpose |
|---|---|
| `employee_management_system.py` | Main Python program containing the Person, Employee, Manager, and Developer classes, menu system, validation, OOP demonstrations, and program execution. |
| `README.md` | Project documentation containing the description, technologies, project structure, OOP concepts, run instructions, assumptions, and sample output. |

---

## 🎯 Objective

The main objective of this project is to build an Employee Management System using Python and demonstrate various Object-Oriented Programming concepts.

The project demonstrates classes, objects, constructors, destructors, encapsulation, inheritance, method overriding, alternative constructors, `super()`, `issubclass()`, `isinstance()`, validation, and an interactive menu-driven user interface.

---

## 📂 Project Classes

1. `Person`
2. `Employee`
3. `Manager`
4. `Developer`

```text
Person
   |
   +---- Employee
             |
             +---- Manager
             |
             +---- Developer
```

---

## 👤 Person Class

The `Person` class represents a basic person.

### Attributes

- `name`
- `age`

### Constructor

```python
def __init__(self, name="", age=0):
    self.name = name
    self.age = age
```

The `self` keyword refers to the current object's instance attributes. The class also contains a `display()` method to show person details.

---

## 👨‍💼 Employee Class

The `Employee` class is the base class for employee-related classes.

### Attributes

- `name`
- `age`
- `employee_id`
- `salary`

### Constructor

```python
def __init__(self, name="", age=0, employee_id="", salary=0.0):
```

---

## 🔐 Encapsulation

Sensitive employee information is protected using private attributes:

```python
self.__employee_id
self.__salary
```

They are accessed through getter and setter methods.

```python
def get_employee_id(self):
    return self.__employee_id
```

```python
def set_employee_id(self, employee_id):
```

```python
def get_salary(self):
    return self.__salary
```

```python
def set_salary(self, salary):
```

The setters validate the values. Employee ID cannot be empty and salary must be numeric and non-negative.

---

## 🏗️ Constructors

Constructors are implemented using `__init__()` and initialize object attributes.

Example:

```python
employee = Employee(
    "Madhav Birla",
    29,
    "E123",
    35000
)
```

---

## 🧹 Destructor

The `Employee` class contains:

```python
def __del__(self):
```

The destructor demonstrates resource cleanup when objects are destroyed.

---

## 🧬 Inheritance

Manager and Developer inherit from Employee:

```python
class Manager(Employee):
```

```python
class Developer(Employee):
```

Both classes reuse Employee attributes and methods.

---

## 👔 Manager Class

The `Manager` class is derived from `Employee`.

Additional attribute:

```text
department
```

The `display()` method is overridden to include department information.

---

## 👨‍💻 Developer Class

The `Developer` class is derived from `Employee`.

Additional attribute:

```text
programming_language
```

The `display()` method is overridden to include programming language information.

---

## 🔄 Method Overriding

The Employee class defines `display()`. Manager and Developer override it.

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

This extends the parent functionality with child-specific information.

---

## ⬆️ Use of `super()`

`super()` calls parent-class constructors and methods.

Manager and Developer constructors call:

```python
super().__init__(
    name,
    age,
    employee_id,
    salary
)
```

Their overridden `display()` methods call:

```python
super().display()
```

---

## 🔀 Method Overloading / Alternative Constructor

Python does not provide traditional method overloading in the same way as some languages, so an alternative constructor is used.

```python
@classmethod
def from_dict(cls, data):
```

This provides another way to create an Employee object from a dictionary.

Example:

```python
employee_data = {
    "name": "Madhav Birla",
    "age": 29,
    "employee_id": "E123",
    "salary": 35000
}
```

It can be created using:

```python
Employee.from_dict(employee_data)
```

The normal constructor can also be used.

---

## 🔍 Getters and Setters

The project uses:

```text
get_employee_id()
set_employee_id()
get_salary()
set_salary()
```

The setters provide controlled access and validation for private attributes.

---

## ✅ Validation

The program validates:

- Name is not empty.
- Age is not negative.
- Employee ID is not empty.
- Salary is numeric.
- Salary is not negative.
- Department is not empty.
- Programming language is not empty.
- Menu choices are valid.

---

## 🧪 `issubclass()`

The program demonstrates:

```python
issubclass(Manager, Employee)
```

and:

```python
issubclass(Developer, Employee)
```

Both return `True` because they inherit from Employee.

---

## 🔎 `isinstance()`

The program uses `isinstance()` to check object types.

Examples:

```python
isinstance(manager, Manager)
```

```python
isinstance(developer, Employee)
```

A Developer is also an Employee because Developer inherits from Employee.

---

## 🧍 Use of `self`

The `self` keyword refers to the current object and is used for instance attributes such as:

```python
self.name
self.age
self.department
self.programming_language
```

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

The program continues until option `6` is selected.

---

## 📋 Show Details

Option `5` displays:

```text
1. Person
2. Employee
3. Manager
4. Developer
5. All
```

The selected object's appropriate `display()` method is called.

---

## 📊 OOP Concepts Demonstrated

| OOP Concept | Implementation |
|---|---|
| Class | Person, Employee, Manager, Developer |
| Object | Objects created from the classes |
| Constructor | `__init__()` |
| Destructor | `__del__()` |
| Encapsulation | Private Employee ID and Salary |
| Getter | `get_employee_id()`, `get_salary()` |
| Setter | `set_employee_id()`, `set_salary()` |
| Validation | Input and setter validation |
| Inheritance | Manager and Developer inherit Employee |
| Method Overriding | Manager and Developer override `display()` |
| `super()` | Parent constructor and display method |
| Alternative Constructor | `Employee.from_dict()` |
| `issubclass()` | Checks class inheritance |
| `isinstance()` | Checks object type |
| `self` | Used for instance attributes |
| Interactive UI | Menu-driven console interface |

---

## ▶️ How to Run

Make sure Python is installed.

```bash
python employee_management_system.py
```

Follow the menu options and enter the required information.

---

## 📝 Assumptions

- Employee ID must not be empty.
- Salary must be numeric.
- Salary cannot be negative.
- Age cannot be negative.
- Department must be provided for a Manager.
- Programming language must be provided for a Developer.
- Created objects are stored only during the current execution.
- No database or external permanent storage is used.

---

## 📌 Conclusion

This project demonstrates how Python Object-Oriented Programming concepts can be used to build an Employee Management System.

The project combines classes, objects, constructors, destructors, encapsulation, getters and setters, validation, inheritance, method overriding, alternative constructors, `super()`, `issubclass()`, `isinstance()`, and an interactive menu.

---

## 🖥️ Output Presentation

The output below represents the complete program execution. It includes the menu flow for creating a Person, Employee, Manager, and Developer, displaying details, performing inheritance checks, and executing **option 6 (Exit)**.

The sample output is kept at the end of this README so the complete execution result is easy to verify.

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

--- Choose an operation ---

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