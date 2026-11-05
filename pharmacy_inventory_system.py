"""
Smart Pharmacy Inventory & Sales Management System
Topic: for loop, range(), conditions, counters, and accumulators.

Processes medicine sales, updates stock, and calculates daily revenue.
"""


def get_positive_integer(prompt):
    """Read an integer greater than zero."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Please enter an integer greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_non_negative_integer(prompt):
    """Read an integer that is zero or greater."""
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            print("Value cannot be negative. Try again.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_non_negative_price(prompt):
    """Read a price that is zero or greater."""
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            print("Price cannot be negative. Try again.")
        except ValueError:
            print("Invalid input. Please enter a numeric price.")


def main():
    print("=" * 60)
    print("          SMART PHARMACY INVENTORY & SALES SYSTEM")
    print("=" * 60)

    medicine_count = get_positive_integer(
        "How many different medicines will be processed? "
    )

    total_revenue = 0.0       # Accumulator for all successful sales.
    restock_count = 0         # Counter for medicines needing restocking.
    successful_sales = 0      # Counter for medicines with completed sales.
    medicine_report = []

    # Process each medicine using a for loop and range().
    for medicine_number in range(1, medicine_count + 1):
        print(f"\n--- Medicine {medicine_number} of {medicine_count} ---")

        # Ensure that the medicine name is not empty.
        while True:
            medicine_name = input("Enter medicine name: ").strip()
            if medicine_name:
                break
            print("Medicine name cannot be empty.")

        stock = get_non_negative_integer("Enter available stock (units): ")
        unit_price = get_non_negative_price("Enter price per unit (Rs.): ")
        quantity_sold = get_non_negative_integer("Enter quantity to sell: ")

        if quantity_sold > stock:
            print(
                f"Sale rejected: only {stock} unit(s) of "
                f"{medicine_name} are available."
            )
            print("No stock or revenue has been changed.")
            remaining_stock = stock
            sales_amount = 0.0
            sale_status = "Rejected - insufficient stock"
        else:
            # Calculate the sale and update inventory.
            sales_amount = quantity_sold * unit_price
            remaining_stock = stock - quantity_sold
            total_revenue += sales_amount
            successful_sales += 1
            sale_status = "Successful"

            print(f"Sale successful for {medicine_name}.")
            print(f"Sales amount: Rs. {sales_amount:,.2f}")
            print(f"Remaining stock: {remaining_stock} unit(s)")

        # A medicine is marked for restocking when its remaining stock is below 10.
        if remaining_stock < 10:
            restock_count += 1
            print(
                f"LOW-STOCK WARNING: {medicine_name} has only "
                f"{remaining_stock} unit(s) remaining."
            )

        medicine_report.append({
            "name": medicine_name,
            "status": sale_status,
            "quantity_sold": quantity_sold if sale_status == "Successful" else 0,
            "sales_amount": sales_amount,
            "remaining_stock": remaining_stock,
        })

    # Display the final daily sales and inventory report.
    print("\n" + "=" * 60)
    print("                  DAILY PHARMACY REPORT")
    print("=" * 60)
    print(f"Total medicines processed : {medicine_count}")
    print(f"Successful medicine sales : {successful_sales}")
    print(f"Medicines needing restock : {restock_count}")
    print(f"Total pharmacy revenue    : Rs. {total_revenue:,.2f}")
    print("-" * 60)
    print("Medicine-wise Summary:")

    for item in medicine_report:
        print(f"\nMedicine       : {item['name']}")
        print(f"Sale status    : {item['status']}")
        print(f"Quantity sold  : {item['quantity_sold']}")
        print(f"Sales amount   : Rs. {item['sales_amount']:,.2f}")
        print(f"Remaining stock: {item['remaining_stock']}")

    print("=" * 60)


if __name__ == "__main__":
    main()
