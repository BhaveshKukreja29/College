create database prac3;
use prac3;

create table dept(
	deptno integer primary key,
    dname varchar(20) not null,
    loc varchar(4)
);

alter table dept rename to department;

alter table department add pincode numeric(6) not null;

alter table department rename column dname to department_name;

alter table department modify loc char(10);

drop table department;
