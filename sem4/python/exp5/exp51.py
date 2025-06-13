"""Python program to create and list of employees using Employee class.
 2 Program should also print total number of employees.
 3 Employee class should have
 4 ● empcount (class variable)
 5 ● id and name (instance variable)
 6 ● constructor to set id,
 7 ● set_name( ), get_name ( ), get_id( ) methods (instance method)
 8 ● set_emp_count ( ) (class method)"""
class Employee:
    empcount = 0

    @classmethod
    def set_emp_count(cls):
        cls.empcount += 1

    def __init__(self):
        self.set_emp_count()
        self.id = self.empcount + 1000
        self.name = self.set_name()

    def set_name(self):
        name = input("Enter employee name: ")
        return name
          
    def get_name(self):
        print(f"Name is: {self.name}")
          
    def get_id(self):
        print(f"Id is: {self.id}")
        print(f"Id is: {self.id}")
         
employees = []
while True:
    ch = int(input("Enter 1 to add employee, 2 to see all employees and 3 to exit"))
     
    if ch == 1:
        employees.append(Employee())
    elif ch == 2:
        print()
        for i in employees:
            print(f"Name: {i.name}, ID: {i.id}")
        print()
    elif ch == 3:
        break
    else:
        print("Invalid choice, try again")


