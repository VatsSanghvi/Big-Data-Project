---- Create the database
--CREATE DATABASE smart_grocery_assistant;

---- Switch to the newly created database
--USE smart_grocery_assistant;

-- Users Table
CREATE TABLE users (
    user_id INT IDENTITY(1,1) PRIMARY KEY,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    email VARCHAR(254) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    phone_number VARCHAR(10) CHECK (LEN(phone_number) = 10),
    role VARCHAR(10) NOT NULL CHECK (role IN ('admin', 'manager', 'customer'))
);

-- Stores Table
CREATE TABLE stores (
    store_id INT IDENTITY(1,1) PRIMARY KEY,
    store_name VARCHAR(100) NOT NULL,
    location VARCHAR(255),
    fk_owner_id INT FOREIGN KEY REFERENCES users(user_id) ON DELETE SET NULL
);

-- Flyers Table
CREATE TABLE flyers (
    flyer_id INT IDENTITY(1,1) PRIMARY KEY,
    flyer_start_date DATE NOT NULL,
    flyer_end_date DATE NOT NULL,
    fk_store_id INT FOREIGN KEY REFERENCES stores(store_id) ON DELETE CASCADE
);

-- Departments Table
CREATE TABLE departments (
    department_id INT IDENTITY(1,1) PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL,
    fk_store_id INT FOREIGN KEY REFERENCES stores(store_id) ON DELETE NO ACTION
);

-- Categories Table
CREATE TABLE categories (
    category_id INT IDENTITY(1,1) PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL,
    fk_department_id INT FOREIGN KEY REFERENCES departments(department_id) ON DELETE NO ACTION
);

-- Products Table
CREATE TABLE products (
    product_id INT IDENTITY(1,1) PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL, --UNIQUE,
    stock_quantity INT DEFAULT 0,
    price DECIMAL(12, 2) NOT NULL CHECK (price >= 0),
    status VARCHAR(10) NOT NULL CHECK (status IN ('In Stock', 'Out Of Stock')) DEFAULT 'In Stock',
    unit_of_measure VARCHAR(20) DEFAULT 'unit',
    ingredients TEXT,
    price_valid_from DATE,
    price_valid_to DATE,
    fk_category_id INT FOREIGN KEY REFERENCES categories(category_id) ON DELETE SET NULL,
    fk_department_id INT FOREIGN KEY REFERENCES departments(department_id) ON DELETE SET NULL,
    fk_store_id INT FOREIGN KEY REFERENCES stores(store_id) ON DELETE SET NULL
);

-- Carts Table
CREATE TABLE carts (
    cart_id INT IDENTITY(1,1) PRIMARY KEY,
    fk_user_id INT FOREIGN KEY REFERENCES users(user_id) ON DELETE CASCADE,
    fk_product_id INT FOREIGN KEY REFERENCES products(product_id) ON DELETE SET NULL,
    quantity INT NOT NULL DEFAULT 1
);

-- User Preferences Table
CREATE TABLE user_preferences (
    preference_id INT IDENTITY(1,1) PRIMARY KEY,
    fk_user_id INT FOREIGN KEY REFERENCES users(user_id) ON DELETE CASCADE,
    fk_store_id INT FOREIGN KEY REFERENCES stores(store_id) ON DELETE CASCADE,
    is_favorite BIT NOT NULL DEFAULT 0
);

-- Price Comparison Table
CREATE TABLE price_comparisons (
    price_id INT IDENTITY(1,1) PRIMARY KEY,
    price DECIMAL(12, 2) NOT NULL CHECK (price >= 0),
    effective_date DATE NOT NULL,
    expiration_date DATE,
    price_match_quantity INT,
    matched_with_store VARCHAR(100),
    fk_store_id INT FOREIGN KEY REFERENCES stores(store_id) ON DELETE CASCADE,
    fk_product_id INT FOREIGN KEY REFERENCES products(product_id) ON DELETE CASCADE
);
