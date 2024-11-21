import pyodbc
from decimal import Decimal

def connect_db():
    try:
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=DP\DSQL;'
            'DATABASE=SMART_GROCERY_ASSISTANT;'
            'Trusted_Connection=yes;'
        )
        return conn
    except pyodbc.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def fetch_products():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT product_id, product_name, price FROM products")
    products = cursor.fetchall()
    conn.close()
    return products

def display_products():
    products = fetch_products()
    print("Available Products List:")
    if products:
        print(f"{'Product ID':<12}{'Product Name':<50}{'Product Price':<12}")
        print("-" * 94)
        for row in products:
            print(f"{row.product_id:<12}{row.product_name:<50}{row.price:<12}")

def get_product_by_id(product_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT product_name, price FROM products WHERE product_id = ?", (product_id,))
    product = cursor.fetchone()
    conn.close()
    return product if product else None

class Budget:
    def __init__(self, amount):
        self.amount = amount
        self.total_spent = 0

    def add_item(self, item_price):
        return self.total_spent + item_price <= self.amount
    
    def add_to_total(self, item_price):
        if self.add_item(item_price):
            self.total_spent += item_price
            return True
        else:
            return False
    
    def remaining_budget(self):
        return Decimal(self.amount) - self.total_spent

class Item:
    def __init__(self, name, price, qunatity=1):
        self.name = name
        self.price = price
        self.quantity = qunatity
        self.total_price = price * qunatity

class Cart:
    def __init__(self, budget):
        self.budget = budget
        self.items = []

    def add_item_by_id(self, product_id, product_qty):
        product = get_product_by_id(product_id)
        if product:
            item_name, item_price = product
            total_price = item_price * product_qty
            item = Item(item_name, item_price, product_qty)
            if self.budget.add_to_total(total_price):
                self.items.append(item)
                print(f"Added {product_qty} x {item.name} to the cart. Remaining budget: ${self.budget.remaining_budget():.2f}")
            else:
                print(f"Cannot add {product_qty} x {item.name}. Budget exceeded.")
        else:
            print("Invalid product ID.")

    def show_cart(self):
        print("Current Cart:")
        for item in self.items:
            print(f"- {item.quantity} x {item.name}: ${item.total_price:.2f}")
        print(f"Total spent: ${self.budget.total_spent:.2f}")
        print(f"Remaining budget: ${self.budget.remaining_budget():.2f}")

budget_amount = float(input("Enter your budget: "))
budget = Budget(budget_amount)
cart = Cart(budget)

while True:
    display_products()
    product_id = input("Enter product ID to add to cart (or 'done' to finish): ")
    if product_id.lower() == 'done':
        break
    product_qty = int(input("Enter the quantity: "))
    cart.add_item_by_id(int(product_id), product_qty)

cart.show_cart()