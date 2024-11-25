import pyodbc

def connect_db():
    try:
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=DESKTOP-06CECOC\\ZSQL;'
            'DATABASE=smart_grocery_assistant;'
            'Trusted_Connection=yes;'
        )
        return conn
    except pyodbc.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def fetch_products():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT product_id, product_name, price, stock_quantity,status FROM products")
    products = cursor.fetchall()
    conn.close()
    return products

def display_products():
    products = fetch_products()
    print("Available Products List:")
    if products:
        print(f"{'Product ID':<12}{'Product Name':<50}{'Price':<12}{'Stock Quantity':<17}{'Product Stock':<12}")
        print("-" * 94)
        for row in products:
            print(f"{row.product_id:<12}{row.product_name:<50}{row.price:<12}{row.stock_quantity:<17}{row.status:<12}")


display_products()
