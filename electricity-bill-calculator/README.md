# Python Loops — Smart Electricity Bill Calculator

A beginner-friendly Python program demonstrating `for` loops, `range()`, accumulators, and conditional statements through a real-world electricity billing scenario.

## Repository Information

**Repository Name:** `python-loops-electricity-bill-calculator`

**Description:** Beginner-friendly Python program demonstrating for loops, range(), accumulators, conditional statements, and tiered electricity bill calculations for multiple households.

## 1. Real-World Scenario

An electricity company needs to calculate monthly electricity bills for multiple households.

Instead of writing separate code for every household, the program uses a `for` loop to process each household, calculate its electricity bill, and maintain a running total of the revenue collected.

**Important:** The electricity rates used in this program are fictional and intended for programming practice only. They do not represent actual electricity tariffs.

## 2. Electricity Billing Rules

The program calculates electricity bills using the following rates:

| Electricity Consumption | Rate |
|---|---:|
| First 100 units | Rs. 10 per unit |
| Units 101–200 | Rs. 15 per unit |
| Units above 200 | Rs. 20 per unit |

The rates are applied progressively. Each rate applies only to the units within its corresponding tier.

### Example Calculations

**Example 1: 80 Units**

- Electricity consumption: 80 units
- Calculation: 80 × 10
- Total bill: Rs. 800

**Example 2: 150 Units**

- First 100 units: 100 × 10 = Rs. 1,000
- Remaining 50 units: 50 × 15 = Rs. 750
- Total bill: Rs. 1,750

**Example 3: 250 Units**

- First 100 units: 100 × 10 = Rs. 1,000
- Next 100 units: 100 × 15 = Rs. 1,500
- Remaining 50 units: 50 × 20 = Rs. 1,000
- Total bill: Rs. 3,500

## 3. What We Covered in Class

### A. For Loop

The `for` loop repeats the billing process for each household.

```python
for household in range(1, households + 1):
    print(f"Household {household}")
```

This avoids repeating the same code manually for every household.

### B. Range Function

The expression `range(1, households + 1)` generates household numbers starting from 1 and ending at the number entered by the user.

For example, if the user enters `3`, the loop processes households 1, 2, and 3.

### C. Conditional Statements

The program uses `if`, `elif`, and `else` to determine which billing formula should be applied.

- `if`: Checks whether consumption is 100 units or less.
- `elif`: Checks whether consumption is 200 units or less when the first condition is false.
- `else`: Calculates the bill for consumption above 200 units.

### D. Accumulator

The accumulator keeps track of the combined revenue collected from all valid household bills.

```python
total_revenue = 0
total_revenue += bill
```

The accumulator starts at zero and increases whenever a valid household bill is calculated.

### E. Continue Statement

The `continue` statement skips the remaining calculations for the current household when negative electricity units are entered.

```python
if units < 0:
    print("Invalid units! Please enter a non-negative value.")
    continue
```

The loop then proceeds to the next household.

## 4. Program Features

The program:

1. Accepts the number of households.
2. Processes each household using a `for` loop.
3. Accepts electricity consumption in units.
4. Rejects negative unit values.
5. Calculates bills using conditional statements.
6. Displays each household's electricity consumption and bill.
7. Calculates the total revenue from valid bills.
8. Displays a final monthly revenue report.

## 5. How to Run the Program

### Prerequisites

- Python 3 installed on your computer.
- A code editor such as Visual Studio Code or PyCharm.

### Execution

1. Save the program as `smart_electricity_bill.py`.
2. Open a terminal in the folder containing the file.
3. Run the following command:

```bash
python smart_electricity_bill.py
```

On some systems, you may need to use `python3` instead of `python`.

## 6. Example Output

For three households consuming 80, 150, and 250 units respectively, the program produces the following billing results:

```text
===== ELECTRICITY BILL SYSTEM =====
Enter the number of households: 3

--- Household 1 ---
Enter electricity units consumed: 80
Units Consumed: 80
Electricity Bill: Rs. 800

--- Household 2 ---
Enter electricity units consumed: 150
Units Consumed: 150
Electricity Bill: Rs. 1750

--- Household 3 ---
Enter electricity units consumed: 250
Units Consumed: 250
Electricity Bill: Rs. 3500

===== MONTHLY REVENUE REPORT =====
Households Processed: 3
Total Revenue: Rs. 6050
```

## 7. Basic UI/UX Considerations

Although this is a console-based application rather than a graphical interface, it incorporates basic usability principles:

- **Clear headings:** Identify the electricity billing system and final report.
- **Descriptive prompts:** Tell users what information they need to enter.
- **Separate household sections:** Make individual calculations easier to follow.
- **Readable results:** Display electricity consumption and bills separately.
- **Error feedback:** Inform users when negative unit values are entered.
- **Summary report:** Display the combined revenue after processing all households.

## 8. Student Practice Challenges

Extend the program by implementing the following features:

1. Validate that the number of households is greater than zero.
2. Handle non-numeric input using `try` and `except`.
3. Count the number of households whose bills were successfully calculated.
4. Display the highest individual electricity bill.
5. Calculate the average bill for households with valid unit entries.
6. Display the household number with the highest bill.
7. Explain why `total_revenue` must be initialized before the loop.
8. Explain the difference between `continue` and `break`.

## 9. Learning Outcomes

After completing this practical exercise, students should be able to:

- Use `for` loops to automate repetitive tasks.
- Apply `range()` to control loop iterations.
- Implement decision-making with conditional statements.
- Use accumulators to calculate running totals.
- Apply `continue` to skip invalid entries.
- Translate real-world billing rules into Python logic.
- Generate a summary report from multiple calculations.

## Suggested Git Commit

```text
Add electricity bill calculator using Python loops
```