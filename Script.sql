create table customer(
	customer_id serial primary key,
	first_name varchar(20),
	last_name varchar(20)
	);
	
insert into customers values(-1, "for", "delete")

create table accounts(
	balance dec(15,2) check(balance >= 0),
	customer_id int,
	account_id serial primary key,
	constraint account_fk foreign key (customer_id) references customer(customer_id) on delete cascade);
	