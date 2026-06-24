#class 1

mysql -uroot -proot
show databases;

SYSTEM cls

CREATE DATABASE dbtwo;

USE dbtwo;

show tables;

CREATE TABLE employees(
empId int,
empName VARCHAR(32),
esal FLOAT
);

DESC employees;

SELECT *FROM employees;

INSERT INTO employees
VALUES
(101,'modi',45000.00),
(102,'Gandhi',55000.00),
(103,'Trisha',65000.00),
(104,'Sonia',75000.00);

INSERT INTO employees(empId,empName)
VALUES
(105,'vijay');

INSERT INTO employees(empId)
VALUES
(106),
(107),
(108),
(109);

SELECT *FROM employees;

DELETE FROM employees
WHERE empId = 101;


TRUNCATE TABLE employees;

DROP TABLE employees;


DELETE → "Remove some data"
TRUNCATE → "Clear full table"
DROP → "Remove table completely"
ALTER → "Change table structure"

ALTER table employees
ADD dept VARCHAR(20);

ALTER table employees
MODIFY esal DOUBLE;


ALTER TABLE employees
DROP COLUMN dept;

=============================================

#DAY2

SYSTEM cls

show databases;

CREATE TABLE employees(
	eid  INT UNIQUE ,
	ename VARCHAR(32) NOT NULL,
	esal  FLOAT CHECK(esal>18000.18), 
	gender VARCHAR(32) NOT NULL, 
	loc    VARCHAR(32)  DEFAULT 'Bangalore'
);

DESC employees

mysql CONSTRAINTS

1.UNIQUE
2.NOT NULL
3.DEFAULT
4.CHECK
5.PRIMARY KEY
6.FOREIGN KEY
7.INDEX


# DAY 3

CREATE table Orders(
orderId int UNIQUE,
name VARCHAR(32) NOT NULL,
price FLOAT CHECK(price>=100),
status VARCHAR(32) DEFAULT 'open'
);

DESC Orders;


INSERT INTO Orders
VALUES
(1001,'Marker pen',150.00,'delivered'),
(1002,'Lenovo',1650.00,'delivered');


SELECT *FROM Orders;


INSERT INTO Orders
VALUES
(1003,'Mi Tv',99,'delivered');


CREATE TABLE employes(
	eid int, 
	ename VARCHAR(32) NOT null,
	esal float,
	age INT CHECK(age>18),
	loc VARCHAR(32) DEFAULT 'Bangalore',
	gender VARCHAR(32),
	PRIMARY KEY(eid)
);


#day 4 

CREATE TABLE customers(
cust_Id int,
name VARCHAR(32) NOT null,
age int CHECK(age>=12),
loc VARCHAR(32) DEFAULT"bangalore",
PRIMARY KEY(cust_Id)
);

DESC customers;

CREATE TABLE Orders(
ord_Id int,
details VARCHAR(32) NOT null,
amount int CHECK(amount>=100),
customer_Id int,
status VARCHAR(32) DEFAULT"open",
PRIMARY KEY(ord_Id),
FOREIGN KEY(customer_Id)REFERENCES customers(cust_Id)
);


DESC Orders;

SELECT *FROM Orders;

SELECT *FROM customers;

INSERT INTO Orders;
VALUES

INSERT INTO orders
VALUES
(10001,'Mp-2',150.00,101,'Delivered'),
(10002,'MI TV',24000.00,101,'OPEN'),
(10003,'Think Pad',150000.00,101,'Success'),
(10004,'Lenovo Mouse',450.00,102,'Delivered'),
(10005,'Dustomer2',150.00,103,'OPEN'),
(10006, 'Iphone 5s',8000.00,103,'InProgress'),
(10007,'Samsung Galaxy2',34850.00,103,'Delivered'),
(10008,'Water Bolldle set',400.00,103,'OPEN'),
(10009,'Mp-3',150.00,101,'Delivered'),
(10010,'Pencils Set',150.00,101,'OPEN');


SELECT *FROM
orders ord,
customers cust
WHERE ord.customer_Id = cust.cust_Id;


SELECT 
	o.details AS "Order Details",
	o.amount AS "Amount",
	c.name AS "Customer Name",
	c.loc AS  "Location"

	from
	orders o,
	customers c
WHERE o.customer_Id = c.cust_Id;


========================================

#DAY 5

show databases;

CREATE DATABASE dbthree;

USE dbthree;

create table employee (
	eid INT ,
	fname VARCHAR(32),
	lname VARCHAR(32),
	city VARCHAR(32),
	esal INT,
	age INT,
	PRIMARY KEY(eid)
);


insert into employee values
(101,'Rahul','Gandhi','Wayanad',45000,52),
(102,'Sonia','Gandhi','New Delhi',55000,75),
(103,'Priyanka','Gandhi','Nodia',65000,45),
(104,'Modi','Narendra','New Delhi',75000,69),
(105,'Rajni','Kanth','Chennai',85000,65),
(106,'Vijay','Setupathi','Chennai',95000,47),
(107,'Nayana','Tara','Chennai',25000,40),
(108,'Alia','Bhut','Mumbai',45000,31),
(109,'Mahesh','Bhut','Mumbai',15000,68),
(110,'Sonam','Kapoor','Mumbai',30000,27),
(111,'Anil','Kapoor','Mumbai',38000,40),
(112,'Raj','Kapoor','Mumbai',18000,78),
(113,'Vishnu','Manchu','Hyderabad',10000,40),
(114,'Manoj','Manchu','Hyderabad',12000,35);

Inserting a null salary value

INSERT INTO employee (eid,fname,lname,city,age)
values
(115,'Mohan','Manchu','Hyderabad',70);

SELECT *from employee;


=======================================================

ASSIGNMENT QUESTIONS AND ANSWERS:


1.Write a query to fetch people whose last name is same.

SELECT *FROM employee
WHERE lname IN (SELECT lname FROM employee 
                GROUP BY lname HAVING COUNT(*)>1
				)
ORDER BY lname;

2.Write a query to fetch whose age is grater then 70.

SELECT *from employee
WHERE age>=70;

SELECT COUNT(*)  AS "No of Employee"
FROM employee
WHERE age>=70;

3.Write a query to to fetch people with same city.

SELECT *from employee
WHERE city=

4.Write a query to to fetch whose name ends with 'h'.


WILDCARD OPERATORS
%-MATCHES MORE THEN ONE CHAR
_ MATCHES EXACTLY ONE CHAR


SELECT *FROM employee
WHERE lname LIKE "%h";


5.Write a query to count person whose last name ends with 'i'.


select count(*) from employee;
where lname LIKE "%i";

6.Write a query to find person with highest salary.

SELECT *FROM employee
WHERE esal = (
    SELECT MAX(esal)
    FROM employee
);

7.Write a query to find person with lowest salary.


SELECT *FROM employee
WHERE esal = (
    SELECT MIN(esal)
    FROM employee
);

8.Write a query to change last name of person whose id is 102.

update employee
set lname = 'singh'
where eid = 102;


9.Write a query to find name of person whose name start's with 'A' and city name starts with 'B'.

SELECT *FROM employee
WHERE fname LIKE 'A%' 
AND city LIKE 'B%';


10.Write a query to find person with highest salary in 'New Delhi'.	

SELECT *FROM employee
WHERE esal = (
    SELECT MAX(esal)
    FROM employee
	where city = 'New Delhi'
	);
	
11.Write a query to to find person who live in 'New Delhi' with age above 70.

	SELECT *from employee
	where age>70
	AND city = 'NEW Delhi';
	

12.Write a query to find person with salary below 50000.

SELECT *from employee
where esal<50000;

SELECT COUNT(*)  AS "No of Employee"
FROM employee
WHERE esal<50000;

13.Write a query to find name of people with salary range between 20000 to 40000.

SELECT fname, lname
FROM employee
WHERE esal BETWEEN 20000 AND 40000;


15. Write a query to find person whose first name third character is 'j'.

SELECT *from employee
where fname LIKE '__j%';

16.Write a query to find person whose first name third character is 'j' and live in 'New Delhi'.

SELECT *from employee
where fname LIKE '__j%'
AND city="New Delhi";

17.Write a query to count persons whose first name third character is 'j'.

SELECT count(*) AS "fname character"
FROM employee
where fname LIKE '__j%';

18.Write a query to fetch person with lowest salary and add 10000 to its salary

select esal from employee
where esal=(select MIN(esal) from employee);
 
 update employee
 set esal = esal+10000
 where esal=10000;
 
 #2
 
 SELECT *from employee;
       esal + 10000 AS new_salary
FROM employee
WHERE esal = (
    SELECT MIN(esal)
    FROM employee
);
 
 
 19.Write a query to Sort the table by ascending.
 
 SELECT *FROM employee
ORDER BY esal ASC;

20.Write a query to Sort the table by descending.

SELECT *FROM employee
ORDER BY esal DESC;

21.Write a query to show person whose name's last third word is 'j' and salary is more then 30000

SELECT *from employee
where lname LIKE '%j__';
AND esal > 30000;

22.Write a query to show all people who live in 'Bangalore' and 'Wayanad'.

SELECT *from employee
where city="Bangalore, Wayanad";

23.Write a query to fetch people with first name conunt is 5.

SELECT *from employee
where LENGTH(fname) = 5;

24.Write a query to group by people with their age.


25.Write a query to insert respective data-(id,fname,age) with values-(109,'Ram',28).

INSERT into employee (eid, fname, age)
VALUES (109,'ram',28);


26.Write a query to find people with null salary.

SELECT *FROM employee
where esal is Null;

27.Write a query to find people whose cities are not null.

SELECT *FROM employee
WHERE city is NOT NULL;


28.Write a query to delete data of person whose id is 109.

delete FROM employee
WHERE id= 109;

=============================================================================

# DAY 6

create DATABASE db4;


use db4;

create TABLE business_unit(
bu_Id INT,
name VARCHAR(32) not null,
loc VARCHAR(32) DEFAULT "bangalore_IBM",
PRIMARY key(bu_Id)
);

desc business_unit;


CREATE TABLE employees(
	eid int,
	ename VARCHAR(32) NOT null,
	esal FLOAT CHECK(esal>=18000),
	unit_Id INT, 
	gender VARCHAR(32),
		PRIMARY KEY(eid),
		FOREIGN KEY(unit_Id) REFERENCES business_unit(bu_Id)
);

INSERT INTO employees
VALUES
(101,'Rahul',45000.45,2001,'Male'),
(102,'Sonia',55000.45,2001,'Female'),
(103,'Priyanka',65000.45,2001,'Female'),
(104,'Modi',75000.45,2001,'Male'),
(105,'Amith',65000.45,2002,'Male'),
(106,'Vijay J',75000.45,2002,'Male'),
(107,'Rajni',85000.45,2002,'Male'),
(108,'Ajith',85000.45,2002,'Male'),
(109,'Vijay Sethupathi',75000.45,2003,'Male'),
(110,'Alia',55000.45,2003,'Female'),
(111,'Mahesh bhut',65000.45,2004,'Male'),
(112,'Mohan Manchu',745000.45,2001,'Male'),
(113,'Vishnu Manchu',845000.45,2001,'Male'),
(114,'Manoj',45000.45,2001,'Male'),
(115,'Lakshmi Manchu',35000.45,2002,'Female');


SELECT 
	emp.ename AS "Employee Name",
	emp.gender AS "Gender",
	bu.name AS "Business Unit Name"
	FROM business_unit bu, employees emp
	
	WHERE bu.bu_Id = emp.unit_Id;
	
	
===============================================
#DAY 7

JOINS:

INNER JOIN - MATCHED ROWS FROM BOTH table

LEFT JOIN - Take EVERYTHING from LEFT table
+
Matching rows from RIGHT table

RIGHT JOIN - Take EVERYTHING from RIGHT table
+
Matching rows from LEFT table



create DATABASE db5;

use db5;

create table customers(
c_id int,
Name VARCHAR(32) NOT Null,
age INT CHECK(age>15),
loc VARCHAR(32) DEFAULT "Bangalore",
PRIMARY key(c_id)
);

create table Orders(
order_id int,
details varchar(32) NOT Null,
amount float CHECK(amount>100),
cust_id INT,
status varchar(32) DEFAULT 'open',
PRIMARY key(order_id),
FOREIGN key(cust_id) REFERENCES customers(c_id)
);

desc customers;

desc orders;

insert into customers
values
(101,'Rahul',50,'hyd'),
(102,'Sonia',52,'kerala'),
(103,'Gandhi',53,'wayanad'),
(104,'Modi',54,'Blr');
(105,'Vijay',55,'Chennai');


insert into Orders
values
(1002,'Mouse Pad set',1500.50,102,'Open'),
(1003,'Lenovo ThinkPad',95000.50,102,'Open'),
(1004,'Apple Iphone 17',17500.50,102,'Outof Stock'),
(1005,'Nokia 1100',1500.50,104,'Open'),
(1006,'Mac book Prog',90500.50,104,'Open'),
(1007,'Ipad',11500.50,102,'Open'),
(1008,'Water PC',8500.50,102,'Open'),
(1010,'Samsung Galaxy',2500.50,103,'Open'),
(1011,'Lenovo Pad',1000.50,102,'Open'),
(1012,'HP',1500.50,103,'Open');

SELECT *from customers,orders;

SELECT 
	c.name AS "Customer Name",
	o.details AS "Order Details",
	o.amount AS "Amount",
	o.status AS "Status"
FROM customers c, orders o
WHERE o.cust_id=c.c_id;

SELECT 
	c.name AS "Customer Name",
	o.details AS "Order Details",
	o.amount AS "Amount",
	o.status AS "Status"
FROM
customers c INNER JOIN orders o
ON o.cust_id=c.c_id;



SELECT 
	c.name AS "Customer Name",
	o.details AS "Order Details",
	o.amount AS "Amount",
	o.status AS "Status"
FROM
customers c LEFT JOIN orders o
ON o.cust_id=c.c_id;

======================================================
#DAY 8

usecase - STATEMENT

1.fetch Customerand their placed order details
2.fetch all customer and their order details.
3.fetch all orders and associated order details

SELECT 
	c.name AS "Customer Name",
	o.details AS "Order Details",
	o.amount AS "Amount",
	o.status AS "Status"
FROM
customers c RIGHT JOIN orders o
ON o.cust_id=c.c_id;



SELECT 
	c.name AS "Customer Name",
	o.details AS "Order Details",
	o.amount AS "Amount",
	o.status AS "Status"
FROM
customers c LEFT OUTER JOIN orders o
ON o.cust_id=c.c_id;