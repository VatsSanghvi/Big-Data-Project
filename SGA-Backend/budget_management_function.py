class budget:
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
        return self.amount - self.total_spent
    

class item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class cart:
    def __init__(self, budget):
        self.budget = budget
        self.cart_items = []

    def add_item(self, item):
        if self.budget.add_to_total(item.price):
            self.cart_items.append(item)
            print(f"Added {item.name} to the cart. Remaining budget: ${self.budget.remaining_budget():.2f}")
        else:
            print(f"Cannot add {item.name}. Budget exceeded by ${item.price - self.budget.remaining_budget():.2f}.")
        
    def show_cart(self):
        print("Current Cart:")
        for item in self.cart_items:
            print(f"- {item.name}: ${item.price}")
        print(f"Total spent: ${self.budget.total_spent:.2f}")
        print(f"Remaining budget: ${self.budget.remaining_budget():.2f}")

budget_amount = float(input("Enter your budget: "))
budget = budget(budget_amount)
cart = cart(budget)

while True:
    item_name = input("Enter item name (or 'done' to finish): ")
    if item_name.lower() == 'done':
        break
    item_price = float(input(f"Enter price for {item_name}: "))
    item = item(item_name, item_price)
    cart.add_item(item)

cart.show_cart()