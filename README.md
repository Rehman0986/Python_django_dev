# Python Conditions and Loops Assessment

## Project Overview

This repository contains two independent, menu-free Python command-line applications developed for a programming assessment. The programs demonstrate conditional statements, loops, input validation, arithmetic operations, counters, and accumulators.

## Project Structure

```text
python-conditions-loops-assessment/
├── student_scholarship_system.py
├── pharmacy_inventory_system.py
└── README.md
```

## Application 1: Student Scholarship Eligibility System

**File:** `student_scholarship_system.py`

This application collects a student's name, academic marks, attendance percentage, and monthly family income. It validates the entries and checks the scholarship requirements.

### Eligibility rules

| Requirement | Condition |
|---|---|
| Academic marks | At least 80% |
| Attendance | At least 85% |
| Monthly family income | Rs. 50,000 or less |
| Full Scholarship | All requirements met and marks are 90% or above |
| Partial Scholarship | All requirements met and marks are from 80% to below 90% |

If one or more requirements are not met, the report lists each reason for ineligibility.

### Python concepts used

- `input()` and `print()`
- Variables and meaningful variable names
- `if`, `elif`, and `else`
- Comparison and logical conditions
- `while` loops for input validation
- `try` / `except` for invalid numeric input
- Lists for collecting ineligibility reasons
- Formatted output using f-strings

### Sample execution

```text
Enter student's name: Ali
Enter academic marks (0-100): 92
Enter attendance percentage (0-100): 90
Enter monthly family income (Rs.): 45000

SCHOLARSHIP EVALUATION REPORT
Student Name          : Ali
Academic Marks        : 92.00%
Attendance            : 90.00%
Monthly Family Income : Rs. 45,000.00
Eligibility Status    : ELIGIBLE
Scholarship Decision  : Full Scholarship

All scholarship eligibility requirements have been met.
```

Another test: marks `78`, attendance `80`, and income `60000` should result in `NOT ELIGIBLE` with all three reasons displayed.

## Application 2: Smart Pharmacy Inventory & Sales Management System

**File:** `pharmacy_inventory_system.py`

This application processes a user-defined number of medicines. For each medicine, it collects the name, available stock, unit price, and requested sales quantity. It rejects sales that exceed available stock, calculates successful sales, updates remaining stock, and warns when stock falls below 10 units.

### Python concepts used

- `input()` and `print()`
- `for` loop and `range()`
- `if` and `else` conditions inside a loop
- `while` loops for input validation
- `try` / `except` for invalid numeric input
- Arithmetic operators for sales and stock calculations
- Accumulator (`total_revenue`) for daily revenue
- Counters (`restock_count`, `successful_sales`)
- Lists and dictionaries for the medicine-wise report

### Sample execution

```text
How many different medicines will be processed? 2

--- Medicine 1 of 2 ---
Enter medicine name: Panadol
Enter available stock (units): 25
Enter price per unit (Rs.): 20
Enter quantity to sell: 18
Sale successful for Panadol.
Sales amount: Rs. 360.00
Remaining stock: 7 unit(s)
LOW-STOCK WARNING: Panadol has only 7 unit(s) remaining.

--- Medicine 2 of 2 ---
Enter medicine name: Syrup
Enter available stock (units): 5
Enter price per unit (Rs.): 100
Enter quantity to sell: 8
Sale rejected: only 5 unit(s) of Syrup are available.
No stock or revenue has been changed.

DAILY PHARMACY REPORT
Total medicines processed : 2
Successful medicine sales : 1
Medicines needing restock : 2
Total pharmacy revenue    : Rs. 360.00
```

The restock count includes any processed medicine whose remaining stock is below 10, including a medicine whose attempted sale was rejected if its original stock is already below 10.

## Requirements

- Python 3.8 or later
- No external packages are required

## How to Run

1. Install Python if it is not already installed.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run either program:

```bash
python student_scholarship_system.py
```

```bash
python pharmacy_inventory_system.py
```

On some Windows installations, use `py` instead of `python`:

```powershell
py student_scholarship_system.py
py pharmacy_inventory_system.py
```

Run the two files separately. Each application is independent.

## Suggested Test Scenarios

### Scholarship system

1. Marks 95, attendance 90, income 40,000: Full Scholarship.
2. Marks 85, attendance 88, income 50,000: Partial Scholarship.
3. Marks 79, attendance 90, income 40,000: Ineligible due to marks.
4. Marks 90, attendance 84, income 40,000: Ineligible due to attendance.
5. Marks 90, attendance 90, income 50,001: Ineligible due to income.
6. Enter letters for a numeric field or a percentage outside 0–100: program asks for valid input again.

### Pharmacy system

1. Sell a quantity less than available stock: sale succeeds and revenue increases.
2. Sell exactly the available stock: sale succeeds and remaining stock becomes zero.
3. Request more than available stock: sale is rejected and revenue is unchanged.
4. Remaining stock of 9: low-stock warning is displayed.
5. Enter a negative number or non-numeric value: program asks for valid input again.

## GitHub Submission

Create a public repository named `python-conditions-loops-assessment`, add the three files shown above, commit, and push the changes. Replace the placeholder below with your actual repository URL before submitting.

**Repository URL:** `https://github.com/YOUR-USERNAME/python-conditions-loops-assessment`
