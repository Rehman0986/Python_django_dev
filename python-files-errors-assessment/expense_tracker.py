"""Task 1: Expense Tracker That Remembers (saves expenses to expenses.csv)."""

import csv
import math
from datetime import date, datetime

EXPENSE_FILE = "expenses.csv"
COLUMNS = ["date", "item", "category", "amount"]  # CSV header
LINE = "=" * 40


def load_expenses():
    # Read expenses.csv into a list of dictionaries; start empty if it is missing.
    expenses = []
    skipped = 0
    try:
        with open(EXPENSE_FILE, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    expense = {
                        "date": row["date"].strip(),
                        "item": row["item"].strip(),
                        "category": row["category"].strip().title(),
                        "amount": float(row["amount"]),
                    }
                    # A usable row has text in every field and a positive amount.
                    if not (expense["date"] and expense["item"] and expense["category"]):
                        raise ValueError("empty field")
                    if not math.isfinite(expense["amount"]) or expense["amount"] <= 0:
                        raise ValueError("bad amount")
                    expenses.append(expense)
                except (ValueError, TypeError, KeyError, AttributeError):
                    skipped += 1  # damaged row: count it and carry on
    except FileNotFoundError:
        # First run: there is no file yet, so start with an empty list.
        print(f"No {EXPENSE_FILE} found. Starting with an empty list.")
        return expenses
    except (OSError, UnicodeDecodeError) as error:
        print(f"Could not read {EXPENSE_FILE} ({error}). Starting with an empty list.")
        return expenses

    print(f"Loaded {len(expenses)} expense(s) from {EXPENSE_FILE}.")
    if skipped > 0:
        print(f"  Warning: skipped {skipped} invalid row(s) in {EXPENSE_FILE}.")
    return expenses


def save_expenses(expenses):
    # Write every expense to expenses.csv (header + one row each). Returns True if saved.
    try:
        with open(EXPENSE_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=COLUMNS)
            writer.writeheader()
            for expense in expenses:
                writer.writerow({"date": expense["date"], "item": expense["item"],
                                 "category": expense["category"],
                                 "amount": f"{expense['amount']:.2f}"})
        return True
    except OSError as error:
        print(f"  Error: could not save {EXPENSE_FILE} ({error}).")
        return False


def unique_categories(expenses):
    # A set comprehension keeps each category only once.
    return {expense["category"] for expense in expenses}


def get_valid_date():
    # Ask for a date as YYYY-MM-DD; pressing Enter uses today's date.
    while True:
        text = input("Date (YYYY-MM-DD, Enter for today): ").strip()
        if text == "":
            return date.today().isoformat()
        try:
            return datetime.strptime(text, "%Y-%m-%d").date().isoformat()
        except ValueError:
            print("  Invalid date. Use the format YYYY-MM-DD (for example 2026-11-14).")


def get_valid_text(label):
    # Ask until the text is not empty.
    while True:
        text = input(f"{label}: ").strip()
        if text:
            return text
        print(f"  {label} cannot be empty.")


def get_valid_amount():
    # Ask until the amount is a positive number; float() raises ValueError for text.
    while True:
        try:
            amount = float(input("Amount (Rs.): "))
        except ValueError:
            print("  Invalid amount. Please enter a number such as 250 or 99.50.")
            continue
        if not math.isfinite(amount):
            print("  Invalid amount. Please enter a number such as 250 or 99.50.")
        elif amount <= 0:
            print("  Amount must be greater than zero.")
        else:
            return amount


def add_expense(expenses):
    # Read one expense, add it to the list and save the file straight away.
    print("\n--- Add Expense ---")
    expense_date = get_valid_date()
    item = get_valid_text("Item")
    known = unique_categories(expenses)
    if known:
        print(f"  Existing categories: {', '.join(sorted(known))}")
    category = get_valid_text("Category").title()
    amount = get_valid_amount()

    expenses.append({"date": expense_date, "item": item, "category": category, "amount": amount})
    if save_expenses(expenses):
        print(f"  Saved: {item} ({category}) - Rs. {amount:,.2f}")
    else:
        print("  The expense is kept for this session only.")


def short_text(text, width):
    # Shorten long text with '...' so table columns stay aligned.
    return text if len(text) <= width else text[:width - 3] + "..."


def show_all(expenses):
    # Show every expense in a numbered table, then the grand total.
    print("\n--- All Expenses ---")
    if not expenses:
        print("  No expenses recorded yet.")
        return
    print(f"{'No.':<5}{'Date':<12}{'Item':<22}{'Category':<16}{'Amount (Rs.)':>12}")
    print("-" * 67)
    for number, expense in enumerate(expenses, start=1):
        print(f"{number:<5}{expense['date']:<12}{short_text(expense['item'], 20):<22}"
              f"{short_text(expense['category'], 14):<16}{expense['amount']:>12,.2f}")
    print("-" * 67)
    total = sum(expense["amount"] for expense in expenses)
    print(f"{len(expenses)} expense(s). Total: Rs. {total:,.2f}")


def show_totals_by_category(expenses):
    # Show the unique categories (a set) and the total spent in each.
    print("\n--- Total by Category ---")
    if not expenses:
        print("  No expenses recorded yet.")
        return
    categories = unique_categories(expenses)
    print(f"Unique categories ({len(categories)}): {', '.join(sorted(categories))}")
    print(f"\n{'Category':<18}{'Count':>7}{'Total (Rs.)':>16}")
    print("-" * 41)
    for category in sorted(categories):
        amounts = [e["amount"] for e in expenses if e["category"] == category]
        print(f"{category:<18}{len(amounts):>7}{sum(amounts):>16,.2f}")
    print("-" * 41)
    print(f"{'Grand total':<25}{sum(e['amount'] for e in expenses):>16,.2f}")


def show_menu():
    # Print the main menu.
    print(f"\n{LINE}")
    print(f"{'EXPENSE TRACKER':^40}")
    print(LINE)
    print("1. Add expense")
    print("2. Show all expenses")
    print("3. Total by category")
    print("4. Quit")
    print("-" * 40)


def get_menu_choice():
    # Ask until the user enters 1, 2, 3 or 4.
    while True:
        choice = input("Enter your choice (1-4): ").strip()
        if choice in ("1", "2", "3", "4"):
            return int(choice)
        print("  Invalid choice. Please enter a number from 1 to 4.")


def main():
    expenses = load_expenses()  # remembers what was saved in earlier runs

    while True:
        show_menu()
        choice = get_menu_choice()
        if choice == 1:
            add_expense(expenses)
        elif choice == 2:
            show_all(expenses)
        elif choice == 3:
            show_totals_by_category(expenses)
        else:
            if expenses:
                print(f"\nGoodbye! {len(expenses)} expense(s) are saved in {EXPENSE_FILE}.")
            else:
                print("\nGoodbye! No expenses were recorded.")
            break


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        # Ctrl+C: expenses were already saved after each add, so nothing is lost.
        print("\nProgram interrupted. Goodbye!")
