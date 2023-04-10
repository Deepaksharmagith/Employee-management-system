create database ems;
use ems;
create table emp_details(emp_id varchar(255),emp_pass varchar(255),emp_name varchar(255),Phone_No varchar(15),gender enum('M','F','O'),address varchar(255),Date_of_join varchar(255),designation varchar(255),dept varchar(255),salary varchar(255),primary key(emp_id));
insert into emp_details values('mohan5856@.com','65974moh','mohan singh','5698745621','m','xxxxxx','5/11/22','HR','xxxxx','50k');
Update emp_details  set emp_pass='56328',address='delhi---xx' where emp_id='varun4568@.com';
select * from emp_details;
select * from emp_details where emp_id='varun4568@.com';
create table admin_details(aid varchar(255),apass varchar(255),primary key(aid));
insert into admin_details values('aman234@mylibrary.com','980iamaman');
insert into admin_details values('varun586@mylibrary.com','vn564');
Update admin_details  set apass='56328' where aid='aman234@mylibrary.com';
select * from admin_details;

create table project(eid varchar(255),project_name varchar(255),project_assigned varchar(255),Deadline varchar(255),target_achieved varchar(255),progress varchar(255),primary key(eid));
select * from project;

create table Resignation_form(Dio varchar(255),eid varchar(255),e_name varchar(255),reason varchar(255),describe_company_culture varchar(255),your_aspects varchar(255),rate_your_manager_out_of_5 varchar(255),primary key(eid));
select * from Resignation_form;




create table attendance(eid varchar(255),emp_name varchar(255),DIO varchar(255));
select * from attendance;