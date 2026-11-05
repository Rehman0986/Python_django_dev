"""
Student Scholarship Eligibility System
Topic: Conditional Statements (if, elif, else)

Evaluates a student's scholarship eligibility using academic marks,
attendance percentage, and monthly family income.
"""


def get_percentage(prompt):
    """Read and validate a percentage between 0 and 100."""
    while True:
        try:
            value = float(input(prompt))
            if 0 <= value <= 100:
                return value
            print("Invalid value. Enter a percentage from 0 to 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def get_non_negative_income(prompt):
    """Read and validate a non-negative monthly income."""
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            print("Income cannot be negative. Try again.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def main():
    print("=" * 55)
    print("       STUDENT SCHOLARSHIP ELIGIBILITY SYSTEM")
    print("=" * 55)

    # Collect and validate the student's name.
    while True:
        student_name = input("Enter student's name: ").strip()
        if student_name:
            break
        print("Name cannot be empty. Please try again.")

    # Collect and validate academic information.
    marks = get_percentage("Enter academic marks (0-100): ")
    attendance = get_percentage("Enter attendance percentage (0-100): ")
    monthly_income = get_non_negative_income("Enter monthly family income (Rs.): ")

    # Evaluate each eligibility requirement separately.
    reasons = []

    if marks < 80:
        reasons.append("Academic marks are below the required 80%.")
    if attendance < 85:
        reasons.append("Attendance is below the required 85%.")
    if monthly_income > 50000:
        reasons.append("Monthly family income exceeds Rs. 50,000.")

    # Prepare the scholarship decision.
    if len(reasons) == 0:
        if marks >= 90:
            scholarship_type = "Full Scholarship"
        elif marks >= 80:
            scholarship_type = "Partial Scholarship"
        else:
            # This branch is a defensive fallback; eligible marks are at least 80.
            scholarship_type = "No Scholarship"
        status = "ELIGIBLE"
    else:
        scholarship_type = "Not Eligible"
        status = "NOT ELIGIBLE"

    # Display a complete evaluation report.
    print("\n" + "=" * 55)
    print("             SCHOLARSHIP EVALUATION REPORT")
    print("=" * 55)
    print(f"Student Name          : {student_name}")
    print(f"Academic Marks        : {marks:.2f}%")
    print(f"Attendance            : {attendance:.2f}%")
    print(f"Monthly Family Income : Rs. {monthly_income:,.2f}")
    print("-" * 55)
    print(f"Eligibility Status    : {status}")
    print(f"Scholarship Decision  : {scholarship_type}")

    if reasons:
        print("\nReason(s) for Ineligibility:")
        for number, reason in enumerate(reasons, start=1):
            print(f"{number}. {reason}")
    else:
        print("\nAll scholarship eligibility requirements have been met.")

    print("=" * 55)


if __name__ == "__main__":
    main()
