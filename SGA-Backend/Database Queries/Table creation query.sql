-- USER Table
CREATE TABLE [USER] (
    user_id INT PRIMARY KEY,
    user_name VARCHAR(50) NOT NULL,
    email VARCHAR(255) NOT NULL CHECK (
        email LIKE '%@gmail.com' OR 
        email LIKE '%@yahoo.com' OR 
        email LIKE '%@hotmail.com' OR 
        email LIKE '%@icloud.com'
    ),
    password_hash VARCHAR(255) NOT NULL,
    phone_number CHAR(10) CHECK (phone_number LIKE '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]'),
    address VARCHAR(255),
    role VARCHAR(20) NOT NULL CHECK (role IN ('admin', 'manager', 'user')),
    created_at DATE DEFAULT GETDATE(),
    last_login DATE
);

-- STORE Table
CREATE TABLE STORE (
    store_id INT PRIMARY KEY,
    store_name VARCHAR(100) NOT NULL,
    location VARCHAR(255),
    manager_id INT,
    user_fk INT,
    FOREIGN KEY (user_fk) REFERENCES [USER](user_id)
);



-- CATEGORY Table
CREATE TABLE CATEGORY (
    category_id INT PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL,
    description VARCHAR(255)
);

-- PRODUCT Table
CREATE TABLE PRODUCT (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category_id INT,
    in_stock BIT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (category_id) REFERENCES CATEGORY(category_id)
);

-- GROCERYLIST Table
CREATE TABLE GROCERYLIST (
    list_id INT PRIMARY KEY IDENTITY(1,1),
    user_id INT NOT NULL,
    list_name VARCHAR(100),
    created_at DATE DEFAULT GETDATE(),
    FOREIGN KEY (user_id) REFERENCES [USER](user_id)
);

-- GROCERYLIST_PRODUCTS Table
CREATE TABLE GROCERYLIST_PRODUCTS (
    list_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT DEFAULT 1,
    FOREIGN KEY (list_id) REFERENCES GROCERYLIST(list_id),
    FOREIGN KEY (product_id) REFERENCES PRODUCT(product_id),
    PRIMARY KEY (list_id, product_id)
);

-- ORDER Table
CREATE TABLE [ORDER] (
    order_id INT PRIMARY KEY IDENTITY(1,1),
    user_id INT NOT NULL,
    order_date DATETIME DEFAULT GETDATE(),
    total_amount FLOAT CHECK (total_amount >= 0),
    FOREIGN KEY (user_id) REFERENCES [USER](user_id)
);

-- PRODUCTS_ORDER Table
CREATE TABLE PRODUCTS_ORDER (
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT,
    price_at_order FLOAT,
    FOREIGN KEY (order_id) REFERENCES [ORDER](order_id),
    FOREIGN KEY (product_id) REFERENCES PRODUCT(product_id),
    PRIMARY KEY (order_id, product_id)
);

-- FLYER_TABLE Table
CREATE TABLE FLYER_TABLE (
    flyer_id INT PRIMARY KEY,
    store_id INT NOT NULL,
    flyer_start_date DATE NOT NULL,
    flyer_end_date DATE NOT NULL,
    flyer_name VARCHAR(100),
    description VARCHAR(255),
    CHECK (flyer_start_date <= flyer_end_date),
    FOREIGN KEY (store_id) REFERENCES STORE(store_id)
);

-- NOTIFICATION Table
CREATE TABLE NOTIFICATION (
    notification_id INT PRIMARY KEY,
    user_id INT NOT NULL,
    notification_type VARCHAR(50) NOT NULL,
    notification_content VARCHAR(255),
    date_sent DATETIME DEFAULT GETDATE(),
    is_read BIT DEFAULT 0,
    FOREIGN KEY (user_id) REFERENCES [USER](user_id)
);

-- PRICE_COMPARISON Table
CREATE TABLE PRICE_COMPARISON (
    product_id INT,
    store_id INT,
    max_quantity INT,
    max_price DECIMAL(10, 2),
    last_updated DATE,
    FOREIGN KEY (product_id) REFERENCES PRODUCT(product_id),
    FOREIGN KEY (store_id) REFERENCES STORE(store_id),
    PRIMARY KEY (product_id, store_id)
);
