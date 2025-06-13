create database prac4;
use prac4;

create table employee(
	empno varchar(10) primary key,
    emp_name varchar(20) not null,
    dept varchar(10),
    salary integer,
    doj date,
    branch varchar(20)
);

insert into employee(empno, emp_name, dept, salary, doj, branch)
values ('E101', 'Amit', 'Production', 45000, '2000-03-12', 'Bangalore'),
('E102', 'Amit', 'HR', 70000, '2002-07-03', 'Bangalore'),
('E103', 'Sunita', 'Management', 120000, '2001-01-11', 'Mysore'),
('E105', 'Sunita', 'IT', 67000, '2001-08-01', 'Mysore'),
('E106', 'Mahesh', 'Civil', 145000, '2003-09-20', 'Mumbai');

select * from employee;

select count(distinct emp_name) as count_of_distinct_emps from employee;

-- Retrieve total salary of employee group by employee name and count similar names
select sum(salary), count(*) from employee
group by emp_name;

-- Retrieve total salary of employees with salary > 120000
select sum(salary) from employee where salary > 120000;

--  Display name of employee in descending order
select emp_name from employee order by emp_name desc;

--   Display details of employee whose name is AMIT and salary greater than 50000
select * from employee where emp_name = 'Amit' and salary > 50000;
