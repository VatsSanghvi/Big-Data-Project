DBCC CHECKIDENT ('products', RESEED, 0);
	
INSERT INTO products (
    product_name, stock_quantity, price, status, fk_category_id, fk_department_id, fk_store_id
)
VALUES
    -- Canned Goods for Grocery Department
    ('Canned Beans - Walmart', 100, 1.99, 'In Stock', 1, 1, 1),
    ('Canned Beans - Zehrs', 120, 2.09, 'In Stock', 2, 2, 2),
    ('Canned Beans - FreshCo', 90, 1.89, 'In Stock', 3, 3, 3),
    ('Canned Beans - No Frills', 110, 2.19, 'In Stock', 4, 4, 4),
    ('Canned Beans - Costco', 95, 2.29, 'In Stock', 5, 5, 5),

    ('Snacks - Walmart', 80, 1.49, 'In Stock', 6, 1, 1),
    ('Snacks - Zehrs', 90, 1.59, 'In Stock', 7, 2, 2),
    ('Snacks - FreshCo', 70, 1.39, 'In Stock', 8, 3, 3),
    ('Snacks - No Frills', 100, 1.69, 'In Stock', 9, 4, 4),
    ('Snacks - Costco', 85, 1.59, 'In Stock', 10, 5, 5),

    -- Milk for Dairy Department
    ('Milk - Walmart', 50, 2.49, 'In Stock', 21, 11, 1),
    ('Milk - Zehrs', 60, 2.59, 'In Stock', 22, 12, 2),
    ('Milk - FreshCo', 55, 2.39, 'In Stock', 23, 13, 3),
    ('Milk - No Frills', 40, 2.69, 'In Stock', 24, 14, 4),
    ('Milk - Costco', 30, 2.59, 'In Stock', 25, 15, 5),

    -- Cheese for Dairy Department
    ('Cheddar Cheese - Walmart', 40, 3.99, 'In Stock', 26, 11, 1),
    ('Cheddar Cheese - Zehrs', 50, 4.09, 'In Stock', 27, 12, 2),
    ('Cheddar Cheese - FreshCo', 45, 3.89, 'In Stock', 28, 13, 3),
    ('Cheddar Cheese - No Frills', 35, 4.19, 'In Stock', 29, 14, 4),
    ('Cheddar Cheese - Costco', 25, 3.99, 'In Stock', 30, 15, 5),

    -- Bread for Bakery Department
    ('Whole Wheat Bread - Walmart', 100, 2.99, 'In Stock', 31, 16, 1),
    ('Whole Wheat Bread - Zehrs', 120, 3.09, 'In Stock', 32, 17, 2),
    ('Whole Wheat Bread - FreshCo', 90, 2.79, 'In Stock', 33, 18, 3),
    ('Whole Wheat Bread - No Frills', 110, 3.19, 'In Stock', 34, 19, 4),
    ('Whole Wheat Bread - Costco', 95, 2.99, 'In Stock', 35, 20, 5),

    -- Pastries for Bakery Department
    ('Butter Croissant - Walmart', 80, 4.99, 'In Stock', 36, 16, 1),
    ('Butter Croissant - Zehrs', 90, 5.19, 'In Stock', 37, 17, 2),
    ('Butter Croissant - FreshCo', 70, 4.79, 'In Stock', 38, 18, 3),
    ('Butter Croissant - No Frills', 100, 5.09, 'In Stock', 39, 19, 4),
    ('Butter Croissant - Costco', 85, 4.99, 'In Stock', 40, 20, 5),

    -- Chicken for Meat Department
    ('Chicken Breast - Walmart', 60, 4.99, 'In Stock', 41, 21, 1),
    ('Chicken Breast - Zehrs', 50, 5.09, 'In Stock', 42, 22, 2),
    ('Chicken Breast - FreshCo', 55, 4.89, 'In Stock', 43, 23, 3),
    ('Chicken Breast - No Frills', 40, 5.19, 'In Stock', 44, 24, 4),
    ('Chicken Breast - Costco', 45, 4.99, 'In Stock', 45, 25, 5),

    -- Beef for Meat Department
    ('Ground Beef - Walmart', 70, 6.49, 'In Stock', 46, 21, 1),
    ('Ground Beef - Zehrs', 80, 6.59, 'In Stock', 47, 22, 2),
    ('Ground Beef - FreshCo', 65, 6.39, 'In Stock', 48, 23, 3),
    ('Ground Beef - No Frills', 75, 6.69, 'In Stock', 49, 24, 4),
    ('Ground Beef - Costco', 85, 6.49, 'In Stock', 50, 25, 5),

    -- Frozen Vegetables for Frozen Department
    ('Frozen Peas - Walmart', 70, 1.79, 'In Stock', 51, 26, 1),
    ('Frozen Peas - Zehrs', 80, 1.89, 'In Stock', 52, 27, 2),
    ('Frozen Peas - FreshCo', 75, 1.69, 'In Stock', 53, 28, 3),
    ('Frozen Peas - No Frills', 90, 1.99, 'In Stock', 54, 29, 4),
    ('Frozen Peas - Costco', 85, 1.89, 'In Stock', 55, 30, 5),

    -- Ice Cream for Frozen Department
    ('Vanilla Ice Cream - Walmart', 50, 4.99, 'In Stock', 56, 26, 1),
    ('Vanilla Ice Cream - Zehrs', 60, 5.09, 'In Stock', 57, 27, 2),
    ('Vanilla Ice Cream - FreshCo', 55, 4.89, 'In Stock', 58, 28, 3),
    ('Vanilla Ice Cream - No Frills', 45, 5.19, 'In Stock', 59, 29, 4),
    ('Vanilla Ice Cream - Costco', 40, 4.99, 'In Stock', 60, 30, 5);
