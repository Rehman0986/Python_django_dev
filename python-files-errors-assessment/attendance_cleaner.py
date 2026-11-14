"""Task 2: Attendance Log Cleaner (attendance.txt -> attendance_clean.csv)."""

import csv

INPUT_FILE = "attendance.txt"
OUTPUT_FILE = "attendance_clean.csv"


def read_lines(path):
    # Read all lines of the text file; return None (after a message) if it cannot be read.
    try:
        with open(path, encoding="utf-8") as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Error: {path} was not found. Put it in the same folder as this program.")
    except UnicodeDecodeError:
        print(f"Error: {path} is not valid UTF-8 text. Save it as UTF-8 and try again.")
    except OSError as error:
        print(f"Error: could not read {path} ({error}).")
    return None


def clean_names(lines):
    # List comprehension: strip extra spaces, fix capitals, and skip blank lines.
    return [" ".join(line.strip().split()).title() for line in lines if line.strip()]


def write_csv(path, names):
    # Write the cleaned, sorted names to a CSV file. Returns True if it worked.
    try:
        with open(path, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["name"])
            for name in names:
                writer.writerow([name])
        return True
    except OSError as error:
        # Common on Windows: the CSV is open in Excel, so it is locked.
        print(f"Error: could not write {path} (is it open in another program?). Details: {error}")
        return False


def main():
    lines = read_lines(INPUT_FILE)
    if lines is None:
        return

    cleaned = clean_names(lines)
    if not cleaned:
        print(f"No names found in {INPUT_FILE}. Nothing to clean.")
        return

    unique_students = set(cleaned)          # a set keeps each student once
    sorted_students = sorted(unique_students)

    print(f"Names read (blank lines ignored) : {len(cleaned)}")
    print(f"Unique students                  : {len(unique_students)}")
    print(f"Duplicates removed               : {len(cleaned) - len(unique_students)}")
    print("\nUnique students (sorted):")
    for number, name in enumerate(sorted_students, start=1):
        print(f"  {number}. {name}")

    if write_csv(OUTPUT_FILE, sorted_students):
        print(f"\nSaved {len(sorted_students)} name(s) to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
