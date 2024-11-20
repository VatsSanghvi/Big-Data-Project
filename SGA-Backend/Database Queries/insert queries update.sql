-- ╔════════════════════════════════════════════════╗
-- ║               Users Table                      ║
-- ╚════════════════════════════════════════════════╝

---- Vats as admin, manager, and user
--INSERT INTO users (first_name, last_name, email, password, phone_number, role)
--VALUES 
--('Vats', 'Sanghvi', 'vats_admin@gmail.com', 'vats123', '123-456-7890', 'admin'),
--('Vats', 'Sanghvi', 'vats_manager@gmail.com', 'vats123', '123-456-7890', 'manager'),
--('Vats', 'Sanghvi', 'vats_user@gmail.com', 'vats123', '123-456-7890', 'customer');

---- Dev as admin, manager, and user
--INSERT INTO users (first_name, last_name, email, password, phone_number, role)
--VALUES 
--('Dev', 'Patel', 'dev_admin@gmail.com', 'dev123', '123-456-7890', 'admin'),
--('Dev', 'Patel', 'dev_manager@gmail.com', 'dev123', '123-456-7890', 'manager'),
--('Dev', 'Patel', 'dev_user@gmail.com', 'dev123', '123-456-7890', 'customer');

---- Zeel as admin, manager, and user
--INSERT INTO users (first_name, last_name, email, password, phone_number, role)
--VALUES 
--('Zeel', 'Shah', 'zeel_admin@gmail.com', 'zeel123', '123-456-7890', 'admin'),
--('Zeel', 'Shah', 'zeel_manager@gmail.com', 'zeel123', '123-456-7890', 'manager'),
--('Zeel', 'Shah', 'zeel_user@gmail.com', 'zeel123', '123-456-7890', 'customer');

---- Andre as admin, manager, and user
--INSERT INTO users (first_name, last_name, email, password, phone_number, role)
--VALUES 
--('Andre', 'Rodríguez', 'andre_admin@gmail.com', 'andre123', '123-456-7890', 'admin'),
--('Andre', 'Rodríguez', 'andre_manager@gmail.com', 'andre123', '123-456-7890', 'manager'),
--('Andre', 'Rodríguez', 'andre_user@gmail.com', 'andre123', '123-456-7890', 'customer');

---- Diego as admin, manager, and user
--INSERT INTO users (first_name, last_name, email, password, phone_number, role)
--VALUES 
--('Diego', 'Bolaños', 'diego_admin@gmail.com', 'diego123', '123-456-7890', 'admin'),
--('Diego', 'Bolaños', 'diego_manager@gmail.com', 'diego123', '123-456-7890', 'manager'),
--('Diego', 'Bolaños', 'diego_user@gmail.com', 'diego123', '123-456-7890', 'customer');



-- ╔════════════════════════════════════════════════╗
-- ║               Stores Table                     ║
-- ╚════════════════════════════════════════════════╝

--INSERT INTO store (store_name, location, manager_id) VALUES
--('Walmart', 'Location 1', 2),
--('Zehrs', 'Location 2', 5),
--('FreshCo', 'Location 3', 8),
--('No Frills', 'Location 4', 11),
--('Costco', 'Location 5', 14);


-- ╔════════════════════════════════════════════════╗
-- ║            Departments Table                   ║
-- ╚════════════════════════════════════════════════╝

---- Departments for all stores
--INSERT INTO department (department_name, store_id) VALUES 
--('Grocery', 1), ('Grocery', 2), ('Grocery', 3), ('Grocery', 4), ('Grocery', 5),
--('Produce', 1), ('Produce', 2), ('Produce', 3), ('Produce', 4), ('Produce', 5),
--('Dairy', 1), ('Dairy', 2), ('Dairy', 3), ('Dairy', 4), ('Dairy', 5),
--('Bakery', 1), ('Bakery', 2), ('Bakery', 3), ('Bakery', 4), ('Bakery', 5),
--('Meat', 1), ('Meat', 2), ('Meat', 3), ('Meat', 4), ('Meat', 5),
--('Frozen Food', 1), ('Frozen Food', 2), ('Frozen Food', 3), ('Frozen Food', 4), ('Frozen Food', 5);


-- ╔════════════════════════════════════════════════╗
-- ║            Categories Table                    ║
-- ╚════════════════════════════════════════════════╝

---- Grocery Categories for all stores
--INSERT INTO categories (category_name, department_id, store_id) VALUES 
--('Canned Food', 1, 1), ('Canned Food', 1, 2), ('Canned Food', 1, 3), ('Canned Food', 1, 4), ('Canned Food', 1, 5),
--('Pasta', 1, 1), ('Pasta', 1, 2), ('Pasta', 1, 3), ('Pasta', 1, 4), ('Pasta', 1, 5),
--('Sauce', 1, 1), ('Sauce', 1, 2), ('Sauce', 1, 3), ('Sauce', 1, 4), ('Sauce', 1, 5),
--('Snacks', 1, 1), ('Snacks', 1, 2), ('Snacks', 1, 3), ('Snacks', 1, 4), ('Snacks', 1, 5),
--('Chips', 1, 1), ('Chips', 1, 2), ('Chips', 1, 3), ('Chips', 1, 4), ('Chips', 1, 5);

---- Produce Categories for all stores
--INSERT INTO categories (category_name, department_id, store_id) VALUES 
--('Fresh Vegetables', 2, 1), ('Fresh Vegetables', 2, 2), ('Fresh Vegetables', 2, 3), ('Fresh Vegetables', 2, 4), ('Fresh Vegetables', 2, 5),
--('Fresh Fruits', 2, 1), ('Fresh Fruits', 2, 2), ('Fresh Fruits', 2, 3), ('Fresh Fruits', 2, 4), ('Fresh Fruits', 2, 5),
--('Packed Salad & Dressing', 2, 1), ('Packed Salad & Dressing', 2, 2), ('Packed Salad & Dressing', 2, 3), ('Packed Salad & Dressing', 2, 4), ('Packed Salad & Dressing', 2, 5);

---- Dairy Categories for all stores
--INSERT INTO categories (category_name, department_id, store_id) VALUES 
--('Milk & Cream', 3, 1), ('Milk & Cream', 3, 2), ('Milk & Cream', 3, 3), ('Milk & Cream', 3, 4), ('Milk & Cream', 3, 5),
--('Egg', 3, 1), ('Egg', 3, 2), ('Egg', 3, 3), ('Egg', 3, 4), ('Egg', 3, 5),
--('Butter & Cheese', 3, 1), ('Butter & Cheese', 3, 2), ('Butter & Cheese', 3, 3), ('Butter & Cheese', 3, 4), ('Butter & Cheese', 3, 5);

---- Bakery Categories for all stores
--INSERT INTO categories (category_name, department_id, store_id) VALUES 
--('Bread', 4, 1), ('Bread', 4, 2), ('Bread', 4, 3), ('Bread', 4, 4), ('Bread', 4, 5),
--('Bagel, Croissants', 4, 1), ('Bagel, Croissants', 4, 2), ('Bagel, Croissants', 4, 3), ('Bagel, Croissants', 4, 4), ('Bagel, Croissants', 4, 5);

---- Meat Categories for all stores
--INSERT INTO categories (category_name, department_id, store_id) VALUES 
--('Chicken & Turkey', 5, 1), ('Chicken & Turkey', 5, 2), ('Chicken & Turkey', 5, 3), ('Chicken & Turkey', 5, 4), ('Chicken & Turkey', 5, 5),
--('Beef', 5, 1), ('Beef', 5, 2), ('Beef', 5, 3), ('Beef', 5, 4), ('Beef', 5, 5),
--('Bacon', 5, 1), ('Bacon', 5, 2), ('Bacon', 5, 3), ('Bacon', 5, 4), ('Bacon', 5, 5);

---- Frozen Food Categories for all stores
--INSERT INTO categories (category_name, department_id, store_id) VALUES 
--('Fruits & Vegetables', 6, 1), ('Fruits & Vegetables', 6, 2), ('Fruits & Vegetables', 6, 3), ('Fruits & Vegetables', 6, 4), ('Fruits & Vegetables', 6, 5),
--('Pizza', 6, 1), ('Pizza', 6, 2), ('Pizza', 6, 3), ('Pizza', 6, 4), ('Pizza', 6, 5),
--('Ice Cream & Desserts', 6, 1), ('Ice Cream & Desserts', 6, 2), ('Ice Cream & Desserts', 6, 3), ('Ice Cream & Desserts', 6, 4), ('Ice Cream & Desserts', 6, 5);

-- ╔════════════════════════════════════════════════╗
-- ║              Products Table                    ║
-- ╚════════════════════════════════════════════════╝

--delete from products

--select * from products


-- ╔════════════════════════════════════════════════╗
-- ║              Products for Grocery Department   ║
-- ╚════════════════════════════════════════════════╝

---- Canned Food Products across all stores
--INSERT INTO products (product_name, price, status, ingredients, price_valid_from, price_valid_to, category_id, department_id, store_id) VALUES
--('Heinz Original Beans in Tomato Sauce – 398 ml', 2.99, 'in stock', 'Beans, Tomato Sauce', '2024-01-01', '2024-12-31', 1, 1, 1),
--('Heinz Original Beans in Tomato Sauce – 398 ml', 3.19, 'in stock', 'Beans, Tomato Sauce', '2024-01-01', '2024-12-31', 1, 1, 2),
--('Heinz Original Beans in Tomato Sauce – 398 ml', 2.79, 'in stock', 'Beans, Tomato Sauce', '2024-01-01', '2024-12-31', 1, 1, 3),
--('Heinz Original Beans in Tomato Sauce – 398 ml', 3.09, 'in stock', 'Beans, Tomato Sauce', '2024-01-01', '2024-12-31', 1, 1, 4),
--('Heinz Original Beans in Tomato Sauce – 398 ml', 2.89, 'in stock', 'Beans, Tomato Sauce', '2024-01-01', '2024-12-31', 1, 1, 5),

--('Unico Canned Black Beans – 540 ml', 1.99, 'in stock', 'Black Beans, Water, Salt', '2024-01-01', '2024-12-31', 1, 1, 1),
--('Unico Canned Black Beans – 540 ml', 2.09, 'in stock', 'Black Beans, Water, Salt', '2024-01-01', '2024-12-31', 1, 1, 2),
--('Unico Canned Black Beans – 540 ml', 1.89, 'in stock', 'Black Beans, Water, Salt', '2024-01-01', '2024-12-31', 1, 1, 3),
--('Unico Canned Black Beans – 540 ml', 2.19, 'in stock', 'Black Beans, Water, Salt', '2024-01-01', '2024-12-31', 1, 1, 4),
--('Unico Canned Black Beans – 540 ml', 1.79, 'in stock', 'Black Beans, Water, Salt', '2024-01-01', '2024-12-31', 1, 1, 5);

---- Pasta Products across all stores
--INSERT INTO products (product_name, price, status, ingredients, price_valid_from, price_valid_to, category_id, department_id, store_id) VALUES
--('Barilla Penne Rigate Pasta – 410 g', 1.89, 'in stock', 'Durum Wheat Semolina', '2024-01-01', '2024-12-31', 2, 1, 1),
--('Barilla Penne Rigate Pasta – 410 g', 1.99, 'in stock', 'Durum Wheat Semolina', '2024-01-01', '2024-12-31', 2, 1, 2),
--('Barilla Penne Rigate Pasta – 410 g', 1.79, 'in stock', 'Durum Wheat Semolina', '2024-01-01', '2024-12-31', 2, 1, 3),
--('Barilla Penne Rigate Pasta – 410 g', 2.09, 'in stock', 'Durum Wheat Semolina', '2024-01-01', '2024-12-31', 2, 1, 4),
--('Barilla Penne Rigate Pasta – 410 g', 1.99, 'in stock', 'Durum Wheat Semolina', '2024-01-01', '2024-12-31', 2, 1, 5),

--('Lancia Rotini – 750 g', 2.99, 'in stock', 'Durum Wheat Semolina', '2024-01-01', '2024-12-31', 2, 1, 1),
--('Lancia Rotini – 750 g', 3.09, 'in stock', 'Durum Wheat Semolina', '2024-01-01', '2024-12-31', 2, 1, 2),
--('Lancia Rotini – 750 g', 2.89, 'in stock', 'Durum Wheat Semolina', '2024-01-01', '2024-12-31', 2, 1, 3),
--('Lancia Rotini – 750 g', 3.19, 'in stock', 'Durum Wheat Semolina', '2024-01-01', '2024-12-31', 2, 1, 4),
--('Lancia Rotini – 750 g', 2.99, 'in stock', 'Durum Wheat Semolina', '2024-01-01', '2024-12-31', 2, 1, 5);

---- Sauce Products across all stores
--INSERT INTO products (product_name, price, status, ingredients, price_valid_from, price_valid_to, category_id, department_id, store_id) VALUES
--('Classico Four Cheese Pasta Sauce – 600 ml', 3.99, 'in stock', 'Tomatoes, Cheese', '2024-01-01', '2024-12-31', 3, 1, 1),
--('Classico Four Cheese Pasta Sauce – 600 ml', 4.19, 'in stock', 'Tomatoes, Cheese', '2024-01-01', '2024-12-31', 3, 1, 2),
--('Classico Four Cheese Pasta Sauce – 600 ml', 3.89, 'in stock', 'Tomatoes, Cheese', '2024-01-01', '2024-12-31', 3, 1, 3),
--('Classico Four Cheese Pasta Sauce – 600 ml', 4.09, 'in stock', 'Tomatoes, Cheese', '2024-01-01', '2024-12-31', 3, 1, 4),
--('Classico Four Cheese Pasta Sauce – 600 ml', 3.99, 'in stock', 'Tomatoes, Cheese', '2024-01-01', '2024-12-31', 3, 1, 5),

--('President’s Choice Plum Sauce – 750 ml', 2.49, 'in stock', 'Plum, Sugar, Vinegar', '2024-01-01', '2024-12-31', 3, 1, 1),
--('President’s Choice Plum Sauce – 750 ml', 2.69, 'in stock', 'Plum, Sugar, Vinegar', '2024-01-01', '2024-12-31', 3, 1, 2),
--('President’s Choice Plum Sauce – 750 ml', 2.39, 'in stock', 'Plum, Sugar, Vinegar', '2024-01-01', '2024-12-31', 3, 1, 3),
--('President’s Choice Plum Sauce – 750 ml', 2.59, 'in stock', 'Plum, Sugar, Vinegar', '2024-01-01', '2024-12-31', 3, 1, 4),
--('President’s Choice Plum Sauce – 750 ml', 2.49, 'in stock', 'Plum, Sugar, Vinegar', '2024-01-01', '2024-12-31', 3, 1, 5);

---- Snacks Products across all stores
--INSERT INTO products (product_name, price, status, ingredients, price_valid_from, price_valid_to, category_id, department_id, store_id) VALUES
--('Panters Cashews, Roasted & Salted – 200g', 6.99, 'in stock', 'Cashews, Salt', '2024-01-01', '2024-12-31', 4, 1, 1),
--('Panters Cashews, Roasted & Salted – 200g', 7.19, 'in stock', 'Cashews, Salt', '2024-01-01', '2024-12-31', 4, 1, 2),
--('Panters Cashews, Roasted & Salted – 200g', 6.79, 'in stock', 'Cashews, Salt', '2024-01-01', '2024-12-31', 4, 1, 3),
--('Panters Cashews, Roasted & Salted – 200g', 7.09, 'in stock', 'Cashews, Salt', '2024-01-01', '2024-12-31', 4, 1, 4),
--('Panters Cashews, Roasted & Salted – 200g', 6.99, 'in stock', 'Cashews, Salt', '2024-01-01', '2024-12-31', 4, 1, 5),

--('Jack Links, Beef Jerky Famin’ Hot Flavour Original – 75 g', 5.49, 'in stock', 'Beef, Spices', '2024-01-01', '2024-12-31', 4, 1, 1),
--('Jack Links, Beef Jerky Famin’ Hot Flavour Original – 75 g', 5.69, 'in stock', 'Beef, Spices', '2024-01-01', '2024-12-31', 4, 1, 2),
--('Jack Links, Beef Jerky Famin’ Hot Flavour Original – 75 g', 5.29, 'in stock', 'Beef, Spices', '2024-01-01', '2024-12-31', 4, 1, 3),
--('Jack Links, Beef Jerky Famin’ Hot Flavour Original – 75 g', 5.79, 'in stock', 'Beef, Spices', '2024-01-01', '2024-12-31', 4, 1, 4),
--('Jack Links, Beef Jerky Famin’ Hot Flavour Original – 75 g', 5.59, 'in stock', 'Beef, Spices', '2024-01-01', '2024-12-31', 4, 1, 5);

---- Chips Products across all stores
--INSERT INTO products (product_name, price, status, ingredients, price_valid_from, price_valid_to, category_id, department_id, store_id) VALUES
--('Pringles, Mega Can Original Flavour – 194 g', 3.49, 'in stock', 'Potatoes, Oil, Salt', '2024-01-01', '2024-12-31', 5, 1, 1),
--('Pringles, Mega Can Original Flavour – 194 g', 3.69, 'in stock', 'Potatoes, Oil, Salt', '2024-01-01', '2024-12-31', 5, 1, 2),
--('Pringles, Mega Can Original Flavour – 194 g', 3.29, 'in stock', 'Potatoes, Oil, Salt', '2024-01-01', '2024-12-31', 5, 1, 3),
--('Pringles, Mega Can Original Flavour – 194 g', 3.79, 'in stock', 'Potatoes, Oil, Salt', '2024-01-01', '2024-12-31', 5, 1, 4),
--('Pringles, Mega Can Original Flavour – 194 g', 3.59, 'in stock', 'Potatoes, Oil, Salt', '2024-01-01', '2024-12-31', 5, 1, 5),

--('Ruffles Regular Potato Chips – 200 g', 3.99, 'in stock', 'Potatoes, Oil, Salt', '2024-01-01', '2024-12-31', 5, 1, 1),
--('Ruffles Regular Potato Chips – 200 g', 4.19, 'in stock', 'Potatoes, Oil, Salt', '2024-01-01', '2024-12-31', 5, 1, 2),
--('Ruffles Regular Potato Chips – 200 g', 3.89, 'in stock', 'Potatoes, Oil, Salt', '2024-01-01', '2024-12-31', 5, 1, 3),
--('Ruffles Regular Potato Chips – 200 g', 4.09, 'in stock', 'Potatoes, Oil, Salt', '2024-01-01', '2024-12-31', 5, 1, 4),
--('Ruffles Regular Potato Chips – 200 g', 3.99, 'in stock', 'Potatoes, Oil, Salt', '2024-01-01', '2024-12-31', 5, 1, 5);

-- ╔════════════════════════════════════════════════╗
-- ║              Products for Produce Department   ║
-- ╚════════════════════════════════════════════════╝

---- Fresh Vegetables Products across all stores
--INSERT INTO products (product_name, price, status, ingredients, price_valid_from, price_valid_to, category_id, department_id, store_id) VALUES
--('Ginger', 3.49, 'in stock', 'Fresh Ginger Root', '2024-01-01', '2024-12-31', 6, 2, 1),
--('Ginger', 3.69, 'in stock', 'Fresh Ginger Root', '2024-01-01', '2024-12-31', 6, 2, 2),
--('Ginger', 3.39, 'in stock', 'Fresh Ginger Root', '2024-01-01', '2024-12-31', 6, 2, 3),
--('Ginger', 3.59, 'in stock', 'Fresh Ginger Root', '2024-01-01', '2024-12-31', 6, 2, 4),
--('Ginger', 3.79, 'in stock', 'Fresh Ginger Root', '2024-01-01', '2024-12-31', 6, 2, 5),

--('Red Onion', 1.29, 'in stock', 'Fresh Red Onion', '2024-01-01', '2024-12-31', 6, 2, 1),
--('Red Onion', 1.39, 'in stock', 'Fresh Red Onion', '2024-01-01', '2024-12-31', 6, 2, 2),
--('Red Onion', 1.19, 'in stock', 'Fresh Red Onion', '2024-01-01', '2024-12-31', 6, 2, 3),
--('Red Onion', 1.49, 'in stock', 'Fresh Red Onion', '2024-01-01', '2024-12-31', 6, 2, 4),
--('Red Onion', 1.39, 'in stock', 'Fresh Red Onion', '2024-01-01', '2024-12-31', 6, 2, 5);

---- Fresh Fruits Products across all stores
--INSERT INTO products (product_name, price, status, ingredients, price_valid_from, price_valid_to, category_id, department_id, store_id) VALUES
--('Granny Smith Apple', 1.99, 'in stock', 'Fresh Granny Smith Apple', '2024-01-01', '2024-12-31', 7, 2, 1),
--('Granny Smith Apple', 2.09, 'in stock', 'Fresh Granny Smith Apple', '2024-01-01', '2024-12-31', 7, 2, 2),
--('Granny Smith Apple', 1.89, 'in stock', 'Fresh Granny Smith Apple', '2024-01-01', '2024-12-31', 7, 2, 3),
--('Granny Smith Apple', 2.19, 'in stock', 'Fresh Granny Smith Apple', '2024-01-01', '2024-12-31', 7, 2, 4),
--('Granny Smith Apple', 2.29, 'in stock', 'Fresh Granny Smith Apple', '2024-01-01', '2024-12-31', 7, 2, 5),

--('Red Delicious Apple', 1.49, 'in stock', 'Fresh Red Delicious Apple', '2024-01-01', '2024-12-31', 7, 2, 1),
--('Red Delicious Apple', 1.59, 'in stock', 'Fresh Red Delicious Apple', '2024-01-01', '2024-12-31', 7, 2, 2),
--('Red Delicious Apple', 1.39, 'in stock', 'Fresh Red Delicious Apple', '2024-01-01', '2024-12-31', 7, 2, 3),
--('Red Delicious Apple', 1.69, 'in stock', 'Fresh Red Delicious Apple', '2024-01-01', '2024-12-31', 7, 2, 4),
--('Red Delicious Apple', 1.79, 'in stock', 'Fresh Red Delicious Apple', '2024-01-01', '2024-12-31', 7, 2, 5);

---- Packed Salad & Dressing Products across all stores
--INSERT INTO products (product_name, price, status, ingredients, price_valid_from, price_valid_to, category_id, department_id, store_id) VALUES
--('PC Caesar Salad Kit', 4.99, 'in stock', 'Romaine Lettuce, Caesar Dressing, Croutons', '2024-01-01', '2024-12-31', 8, 2, 1),
--('PC Caesar Salad Kit', 5.19, 'in stock', 'Romaine Lettuce, Caesar Dressing, Croutons', '2024-01-01', '2024-12-31', 8, 2, 2),
--('PC Caesar Salad Kit', 4.79, 'in stock', 'Romaine Lettuce, Caesar Dressing, Croutons', '2024-01-01', '2024-12-31', 8, 2, 3),
--('PC Caesar Salad Kit', 5.09, 'in stock', 'Romaine Lettuce, Caesar Dressing, Croutons', '2024-01-01', '2024-12-31', 8, 2, 4),
--('PC Caesar Salad Kit', 5.29, 'in stock', 'Romaine Lettuce, Caesar Dressing, Croutons', '2024-01-01', '2024-12-31', 8, 2, 5),

--('Cello Spinach', 3.49, 'in stock', 'Fresh Spinach', '2024-01-01', '2024-12-31', 8, 2, 1),
--('Cello Spinach', 3.69, 'in stock', 'Fresh Spinach', '2024-01-01', '2024-12-31', 8, 2, 2),
--('Cello Spinach', 3.39, 'in stock', 'Fresh Spinach', '2024-01-01', '2024-12-31', 8, 2, 3),
--('Cello Spinach', 3.59, 'in stock', 'Fresh Spinach', '2024-01-01', '2024-12-31', 8, 2, 4),
--('Cello Spinach', 3.79, 'in stock', 'Fresh Spinach', '2024-01-01', '2024-12-31', 8, 2, 5);

-- ╔════════════════════════════════════════════════╗
-- ║              Products for Dairy Department     ║
-- ╚════════════════════════════════════════════════╝

---- Milk & Cream Products across all stores
--INSERT INTO products (product_name, price, status, ingredients, price_valid_from, price_valid_to, category_id, department_id, store_id) VALUES
--('Fairlife Chocolate Lactose Free 2% partly Skimmed Milk – 1.5 L', 5.49, 'in stock', 'Milk, Cocoa, Sugar, Lactase Enzyme', '2024-01-01', '2024-12-31', 9, 3, 1),
--('Fairlife Chocolate Lactose Free 2% partly Skimmed Milk – 1.5 L', 5.69, 'in stock', 'Milk, Cocoa, Sugar, Lactase Enzyme', '2024-01-01', '2024-12-31', 9, 3, 2),
--('Fairlife Chocolate Lactose Free 2% partly Skimmed Milk – 1.5 L', 5.29, 'in stock', 'Milk, Cocoa, Sugar, Lactase Enzyme', '2024-01-01', '2024-12-31', 9, 3, 3),
--('Fairlife Chocolate Lactose Free 2% partly Skimmed Milk – 1.5 L', 5.89, 'in stock', 'Milk, Cocoa, Sugar, Lactase Enzyme', '2024-01-01', '2024-12-31', 9, 3, 4),
--('Fairlife Chocolate Lactose Free 2% partly Skimmed Milk – 1.5 L', 5.59, 'in stock', 'Milk, Cocoa, Sugar, Lactase Enzyme', '2024-01-01', '2024-12-31', 9, 3, 5),

--('Silk Almond For Coffee, Vanilla Flavour – 890 ml', 3.99, 'in stock', 'Almond Milk, Vanilla Flavoring', '2024-01-01', '2024-12-31', 9, 3, 1),
--('Silk Almond For Coffee, Vanilla Flavour – 890 ml', 4.19, 'in stock', 'Almond Milk, Vanilla Flavoring', '2024-01-01', '2024-12-31', 9, 3, 2),
--('Silk Almond For Coffee, Vanilla Flavour – 890 ml', 3.79, 'in stock', 'Almond Milk, Vanilla Flavoring', '2024-01-01', '2024-12-31', 9, 3, 3),
--('Silk Almond For Coffee, Vanilla Flavour – 890 ml', 4.09, 'in stock', 'Almond Milk, Vanilla Flavoring', '2024-01-01', '2024-12-31', 9, 3, 4),
--('Silk Almond For Coffee, Vanilla Flavour – 890 ml', 3.89, 'in stock', 'Almond Milk, Vanilla Flavoring', '2024-01-01', '2024-12-31', 9, 3, 5);

---- Egg Products across all stores
--INSERT INTO products (product_name, price, status, ingredients, price_valid_from, price_valid_to, category_id, department_id, store_id) VALUES
--('No Name Large Grade A Eggs 12ea', 2.99, 'in stock', 'Grade A Eggs', '2024-01-01', '2024-12-31', 10, 3, 1),
--('No Name Large Grade A Eggs 12ea', 3.19, 'in stock', 'Grade A Eggs', '2024-01-01', '2024-12-31', 10, 3, 2),
--('No Name Large Grade A Eggs 12ea', 2.79, 'in stock', 'Grade A Eggs', '2024-01-01', '2024-12-31', 10, 3, 3),
--('No Name Large Grade A Eggs 12ea', 3.09, 'in stock', 'Grade A Eggs', '2024-01-01', '2024-12-31', 10, 3, 4),
--('No Name Large Grade A Eggs 12ea', 2.89, 'in stock', 'Grade A Eggs', '2024-01-01', '2024-12-31', 10, 3, 5),

--('PC Free Run Brown Eggs Large – 12ea', 4.49, 'in stock', 'Free Run Brown Eggs', '2024-01-01', '2024-12-31', 10, 3, 1),
--('PC Free Run Brown Eggs Large – 12ea', 4.69, 'in stock', 'Free Run Brown Eggs', '2024-01-01', '2024-12-31', 10, 3, 2),
--('PC Free Run Brown Eggs Large – 12ea', 4.29, 'in stock', 'Free Run Brown Eggs', '2024-01-01', '2024-12-31', 10, 3, 3),
--('PC Free Run Brown Eggs Large – 12ea', 4.59, 'in stock', 'Free Run Brown Eggs', '2024-01-01', '2024-12-31', 10, 3, 4),
--('PC Free Run Brown Eggs Large – 12ea', 4.39, 'in stock', 'Free Run Brown Eggs', '2024-01-01', '2024-12-31', 10, 3, 5);

---- Butter & Cheese Products across all stores
--INSERT INTO products (product_name, price, status, ingredients, price_valid_from, price_valid_to, category_id, department_id, store_id) VALUES
--('Lactania Salted Butter', 3.99, 'in stock', 'Cream, Salt', '2024-01-01', '2024-12-31', 11, 3, 1),
--('Lactania Salted Butter', 4.19, 'in stock', 'Cream, Salt', '2024-01-01', '2024-12-31', 11, 3, 2),
--('Lactania Salted Butter', 3.79, 'in stock', 'Cream, Salt', '2024-01-01', '2024-12-31', 11, 3, 3),
--('Lactania Salted Butter', 4.09, 'in stock', 'Cream, Salt', '2024-01-01', '2024-12-31', 11, 3, 4),
--('Lactania Salted Butter', 3.89, 'in stock', 'Cream, Salt', '2024-01-01', '2024-12-31', 11, 3, 5),

--('No Name Unsalted Butter', 3.69, 'in stock', 'Cream', '2024-01-01', '2024-12-31', 11, 3, 1),
--('No Name Unsalted Butter', 3.89, 'in stock', 'Cream', '2024-01-01', '2024-12-31', 11, 3, 2),
--('No Name Unsalted Butter', 3.49, 'in stock', 'Cream', '2024-01-01', '2024-12-31', 11, 3, 3),
--('No Name Unsalted Butter', 3.79, 'in stock', 'Cream', '2024-01-01', '2024-12-31', 11, 3, 4),
--('No Name Unsalted Butter', 3.59, 'in stock', 'Cream', '2024-01-01', '2024-12-31', 11, 3, 5);

-- ╔════════════════════════════════════════════════╗
-- ║              Products for Bakery Department    ║
-- ╚════════════════════════════════════════════════╝

---- Bread Products across all stores
--INSERT INTO products (product_name, price, status, ingredients, price_valid_from, price_valid_to, category_id, department_id, store_id) VALUES
--('Country Harvest Whole Wheat Oats & Honey Bread', 2.99, 'in stock', 'Whole Wheat Flour, Honey, Oats', '2024-01-01', '2024-12-31', 13, 4, 1),
--('Country Harvest Whole Wheat Oats & Honey Bread', 3.19, 'in stock', 'Whole Wheat Flour, Honey, Oats', '2024-01-01', '2024-12-31', 13, 4, 2),
--('Country Harvest Whole Wheat Oats & Honey Bread', 2.79, 'in stock', 'Whole Wheat Flour, Honey, Oats', '2024-01-01', '2024-12-31', 13, 4, 3),
--('Country Harvest Whole Wheat Oats & Honey Bread', 3.09, 'in stock', 'Whole Wheat Flour, Honey, Oats', '2024-01-01', '2024-12-31', 13, 4, 4),
--('Country Harvest Whole Wheat Oats & Honey Bread', 2.89, 'in stock', 'Whole Wheat Flour, Honey, Oats', '2024-01-01', '2024-12-31', 13, 4, 5),

--('Furlani Ready Bake Garlic Toast Texas – Style Bread', 3.49, 'in stock', 'Bread, Garlic Butter', '2024-01-01', '2024-12-31', 13, 4, 1),
--('Furlani Ready Bake Garlic Toast Texas – Style Bread', 3.69, 'in stock', 'Bread, Garlic Butter', '2024-01-01', '2024-12-31', 13, 4, 2),
--('Furlani Ready Bake Garlic Toast Texas – Style Bread', 3.29, 'in stock', 'Bread, Garlic Butter', '2024-01-01', '2024-12-31', 13, 4, 3),
--('Furlani Ready Bake Garlic Toast Texas – Style Bread', 3.59, 'in stock', 'Bread, Garlic Butter', '2024-01-01', '2024-12-31', 13, 4, 4),
--('Furlani Ready Bake Garlic Toast Texas – Style Bread', 3.39, 'in stock', 'Bread, Garlic Butter', '2024-01-01', '2024-12-31', 13, 4, 5);

---- Bagel, Croissants Products across all stores
--INSERT INTO products (product_name, price, status, ingredients, price_valid_from, price_valid_to, category_id, department_id, store_id) VALUES
--('Farmer’s Market Butter Croissant', 4.99, 'in stock', 'Butter, Flour, Sugar, Yeast', '2024-01-01', '2024-12-31', 14, 4, 1),
--('Farmer’s Market Butter Croissant', 5.19, 'in stock', 'Butter, Flour, Sugar, Yeast', '2024-01-01', '2024-12-31', 14, 4, 2),
--('Farmer’s Market Butter Croissant', 4.79, 'in stock', 'Butter, Flour, Sugar, Yeast', '2024-01-01', '2024-12-31', 14, 4, 3),
--('Farmer’s Market Butter Croissant', 5.09, 'in stock', 'Butter, Flour, Sugar, Yeast', '2024-01-01', '2024-12-31', 14, 4, 4),
--('Farmer’s Market Butter Croissant', 4.89, 'in stock', 'Butter, Flour, Sugar, Yeast', '2024-01-01', '2024-12-31', 14, 4, 5),

--('No Name Bagel Plain, 6 Pack', 2.49, 'in stock', 'Wheat Flour, Water, Salt, Yeast', '2024-01-01', '2024-12-31', 14, 4, 1),
--('No Name Bagel Plain, 6 Pack', 2.69, 'in stock', 'Wheat Flour, Water, Salt, Yeast', '2024-01-01', '2024-12-31', 14, 4, 2),
--('No Name Bagel Plain, 6 Pack', 2.29, 'in stock', 'Wheat Flour, Water, Salt, Yeast', '2024-01-01', '2024-12-31', 14, 4, 3),
--('No Name Bagel Plain, 6 Pack', 2.59, 'in stock', 'Wheat Flour, Water, Salt, Yeast', '2024-01-01', '2024-12-31', 14, 4, 4),
--('No Name Bagel Plain, 6 Pack', 2.39, 'in stock', 'Wheat Flour, Water, Salt, Yeast', '2024-01-01', '2024-12-31', 14, 4, 5);

-- ╔════════════════════════════════════════════════╗
-- ║              Products for Meat Department      ║
-- ╚════════════════════════════════════════════════╝

-- Chicken & Turkey Products across all stores
--INSERT INTO products (product_name, price, status, ingredients, price_valid_from, price_valid_to, category_id, department_id, store_id) VALUES
--('Sufra Halal Chicken Nuggets – 840 g', 8.99, 'in stock', 'Chicken, Wheat Flour, Spices', '2024-01-01', '2024-12-31', 16, 5, 1),
--('Sufra Halal Chicken Nuggets – 840 g', 9.19, 'in stock', 'Chicken, Wheat Flour, Spices', '2024-01-01', '2024-12-31', 16, 5, 2),
--('Sufra Halal Chicken Nuggets – 840 g', 8.79, 'in stock', 'Chicken, Wheat Flour, Spices', '2024-01-01', '2024-12-31', 16, 5, 3),
--('Sufra Halal Chicken Nuggets – 840 g', 9.09, 'in stock', 'Chicken, Wheat Flour, Spices', '2024-01-01', '2024-12-31', 16, 5, 4),
--('Sufra Halal Chicken Nuggets – 840 g', 8.89, 'in stock', 'Chicken, Wheat Flour, Spices', '2024-01-01', '2024-12-31', 16, 5, 5),

--('Chicken Leg with Bone, Club Pack', 4.99, 'in stock', 'Fresh Chicken', '2024-01-01', '2024-12-31', 16, 5, 1),
--('Chicken Leg with Bone, Club Pack', 5.19, 'in stock', 'Fresh Chicken', '2024-01-01', '2024-12-31', 16, 5, 2),
--('Chicken Leg with Bone, Club Pack', 4.79, 'in stock', 'Fresh Chicken', '2024-01-01', '2024-12-31', 16, 5, 3),
--('Chicken Leg with Bone, Club Pack', 5.09, 'in stock', 'Fresh Chicken', '2024-01-01', '2024-12-31', 16, 5, 4),
--('Chicken Leg with Bone, Club Pack', 4.89, 'in stock', 'Fresh Chicken', '2024-01-01', '2024-12-31', 16, 5, 5);

---- Beef Products across all stores
--INSERT INTO products (product_name, price, status, ingredients, price_valid_from, price_valid_to, category_id, department_id, store_id) VALUES
--('Lean Ground Beef, Club Pack', 6.49, 'in stock', 'Lean Ground Beef', '2024-01-01', '2024-12-31', 17, 5, 1),
--('Lean Ground Beef, Club Pack', 6.69, 'in stock', 'Lean Ground Beef', '2024-01-01', '2024-12-31', 17, 5, 2),
--('Lean Ground Beef, Club Pack', 6.29, 'in stock', 'Lean Ground Beef', '2024-01-01', '2024-12-31', 17, 5, 3),
--('Lean Ground Beef, Club Pack', 6.79, 'in stock', 'Lean Ground Beef', '2024-01-01', '2024-12-31', 17, 5, 4),
--('Lean Ground Beef, Club Pack', 6.59, 'in stock', 'Lean Ground Beef', '2024-01-01', '2024-12-31', 17, 5, 5),

--('Extra Lean Ground Beef', 7.49, 'in stock', 'Extra Lean Ground Beef', '2024-01-01', '2024-12-31', 17, 5, 1),
--('Extra Lean Ground Beef', 7.69, 'in stock', 'Extra Lean Ground Beef', '2024-01-01', '2024-12-31', 17, 5, 2),
--('Extra Lean Ground Beef', 7.29, 'in stock', 'Extra Lean Ground Beef', '2024-01-01', '2024-12-31', 17, 5, 3),
--('Extra Lean Ground Beef', 7.79, 'in stock', 'Extra Lean Ground Beef', '2024-01-01', '2024-12-31', 17, 5, 4),
--('Extra Lean Ground Beef', 7.59, 'in stock', 'Extra Lean Ground Beef', '2024-01-01', '2024-12-31', 17, 5, 5);

---- Bacon Products across all stores
--INSERT INTO products (product_name, price, status, ingredients, price_valid_from, price_valid_to, category_id, department_id, store_id) VALUES
--('PC Bacon – 500 g', 4.99, 'in stock', 'Pork, Salt, Sugar', '2024-01-01', '2024-12-31', 18, 5, 1),
--('PC Bacon – 500 g', 5.19, 'in stock', 'Pork, Salt, Sugar', '2024-01-01', '2024-12-31', 18, 5, 2),
--('PC Bacon – 500 g', 4.79, 'in stock', 'Pork, Salt, Sugar', '2024-01-01', '2024-12-31', 18, 5, 3),
--('PC Bacon – 500 g', 5.09, 'in stock', 'Pork, Salt, Sugar', '2024-01-01', '2024-12-31', 18, 5, 4),
--('PC Bacon – 500 g', 4.89, 'in stock', 'Pork, Salt, Sugar', '2024-01-01', '2024-12-31', 18, 5, 5),

--('No Name Mild Sugar-Cured Bacon', 3.99, 'in stock', 'Pork, Salt, Sugar', '2024-01-01', '2024-12-31', 18, 5, 1),
--('No Name Mild Sugar-Cured Bacon', 4.19, 'in stock', 'Pork, Salt, Sugar', '2024-01-01', '2024-12-31', 18, 5, 2),
--('No Name Mild Sugar-Cured Bacon', 3.79, 'in stock', 'Pork, Salt, Sugar', '2024-01-01', '2024-12-31', 18, 5, 3),
--('No Name Mild Sugar-Cured Bacon', 4.09, 'in stock', 'Pork, Salt, Sugar', '2024-01-01', '2024-12-31', 18, 5, 4),
--('No Name Mild Sugar-Cured Bacon', 3.89, 'in stock', 'Pork, Salt, Sugar', '2024-01-01', '2024-12-31', 18, 5, 5);


-- ╔════════════════════════════════════════════════╗
-- ║         Products for Frozen Food Department    ║
-- ╚════════════════════════════════════════════════╝

---- Fruits & Vegetables Products across all stores
--INSERT INTO products (product_name, price, status, ingredients, price_valid_from, price_valid_to, category_id, department_id, store_id) VALUES
--('PC Blueberries Cultivated – 600 g', 4.49, 'in stock', 'Blueberries', '2024-01-01', '2024-12-31', 19, 6, 1),
--('PC Blueberries Cultivated – 600 g', 4.69, 'in stock', 'Blueberries', '2024-01-01', '2024-12-31', 19, 6, 2),
--('PC Blueberries Cultivated – 600 g', 4.29, 'in stock', 'Blueberries', '2024-01-01', '2024-12-31', 19, 6, 3),
--('PC Blueberries Cultivated – 600 g', 4.59, 'in stock', 'Blueberries', '2024-01-01', '2024-12-31', 19, 6, 4),
--('PC Blueberries Cultivated – 600 g', 4.39, 'in stock', 'Blueberries', '2024-01-01', '2024-12-31', 19, 6, 5),

--('Green Giant Summer Sweet Peas – 750 g', 3.99, 'in stock', 'Peas', '2024-01-01', '2024-12-31', 19, 6, 1),
--('Green Giant Summer Sweet Peas – 750 g', 4.19, 'in stock', 'Peas', '2024-01-01', '2024-12-31', 19, 6, 2),
--('Green Giant Summer Sweet Peas – 750 g', 3.79, 'in stock', 'Peas', '2024-01-01', '2024-12-31', 19, 6, 3),
--('Green Giant Summer Sweet Peas – 750 g', 4.09, 'in stock', 'Peas', '2024-01-01', '2024-12-31', 19, 6, 4),
--('Green Giant Summer Sweet Peas – 750 g', 3.89, 'in stock', 'Peas', '2024-01-01', '2024-12-31', 19, 6, 5);

---- Pizza Products across all stores
--INSERT INTO products (product_name, price, status, ingredients, price_valid_from, price_valid_to, category_id, department_id, store_id) VALUES
--('Dr Oetker Rising Crust Pepperoni Pizza – 720 g', 6.99, 'in stock', 'Pepperoni, Cheese, Wheat Flour', '2024-01-01', '2024-12-31', 20, 6, 1),
--('Dr Oetker Rising Crust Pepperoni Pizza – 720 g', 7.19, 'in stock', 'Pepperoni, Cheese, Wheat Flour', '2024-01-01', '2024-12-31', 20, 6, 2),
--('Dr Oetker Rising Crust Pepperoni Pizza – 720 g', 6.79, 'in stock', 'Pepperoni, Cheese, Wheat Flour', '2024-01-01', '2024-12-31', 20, 6, 3),
--('Dr Oetker Rising Crust Pepperoni Pizza – 720 g', 7.09, 'in stock', 'Pepperoni, Cheese, Wheat Flour', '2024-01-01', '2024-12-31', 20, 6, 4),
--('Dr Oetker Rising Crust Pepperoni Pizza – 720 g', 6.89, 'in stock', 'Pepperoni, Cheese, Wheat Flour', '2024-01-01', '2024-12-31', 20, 6, 5),

--('Dr Oetker Thin Crust Spinach Pizza – 390 g', 5.99, 'in stock', 'Spinach, Cheese, Wheat Flour', '2024-01-01', '2024-12-31', 20, 6, 1),
--('Dr Oetker Thin Crust Spinach Pizza – 390 g', 6.19, 'in stock', 'Spinach, Cheese, Wheat Flour', '2024-01-01', '2024-12-31', 20, 6, 2),
--('Dr Oetker Thin Crust Spinach Pizza – 390 g', 5.79, 'in stock', 'Spinach, Cheese, Wheat Flour', '2024-01-01', '2024-12-31', 20, 6, 3),
--('Dr Oetker Thin Crust Spinach Pizza – 390 g', 6.09, 'in stock', 'Spinach, Cheese, Wheat Flour', '2024-01-01', '2024-12-31', 20, 6, 4),
--('Dr Oetker Thin Crust Spinach Pizza – 390 g', 5.89, 'in stock', 'Spinach, Cheese, Wheat Flour', '2024-01-01', '2024-12-31', 20, 6, 5);

---- Ice Cream & Desserts Products across all stores
--INSERT INTO products (product_name, price, status, ingredients, price_valid_from, price_valid_to, category_id, department_id, store_id) VALUES
--('Kawartha Premium Ice Cream Made with Fresh Milk & Cream Moose – 1.5 L', 7.99, 'in stock', 'Milk, Cream, Sugar', '2024-01-01', '2024-12-31', 21, 6, 1),
--('Kawartha Premium Ice Cream Made with Fresh Milk & Cream Moose – 1.5 L', 8.19, 'in stock', 'Milk, Cream, Sugar', '2024-01-01', '2024-12-31', 21, 6, 2),
--('Kawartha Premium Ice Cream Made with Fresh Milk & Cream Moose – 1.5 L', 7.79, 'in stock', 'Milk, Cream, Sugar', '2024-01-01', '2024-12-31', 21, 6, 3),
--('Kawartha Premium Ice Cream Made with Fresh Milk & Cream Moose – 1.5 L', 8.09, 'in stock', 'Milk, Cream, Sugar', '2024-01-01', '2024-12-31', 21, 6, 4),
--('Kawartha Premium Ice Cream Made with Fresh Milk & Cream Moose – 1.5 L', 7.89, 'in stock', 'Milk, Cream, Sugar', '2024-01-01', '2024-12-31', 21, 6, 5),

--('No Name Vanilla Ice Cream Sandwiches – 24x120 ml', 6.49, 'in stock', 'Vanilla Ice Cream, Chocolate Wafer', '2024-01-01', '2024-12-31', 21, 6, 1),
--('No Name Vanilla Ice Cream Sandwiches – 24x120 ml', 6.69, 'in stock', 'Vanilla Ice Cream, Chocolate Wafer', '2024-01-01', '2024-12-31', 21, 6, 2),
--('No Name Vanilla Ice Cream Sandwiches – 24x120 ml', 6.29, 'in stock', 'Vanilla Ice Cream, Chocolate Wafer', '2024-01-01', '2024-12-31', 21, 6, 3),
--('No Name Vanilla Ice Cream Sandwiches – 24x120 ml', 6.59, 'in stock', 'Vanilla Ice Cream, Chocolate Wafer', '2024-01-01', '2024-12-31', 21, 6, 4),
--('No Name Vanilla Ice Cream Sandwiches – 24x120 ml', 6.39, 'in stock', 'Vanilla Ice Cream, Chocolate Wafer', '2024-01-01', '2024-12-31', 21, 6, 5);

-- ╔════════════════════════════════════════════════╗
-- ║              Search Logs Table                 ║
-- ╚════════════════════════════════════════════════╝

-- INSERT INTO search_logs(search_term, user_id) 
-- VALUES 
-- ('No Name', 1),
-- ('Heinz', 5),
-- ('Chips', 8), 
-- ('pasta', 10)
