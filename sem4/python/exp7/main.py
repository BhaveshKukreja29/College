"""
Python program to
● Import Employee and Account sub-packages.
● Calculate Salary = Basic + H.R.A - P.F.
● Display all the details of the Employee in tabular format.
"""

from employee.profile import Profile
from employee.qualification import Qualification
from account.salary import Salary


class Employee:
    def __init__(t, id, name, age, dob, degree, experience, basic, hra, pf):
        t.profile = Profile(id, name, age, dob)
        t.qualification = Qualification(degree, experience)
        t.salary = Salary(basic, hra, pf)

    def __str__(t):
        return f"|{t.profile.id:^6}|{t.profile.name:^12}|{t.profile.age:^7}|{t.profile.dob:^12}|{t.qualification.degree:^12}|{t.qualification.experience:^12}|{t.salary.basic:^12}|{t.salary.hra:^8}|{t.salary.pf:^8}|{t.salary.total:^13}|"


def main():
    n = int(input("Enter the number of Employees: "))
    employees = []

    for i in range(n):
        print(f'\nFor Employee {i + 1}')
        id = int(input('Enter ID: '))
        name = input('Enter Name: ')
        age = int(input('Enter Age: '))
        dob = input('Enter Date of Birth (YYYY-MM-DD): ')
        degree = input('Enter Degree: ')
        experience = int(input('Enter Experience (Years): '))
        basic = float(input('Enter Basic Pay: '))
        hra = float(input('Enter H.R.A: '))
        pf = float(input('Enter P.F: '))

        employees.append(Employee(id, name, age, dob, degree, experience, basic, hra, pf))

    print("\n+------+------------+-------+------------+------------+------------+------------+--------+--------+-------------+")
    print("|  ID  |    Name    |  Age  |    DOB     |   Degree   | Experience |  Basic Pay |  HRA   |  P.F   |  Net Salary |")
    print("+------+------------+-------+------------+------------+------------+------------+--------+--------+-------------+")

    for emp in employees:
        print(emp)
        print("+------+------------+-------+------------+------------+------------+------------+--------+--------+-------------+")

    return 0


if __name__ == "__main__":
    while True:
        if main() == 0:
            break
