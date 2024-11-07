-- Users Table
CREATE TABLE users (
    user_id INT IDENTITY(1,1) PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE CHECK (email LIKE '%@gmail.com' OR email LIKE '%@hotmail.com' OR email LIKE '%@yahoo.com' OR email LIKE '%@icloud.com'),
    password VARCHAR(255) NOT NULL,
    phone_number VARCHAR(15),
    role VARCHAR(10) NOT NULL CHECK (role IN ('admin', 'manager', 'customer'))
);

-- Store Table
CREATE TABLE store (
    store_id INT IDENTITY(1,1) PRIMARY KEY,
    store_name VARCHAR(100) NOT NULL,
    location VARCHAR(255),
    manager_id INT FOREIGN KEY REFERENCES users(user_id) ON DELETE SET NULL
);

-- Flyer Table (newly added)
CREATE TABLE flyer (
    flyer_id INT IDENTITY(1,1) PRIMARY KEY,
    flyer_start_date DATE NOT NULL,
    flyer_end_date DATE NOT NULL,
    store_id INT FOREIGN KEY REFERENCES store(store_id) ON DELETE CASCADE
);

-- Department Table
CREATE TABLE department (
    department_id INT IDENTITY(1,1) PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL,
    store_id INT FOREIGN KEY REFERENCES store(store_id) ON DELETE NO ACTION
);

-- Categories Table
CREATE TABLE categories (
    category_id INT IDENTITY(1,1) PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL,
    department_id INT FOREIGN KEY REFERENCES department(department_id) ON DELETE NO ACTION,
    store_id INT FOREIGN KEY REFERENCES store(store_id) ON DELETE NO ACTION
);

-- Products Table with foreign keys at the end
CREATE TABLE products (
    product_id INT IDENTITY(1,1) PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    status VARCHAR(10) NOT NULL CHECK (status IN ('in stock', 'out of stock')),
    ingredients TEXT,
    price_valid_from DATE,
    price_valid_to DATE,
    category_id INT FOREIGN KEY REFERENCES categories(category_id) ON DELETE SET NULL,
    department_id INT FOREIGN KEY REFERENCES department(department_id) ON DELETE SET NULL,
    store_id INT FOREIGN KEY REFERENCES store(store_id) ON DELETE SET NULL
);

-- Cart Table
CREATE TABLE cart (
    cart_id INT IDENTITY(1,1) PRIMARY KEY,
    user_id INT FOREIGN KEY REFERENCES users(user_id) ON DELETE CASCADE,
    product_id INT FOREIGN KEY REFERENCES products(product_id) ON DELETE SET NULL,
    quantity INT NOT NULL DEFAULT 1,
    added_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- User Preferences Table for Favorites
CREATE TABLE user_preferences (
    preference_id INT IDENTITY(1,1) PRIMARY KEY,
    user_id INT FOREIGN KEY REFERENCES users(user_id) ON DELETE CASCADE,
    store_id INT FOREIGN KEY REFERENCES store(store_id) ON DELETE CASCADE,
    is_favorite BIT NOT NULL DEFAULT 0
);

-- Price Comparison Table with foreign keys at the end
CREATE TABLE price_comparison (
    price_id INT IDENTITY(1,1) PRIMARY KEY,
    price DECIMAL(10, 2) NOT NULL,
    effective_date DATE NOT NULL,
    expiration_date DATE,
    price_match_quantity INT,
    matched_with_store VARCHAR(100),
    store_id INT FOREIGN KEY REFERENCES store(store_id) ON DELETE CASCADE,
    product_id INT FOREIGN KEY REFERENCES products(product_id) ON DELETE CASCADE
);
