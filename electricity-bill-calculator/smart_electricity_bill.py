# Program 2: Smart Electricity Bill Calculator
# Topic: for loop, range(), accumulators, and conditional statements inside loops.

# Real-World Scenario
# Imagine an electricity company that wants to calculate the monthly electricity bills of multiple households.
# Instead of writing the same code repeatedly for every household, the company wants a program that:
# 1. Asks how many households need their bills calculated.
# 2. Takes the electricity units consumed by each household.
# 3. Calculates the bill using the following rates:
#    - First 100 units: Rs. 10 per unit.
#    - Next 100 units (101–200): Rs. 15 per unit.
#    - Units above 200: Rs. 20 per unit.
# 4. Calculates the total bill for every household.
# 5. Displays the combined electricity revenue collected from all households.
# Important: These rates are fictional and intended for programming practice, not actual electricity tariffs.

# Smart Electricity Bill Calculator

print("===== ELECTRICITY BILL SYSTEM =====")

households = int(input("Enter the number of households: "))

total_revenue = 0

for household in range(1, households + 1):

    print(f"\n--- Household {household} ---")

    units = int(input("Enter electricity units consumed: "))

    if units < 0:
        print("Invalid units! Please enter a non-negative value.")
        continue

    if units <= 100:
        bill = units * 10

    elif units <= 200:
        bill = (100 * 10) + ((units - 100) * 15)

    else:
        bill = (100 * 10) + (100 * 15) + ((units - 200) * 20)

    print(f"Units Consumed: {units}")
    print(f"Electricity Bill: Rs. {bill}")

    total_revenue += bill

print("\n===== MONTHLY REVENUE REPORT =====")
print(f"Households Processed: {households}")
print(f"Total Revenue: Rs. {total_revenue}")