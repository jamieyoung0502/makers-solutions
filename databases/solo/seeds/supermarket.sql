DROP TABLE IF EXISTS order_products;
DROP SEQUENCE IF EXISTS order_products_id_seq;

DROP TABLE IF EXISTS orders;
DROP SEQUENCE IF EXISTS orders_id_seq;

DROP TABLE IF EXISTS products CASCADE;
DROP SEQUENCE IF EXISTS products_id_seq;

DROP TABLE IF EXISTS customers CASCADE;
DROP SEQUENCE IF EXISTS customers_id_seq;

CREATE TABLE customers (
	id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	first_name VARCHAR(100) NOT NULL,
	last_name VARCHAR(100) NOT NULL
);

INSERT INTO customers (first_name, last_name) VALUES ('Adrian', 'Hards');

CREATE TABLE products (
	id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	name VARCHAR(100) NOT NULL,
	quantity INT,
	price decimal (10,2) NOT NULL
);

INSERT INTO products (name, quantity, price) VALUES ('salad cream', 100, 9.99);
INSERT INTO products (name, quantity, price) VALUES ('ketchup', 0, 8.01);
INSERT INTO products (name, quantity, price) VALUES ('mayo', 11, 5);

CREATE TABLE orders (
	id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	date DATE NOT NULL,
	customer_id INT,
	CONSTRAINT fk_customer FOREIGN KEY (customer_id) REFERENCES customers (id) ON DELETE CASCADE
);

CREATE TABLE order_products (
	order_id INT NOT NULL,
	product_id INT NOT NULL,
	quantity INT NOT NULL,
	CONSTRAINT fk_order FOREIGN KEY (order_id) REFERENCES orders (id) ON DELETE CASCADE,
	CONSTRAINT fk_product FOREIGN KEY (product_id) REFERENCES products (id) ON DELETE CASCADE,
	PRIMARY KEY (order_id, product_id)
);
