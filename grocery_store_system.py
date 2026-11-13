"""Smart Grocery Store Management System (lists and dictionaries)."""

import math

LOW_STOCK_LIMIT = 5  # products with stock below this are reported as low stock
LINE = "=" * 36


# ---------- input helpers ----------

def get_menu_choice():
    # Ask until the user enters a number from 1 to 8.
    while True:
        entry = input("Enter your choice: ").strip()
        if entry in ("1", "2", "3", "4", "5", "6", "7", "8"):
            return int(entry)
        print("  Invalid choice. Please enter a number from 1 to 8.")


def get_valid_text(prompt):
    # Ask until the text is not empty after trimming spaces.
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("  This field cannot be empty.")


def get_valid_int(prompt, minimum):
    # Ask until the user enters a whole number that is at least 'minimum'.
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("  Invalid input. Please enter a whole number.")
            continue
        if value >= minimum:
            return value
        print(f"  Value must be at least {minimum}.")


def get_valid_price(prompt):
    # Ask until the price is a number greater than zero (rejects nan and inf).
    while True:
        try:
            price = float(input(prompt))
        except ValueError:
            print("  Invalid input. Please enter a number.")
            continue
        if not math.isfinite(price):
            print("  Invalid input. Please enter a number.")
        elif price <= 0:
            print("  Price must be greater than zero.")
        else:
            return price


# ---------- product helpers ----------

def find_product_by_id(products, product_id):
    # Return the product dictionary with this ID, or None if it does not exist.
    for product in products:
        if product["id"] == product_id:
            return product
    return None


def find_products_by_name(products, search_text):
    # Return every product whose name contains the text (ignoring capitals).
    matches = []
    for product in products:
        if search_text.lower() in product["name"].lower():
            matches.append(product)
    return matches


def short_text(text, width):
    # Shorten long text with '...' so table columns stay aligned.
    if len(text) > width:
        return text[:width - 3] + "..."
    return text


def print_product_details(product):
    # Print the complete details of one product.
    print(f"  Product ID : {product['id']}")
    print(f"  Name       : {product['name']}")
    print(f"  Category   : {product['category']}")
    print(f"  Price      : Rs. {product['price']:,.2f}")
    print(f"  Stock      : {product['stock']} units")


# ---------- menu operations ----------

def show_menu():
    # Print the main menu.
    print(f"\n{LINE}")
    print("SMART GROCERY STORE SYSTEM")
    print(LINE)
    print("\n1. Add New Product")
    print("2. View All Products")
    print("3. Search Product")
    print("4. Update Product Stock")
    print("5. Process Customer Sale")
    print("6. View Sales Records")
    print("7. Generate Store Report")
    print("8. Exit\n")


def add_product(products):
    # Read a new product, block duplicate IDs, and append it as a dictionary.
    print("\n--- Add New Product ---")
    while True:
        product_id = get_valid_int("Product ID: ", 1)
        existing = find_product_by_id(products, product_id)
        if existing is None:
            break
        print(f"  Product ID {product_id} already exists ({existing['name']}). Please use a different ID.")

    name = get_valid_text("Product name: ")
    category = get_valid_text("Category: ").title()
    price = get_valid_price("Price (Rs.): ")
    stock = get_valid_int("Available stock: ", 0)

    product = {"id": product_id, "name": name, "category": category,
               "price": price, "stock": stock}
    products.append(product)
    print(f"  Product added: {name} (ID {product_id}).")


def display_products(products):
    # Show every product in an aligned table; flag low-stock items.
    print("\n--- All Products ---")
    if len(products) == 0:
        print("  No products in the store yet.")
        return
    print(f"{'ID':<7}{'Name':<22}{'Category':<16}{'Price (Rs.)':>12}{'Stock':>8}")
    print("-" * 65)
    for product in products:
        flag = "  LOW" if product["stock"] < LOW_STOCK_LIMIT else ""
        print(f"{product['id']:<7}{short_text(product['name'], 20):<22}"
              f"{short_text(product['category'], 14):<16}"
              f"{product['price']:>12,.2f}{product['stock']:>8}{flag}")
    print("-" * 65)
    print(f"{len(products)} product(s) listed.")


def search_product(products):
    # Search by ID (digits) or by name (text) and show complete details.
    print("\n--- Search Product ---")
    text = input("Enter product ID or name: ").strip()
    if not text:
        print("  Search text cannot be empty.")
        return

    if text.isdigit():
        product = find_product_by_id(products, int(text))
        matches = [product] if product is not None else []
        not_found = f"  No product found with ID {int(text)}."
    else:
        matches = find_products_by_name(products, text)
        not_found = f"  No product found with name '{text}'."

    if len(matches) == 0:
        print(not_found)
        return
    print(f"  Found {len(matches)} product(s):")
    for product in matches:
        print()
        print_product_details(product)


def update_stock(products):
    # Add stock to, or set a new quantity for, one product.
    print("\n--- Update Product Stock ---")
    product_id = get_valid_int("Enter product ID: ", 1)
    product = find_product_by_id(products, product_id)
    if product is None:
        print(f"  No product found with ID {product_id}.")
        return

    print(f"  {product['name']} currently has {product['stock']} units.")
    print("  1. Add stock to the current quantity")
    print("  2. Set a new quantity")
    while True:
        option = input("Choose an option (1 or 2): ").strip()
        if option in ("1", "2"):
            break
        print("  Invalid option. Please enter 1 or 2.")

    old_stock = product["stock"]
    if option == "1":
        amount = get_valid_int("Units to add: ", 1)
        product["stock"] = old_stock + amount
    else:
        product["stock"] = get_valid_int("New quantity: ", 0)
    print(f"  Updated stock for {product['name']}: {old_stock} -> {product['stock']} units")


def process_sale(products, sales):
    # Sell units of a product, update its stock, and record the sale.
    print("\n--- Process Customer Sale ---")
    product_id = get_valid_int("Enter product ID: ", 1)
    product = find_product_by_id(products, product_id)
    if product is None:
        print(f"  No product found with ID {product_id}. Sale cancelled.")
        return
    if product["stock"] == 0:
        print(f"  {product['name']} is out of stock. Sale cancelled.")
        return

    quantity = get_valid_int("Quantity to buy: ", 1)
    if quantity > product["stock"]:
        print(f"  Not enough stock! Only {product['stock']} units of {product['name']} available. Sale cancelled.")
        return

    total_price = product["price"] * quantity
    product["stock"] -= quantity  # deduct the purchased quantity

    sale = {"product_id": product["id"], "product_name": product["name"],
            "quantity_sold": quantity, "total_amount": total_price}
    sales.append(sale)

    print("\n  Purchase Summary")
    print(f"  Product         : {product['name']} (ID {product['id']})")
    print(f"  Quantity        : {quantity}")
    print(f"  Unit price      : Rs. {product['price']:,.2f}")
    print(f"  Total price     : Rs. {total_price:,.2f}")
    print(f"  Remaining stock : {product['stock']} units")


def view_sales(sales):
    # Show every completed sale and the revenue so far.
    print("\n--- Sales Records ---")
    if len(sales) == 0:
        print("  No sales recorded yet.")
        return
    print(f"{'No.':<5}{'Product ID':<12}{'Product Name':<22}{'Qty Sold':>9}{'Total (Rs.)':>14}")
    print("-" * 62)
    total_revenue = 0.0
    for number, sale in enumerate(sales, start=1):
        print(f"{number:<5}{sale['product_id']:<12}{short_text(sale['product_name'], 20):<22}"
              f"{sale['quantity_sold']:>9}{sale['total_amount']:>14,.2f}")
        total_revenue += sale["total_amount"]
    print("-" * 62)
    print(f"{len(sales)} sale(s). Total revenue: Rs. {total_revenue:,.2f}")


def generate_report(products, sales):
    # Print the final store report from the products and sales lists.
    print(f"\n{LINE}")
    print("STORE REPORT")
    print(LINE)
    if len(products) == 0:
        print("No products in the store yet.")
        return

    total_stock = 0
    for product in products:
        total_stock += product["stock"]
    revenue = 0.0
    for sale in sales:
        revenue += sale["total_amount"]

    print(f"Total products          : {len(products)}")
    print(f"Total available stock   : {total_stock} units")
    print(f"Total sales transactions: {len(sales)}")
    print(f"Total revenue           : Rs. {revenue:,.2f}")

    print(f"\nProducts with stock below {LOW_STOCK_LIMIT} units:")
    low_found = False
    for product in products:
        if product["stock"] < LOW_STOCK_LIMIT:
            print(f"  - {product['name']} (ID {product['id']}): {product['stock']} units")
            low_found = True
    if not low_found:
        print("  None")

    highest = max(product["price"] for product in products)
    lowest = min(product["price"] for product in products)
    highest_names = [p["name"] for p in products if p["price"] == highest]
    lowest_names = [p["name"] for p in products if p["price"] == lowest]
    print(f"\nHighest priced product  : {', '.join(highest_names)} (Rs. {highest:,.2f})")
    print(f"Lowest priced product   : {', '.join(lowest_names)} (Rs. {lowest:,.2f})")


def show_goodbye(sales):
    # Print a short goodbye message when the user exits.
    print(f"\n{LINE}")
    print("Thank you for using the Smart Grocery Store System!")
    print(f"Sales completed this session: {len(sales)}")
    print(LINE)


def main():
    # Starting stock so the store can be used straight away.
    products = [
        {"id": 101, "name": "Milk", "category": "Dairy", "price": 250, "stock": 20},
        {"id": 102, "name": "Eggs", "category": "Dairy", "price": 320, "stock": 12},
        {"id": 103, "name": "Rice", "category": "Grains", "price": 1200, "stock": 8},
        {"id": 104, "name": "Apples", "category": "Fruits", "price": 300, "stock": 4},
        {"id": 105, "name": "Sugar", "category": "Pantry", "price": 180, "stock": 3},
        {"id": 106, "name": "Bread", "category": "Bakery", "price": 80, "stock": 15},
    ]
    sales = []  # each completed sale is stored here as a dictionary

    while True:
        show_menu()
        choice = get_menu_choice()

        if choice == 1:
            add_product(products)
        elif choice == 2:
            display_products(products)
        elif choice == 3:
            search_product(products)
        elif choice == 4:
            update_stock(products)
        elif choice == 5:
            process_sale(products, sales)
        elif choice == 6:
            view_sales(sales)
        elif choice == 7:
            generate_report(products, sales)
        else:  # choice == 8
            show_goodbye(sales)
            break


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        # Ctrl+C or closed input: exit politely instead of showing a traceback.
        print("\nProgram interrupted. Goodbye!")
