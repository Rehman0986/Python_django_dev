# Python Conditional Statements — Smart Canteen Discount System

A beginner-friendly Python console program created during the Python lecture on **conditional statements**. It demonstrates how a program makes decisions using `if`, `elif`, and `else` in a realistic college-canteen scenario.

## Repository Name

`python-conditionals-smart-canteen`

## Class Demonstration

The class used a canteen bill to explain how conditions choose one outcome from several possible outcomes.

| Bill Amount | Standard Discount |
|---|---:|
| Rs. 3,000 or more | 20% |
| Rs. 2,000 to below Rs. 3,000 | 10% |
| Rs. 1,000 to below Rs. 2,000 | 5% |
| Below Rs. 1,000 | 0% |

The program then displays the original bill, discount amounts, total savings, and final payable amount.

## Concepts Covered

- `if`: runs a block when a condition is true.
- `elif`: checks another condition when earlier conditions were false.
- `else`: handles the remaining case when no previous condition matched.
- Comparison operators such as `>=` and `<=`.
- Input using `input()` and numeric conversion using `float()`.
- Input validation and `try/except` for non-numeric values.
- Calculations with percentages.
- String formatting using f-strings and `:.2f`.
- Membership checks and combined bill calculations.

## Program Enhancements

The lecture's student challenge is included in this version:

1. Reject bill amounts that are zero or negative.
2. Ask whether the student has a membership card.
3. Apply an additional 5% membership discount to the amount remaining after the standard discount.
4. Show total savings and a congratulatory message when a discount is applied.

**Discount calculation note:** The membership discount is calculated after the standard discount. For example, if the bill is Rs. 3,000, the standard discount is Rs. 600. A member then receives 5% of the remaining Rs. 2,400 (Rs. 120), making total savings Rs. 720 and the final bill Rs. 2,280.

## How to Run

1. Install Python 3.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:

```bash
python smart_canteen_discount.py
```

On some systems, use `python3` instead of `python`.

## Example Run

```text
================================
       SMART CANTEEN
================================
Enter your total bill amount (Rs.): 3000
Do you have a membership card? (yes/no): yes

================================
         BILL SUMMARY
================================
Original Bill:                 Rs. 3000.00
Standard Discount (20%):       Rs. 600.00
Membership Discount:           Rs. 120.00
Total Savings:                 Rs. 720.00
Final Payable Amount:          Rs. 2280.00
Congratulations! You saved Rs. 720.00.
```

## UI/UX Notes

This is a **console-based** program, not a graphical web interface. Its basic user-experience choices are:

- A clear title and section separators.
- A direct prompt that tells the user what to enter.
- Currency labels (`Rs.`) and two decimal places for money.
- A readable bill summary with discounts shown separately.
- Friendly success and validation messages.

These choices make the output easier for a beginner to follow. A future extension could add a graphical interface or web page, but that is outside the scope of this Python conditionals exercise.

## Practice Challenges

1. Add a rule that rejects membership answers other than `yes` or `no`.
2. Add a student category (e.g., regular student or staff) and introduce a new condition.
3. Add a maximum discount limit.
4. Print which standard discount tier was selected.
5. Explain why `elif` is suitable here instead of several independent `if` statements.

## Suggested Git Commit

```text
Add Python conditionals smart canteen discount example
```

## Suggested Repository Description

Beginner Python lesson demonstrating if, elif, else, comparison operators, input validation, and a real-world canteen discount calculator.
