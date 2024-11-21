import pyodbc

# Connection to the database
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

#####################################################################################################
# Function to Search for the product
def search_products(search_term):
    conn = connect_db()
    cursor = conn.cursor()
    query = "select product_id, product_name, price from products where product_name like ?"
    cursor.execute(query, ('%' + search_term + '%',))
    results = cursor.fetchall()
    conn.close()
    return results

## Displaying the searched product
def display_search_results(search_term):
    results = search_products(search_term)
    if results:
        print(f"Search Results for '{search_term}':")
        print(f"{'Product ID':<12}{'Product Name':<50}{'Product Price':<12}")
        print("-" * 94)
        for row in results:
            print(f"{row.product_id:<12}{row.product_name:<50}{row.price:<12}")
    else:
        print(f"No products found matching '{search_term}'.")

#####################################################################################################
# Function to Searching by Category.
def search_by_category(category):
    conn = connect_db()
    cursor = conn.cursor()
    query = "select p.product_id, p.product_name, p.price from products p join categories c on p.category_id = c.category_id where c.category_name = ?"
    cursor.execute(query, (category,))
    results = cursor.fetchall()
    conn.close()
    return results

# Displaying the products by searched category
def display_search_by_category(category):
    results = search_by_category(category)
    if results:
        print(f"Products in category '{category}':")
        print(f"{'Product ID':<12}{'Product Name':<50}{'Product Price':<12}")
        print("-" * 94)
        for row in results:
            print(f"{row.product_id:<12}{row.product_name:<50}{row.price:<12}")
    else:
        print(f"No products found in category '{category}'.")

#####################################################################################################
# Function for sorting and Filtering by Product Name and Price
def search_with_sort(sort_by, order='ASC'):
    conn = connect_db()
    cursor = conn.cursor()
    query = f"select product_id, product_name, price from products order by {sort_by} {order}"
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

## Displaying the sorted or fitered results
def display_sorted_results(sort_by, order):
    results = search_with_sort(sort_by, order)
    print(f"Products sorted by {sort_by} ({order}):")
    if results:
        print(f"{'Product ID':<12}{'Product Name':<50}{'Product Price':<12}")
        print("-" * 94)
        for product in results:
            print(f"{product.product_id:<12}{product.product_name:<50}{product.price:<12}")

#####################################################################################################
## Function to search for a product using the grocery store name
def search_by_store(store_name):
    conn = connect_db()
    cursor = conn.cursor()
    query = "Select p.product_id, p.product_name, p.price, p.status from products p join store s on p.store_id = s.store_id where s.store_name = ?"
    cursor.execute(query, (store_name,))
    results = cursor.fetchall()
    conn.close()
    return results

# Displaying the product by store name
def display_search_by_store(store_name):
    results = search_by_store(store_name)
    if results:
        print(f"Products available in store: '{store_name}':")
        print(f"{'Product ID':<12}{'Product Name':<50}{'Product Price':<12}")
        print("-" * 94)
        for row in results:
            print(f"{row.product_id:<12}{row.product_name:<50}{row.price:<12}")
    else:
        print(f"No products found in store '{store_name}'.")

#####################################################################################################
# Function for trending searches of Products done by user
def get_trending_searches():
    conn = connect_db()
    cursor = conn.cursor()
    query = "select search_term, count(search_term) as search_count from search_logs group by search_term order by search_count desc"
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

# Displaying the trending searches
def display_trending_searches():
    trending = get_trending_searches()
    if trending:
        print("Trending Searches:")
        print("-" * 94)
        for search in trending:
            print(f"{search.search_term}")

#####################################################################################################
# Function for searching the entire flyer
def search_flyer_by_store(store_name):
    conn = connect_db()
    cursor = conn.cursor()
    query = "select flyer_url from flyer where store_name = ?"
    cursor.execute(query, (store_name,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

# Displaying the flyer
def display_flyer(store_name):
    flyer_url = search_flyer_by_store(store_name)
    if flyer_url:
        print(f"Flyer for store '{store_name}': {flyer_url}")
    else:
        print(f"No flyer found for store '{store_name}'.")

#####################################################################################################
## Testing the functions
search_term = input("Enter product name or keyword to search: ")
display_search_results(search_term)

category = input("Enter category: ")
display_search_by_category(category)

sort_by = input("Sort by 'product_name' or 'price': ")
order = input("Order 'ASC' or 'DESC': ")
display_sorted_results(sort_by, order)

store_name = input("Enter grocery store name: ")
display_search_by_store(store_name)

display_trending_searches()

store_name = input("Enter grocery store name to view flyer: ")
display_flyer(store_name)

