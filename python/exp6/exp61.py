class Fail(Exception):
    def __init__(self):
        super().__init__("Error: Marks can't be below 40. The student will Fail\n")

class Student:
    def __init__(self, rno, name, marks):
        self.rno = rno
        self.name = name
        self.marks = marks

        if marks < 40:
            raise Fail()

    def __str__(self):
        return f"|{self.name:^10}|{self.rno:^10}|{self.marks:^10}|"
    
def main():
    n = int(input("Enter the number of students: "))
    slist = []

    for i in range(n):
        print(f"Data for student {i + 1}")
        rno = int(input("Enter the roll no. : "))
        name = input("Enter the name: ")
        marks = int(input("Enter the marks: "))
        print()

        try:
            slist.append(Student(rno, name, marks))
        except Fail as e:
            print(e)
            print()

    print("+----------+----------+----------+")
    print("|   Name   | Roll No. |  Marks   |")
    print("+----------+----------+----------+")

    for i in slist:
        print(i)
        print("+----------+----------+----------+")

if __name__ == "__main__":
    main()