create database prac5;
use prac5;

CREATE TABLE department (
    dname VARCHAR(50),
    dnumber INT PRIMARY KEY,
    mgrssn CHAR(9),
    mgrstartdate DATE
);

CREATE TABLE employee (
    fname VARCHAR(30),
    lname VARCHAR(30),
    ssn CHAR(9) PRIMARY KEY,
    bdate DATE,
    address VARCHAR(100),
    sex CHAR(1),
    salary DECIMAL(10, 2),
    superssn CHAR(9),
    dno INT,
    FOREIGN KEY (dno) REFERENCES department(dnumber)
);

-- Department Data
INSERT INTO department (dname, dnumber, mgrssn, mgrstartdate) VALUES
('Research', 1, '123456789', '2020-01-01'),
('Accounts', 2, '987654321', '2019-05-15'),
('IT', 3, '456789123', '2021-03-20'),
('HR', 4, '321654987', '2022-07-01'),
('Marketing', 5, '741852963', '2023-11-10');

-- Employee Data
INSERT INTO employee (fname, lname, ssn, bdate, address, sex, salary, superssn, dno) VALUES
('John', 'Doe', '111111111', '1990-05-10', 'NY', 'M', 60000, NULL, 1),
('Jane', 'Smith', '222222222', '1992-07-20', 'LA', 'F', 72000, '111111111', 2),
('Alice', 'Brown', '333333333', '1989-03-14', 'TX', 'F', 50000, '111111111', 1),
('Bob', 'White', '444444444', '1995-09-30', 'NJ', 'M', 45000, '222222222', 2),
('Carol', 'Black', '555555555', '1993-01-25', 'FL', 'F', 80000, '333333333', 3),
('Dave', 'Green', '666666666', '1991-11-22', 'NY', 'M', 43000, '111111111', 5),
('Eve', 'Grey', '777777777', '1998-06-15', 'TX', 'F', 40000, '222222222', 5),
('Frank', 'Blue', '888888888', '1985-08-19', 'WA', 'M', 85000, '333333333', 4);

-- important to do when updating with where clause
set SQL_SAFE_UPDATES = 0;

-- ten percent raise for research employeees
update employee set salary = salary * 1.10 where dno = (select dnumber from department where dname = 'Research');
select * from employee;

-- Salary Stats for 'Accounts'
select salary from employee where dno = (select dnumber from department where dname = 'Accounts');

-- name of employees in department 5
select fname, lname from employee where dno = 5;

-- Retrieve the name of each dept and number of employees working in each department which has at least 2 employees
select d.dname, count(*) as employee_count
from department d
join employee e on d.dnumber = e.dno
group by d.dname
having count(*) >= 2;	

-- Retrieve the name of employees who born in the year 1990’s
select fname, lname, bdate from employee where bdate like '199%';

-- 	Retrieve the name of employees and their dept name (using JOIN)
select e.fname, d.dname from employee e
join department d on d.dnumber = e.dno;
