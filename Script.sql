create table customer(
	customer_id serial primary key,
	first_name varchar(20),
	last_name varchar(20)
	);
	
--for delete test
insert into customers values(-1, "for", "delete");
-- for account create test 
insert into custoemrs values(-2 'for', 'create account test');

update accounts set balance = 500.00 dwhere acount id = -5;
update accounts set balance = 500.00 dwhere acount id = -6;

create table accounts(
	balance dec(15,2) check(balance >= 0),
	customer_id int,
	account_id serial primary key,
	constraint account_fk foreign key (customer_id) references customer(customer_id) on delete cascade);

insert into account values(-2,-2,500.00);

select * from accounts where customer_id = 1000




