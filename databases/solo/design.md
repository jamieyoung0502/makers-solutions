# Single Table Design Recipe Template

_Copy this recipe template to design and create a database table from a specification._

## 1. Extract nouns from the user stories or specification

```
As a shop manager
So I can know which items I have in stock
I want to keep a list of my shop items with their name and unit price.

As a shop manager
So I can know which items I have in stock
I want to know which quantity (a number) I have for each item.

As a shop manager
So I can manage items
I want to be able to create a new item.

As a shop manager
So I can know which orders were made
I want to keep a list of orders with their customer name.

As a shop manager
So I can know which orders were made
I want to assign each order to their corresponding item.

As a shop manager
So I can know which orders were made
I want to know on which date an order was placed.

As a shop manager
So I can manage orders
I want to be able to create a new order.
```

```
Nouns:
items, name, price, quantity
order, date
customer, name

Verbs:
create -> order, item
list -> items
update -> order
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record   | Properties            |
| -------- | --------------------- |
| item     | name, price, quantity |
| order    | date                  |
| customer | name                  |

## 3. Decide the column types

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

## 4. Design the Many-to-Many relationship

Make sure you can answer YES to these two questions:

1. Can one [TABLE ONE] have many [TABLE TWO]? (Yes/No)
2. Can one [TABLE TWO] have many [TABLE ONE]? (Yes/No)

```
# EXAMPLE

customer, order
1. Can one customer have many orders? YES
2. Can one order have many customers? NO
* one to many

order, items
1. Can one order have many items? YES
2. Can one item have many orders? YES
* many to many
```

_If you would answer "No" to one of these questions, you'll probably have to implement a One-to-Many relationship, which is simpler. Use the relevant design recipe in that case._

## 5. Design the Join Table

The join table usually contains two columns, which are two foreign keys, each one linking to a record in the two other tables.

The naming convention is `table1_table2`.

```
# EXAMPLE

Join table for tables: orders and items
Join table name: order_items
Columns: order_id, item_id
```

## 4. Write the SQL.

```sql
-- id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY better for new apps: has some advantages over SERIAL
-- product_name VARCHAR(100) NOT NULL, limits number of chars to 100
-- price decimal(10,2) # specifies max number of digits (10) and number of decimal points after (2)

-- https://learnsql.com/cookbook/how-to-create-a-primary-key-in-sql/
-- CREATE TABLE product (
-- name VARCHAR(100) NOT NULL,
-- producer VARCHAR(100) NOT NULL),
-- price DECIMAL(7,2),
-- PRIMARY KEY(name, producer)
-- );

CREATE TABLE customers (
	id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	name VARCHAR(100) NOT NULL
);

CREATE TABLE products (
	id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	product_name VARCHAR(100) NOT NULL,
	quantity INT,
	price decimal (10,2) NOT NULL
);

CREATE TABLE orders (
	id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	name VARCHAR(100) NOT NULL,
	date DATE NOT NULL,
	customer_id INT,
	CONSTRAINT fk_customer FOREIGN KEY (customer_id) REFERENCES customers (id) ON DELETE CASCADE
);

CREATE TABLE order_products (
	order_id INT NOT NULL,
	product_id INT NOT NULL,
	CONSTRAINT fk_order FOREIGN KEY (order_id) REFERENCES orders (id) ON DELETE CASCADE,
	CONSTRAINT fk_product FOREIGN KEY (product_id) REFERENCES products (id) ON DELETE CASCADE,
	PRIMARY KEY (order_id, product_id)
);
-- A composite key is a primary key that consists of two or more attributes (table columns) that together uniquely identify an entity occurrence (table row)
```

## 5. Create the table

```bash
psql -h 127.0.0.1 supermarket < supermarket_table.sql
```

## Diagram

<!-- https://www.datensen.com/blog/er-diagram/many-to-many-relationships/ -->

<img width="928" alt="Screenshot 2023-05-12 at 11 30 11" src="https://github.com/adrianHards/databases-in-python/assets/93719632/73afc77a-cce1-424a-88f5-1d3a5299ea8a">

## Tests

### Unit

```python
"""
does the class construct an object
and can attributes be called
"""

def test_constructs_object():
	pass

"""
when printed are the objects formatted in a readable manner
"""

def test_printed_object_is_formatted():
	pass

"""
are two objects with the same attributes regarded as equal
"""

def test_objects_with_same_attributes_seen_as_equal():
	pass
```

### Integration

```bash
Welcome to the shop management program!

What do you want to do?
  1 = list all shop products
  2 = create a new product
  3 = list all orders
  4 = create a new order

1 [enter]

Here's a list of all shop products:

 #1 Super Shark Vacuum Cleaner - Unit price: 99 - Quantity: 30
 #2 Makerspresso Coffee Machine - Unit price: 69 - Quantity: 15
 (...)
```

```python

"""
when I call ProductRepository#all
I see a list of all products for sale, their price and stock
no stock should be less than 0
"""

def test_list_all_products():
	pass

"""
when I call ProductRepository#create
I can add a new product to my inventory if the values are valid
and see the product added to my inventory
"""

def test_create_new_product():
	pass

"""
when I call OrderRepository#all
I see a list of all orders
with a list of items associated with each order
and the customers name who made the order
"""

def test_list_all_orders():
	pass

"""
when I call OrderRepository#create
I can make a new order
add multiple items to that order
but not be able to add items that are not in stock
see that the product quantity is affected as a result of the order
"""

def test_create_new_order():
	pass

```
