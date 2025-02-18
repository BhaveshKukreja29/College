"""Python program to create and list of employees using Employee class.
 2 Program should also print total number of employees.
 3 Employee class should have
 4 ● empcount (class variable)
 5 ● id and name (instance variable)
 6 ● constructor to set id,
 7 ● set_name( ), get_name ( ), get_id( ) methods (instance method)
 8 ● set_emp_count ( ) (class method)"""
 9 class Employee:
10      empcount = 0
11
12      @classmethod
13      def set_emp_count(cls):
14         cls.empcount += 1
15
16      def __init__(self):
17          self.set_emp_count()
18          self.id = self.empcount + 1000
19          self.name = self.set_name()
20          
21      def set_name(self):
22          name = input("Enter employee name: ")
23          return name
24          
25      def get_name(self):
26          print(f"Name is: {self.name}")
27          
28      def get_id(self):
29         print(f"Id is: {self.id}")
30         print(f"Id is: {self.id}")
31         
32 employees = []
33 while True:
34     ch = int(input("Enter 1 to add employee, 2 to see all employees and 3 to exi>
35     
36     if ch == 1:
37         employees.append(Employee())
38     elif ch == 2:
39         print()
40         for i in employees:
41             print(f"Name: {i.name}, ID: {i.id}")
42         print()
43     elif ch == 3:
44         break
45     else:
46         print("Invalid choice, try again")
47

