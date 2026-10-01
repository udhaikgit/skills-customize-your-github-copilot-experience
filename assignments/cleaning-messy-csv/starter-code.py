import csv
from pathlib import Path

INPUT_FILE = Path(__file__).with_name("data.csv")
OUTPUT_FILE = Path(__file__).with_name("cleaned-data.csv")
FIELDNAMES = ["student_name", "grade", "attendance_percent"]


def clean_student(row):
    """Return a cleaned record, or None when the row is invalid."""
    raise NotImplementedError("Complete the cleaning and validation rules")


def clean_csv():
    with INPUT_FILE.open(newline="", encoding="utf-8") as source:
        reader = csv.DictReader(source)

        with OUTPUT_FILE.open("w", newline="", encoding="utf-8") as destination:
            writer = csv.DictWriter(destination, fieldnames=FIELDNAMES)
            writer.writeheader()
            kept = 0
            skipped = 0

            for row in reader:
                cleaned = clean_student(row)
                if cleaned is None:
                    skipped += 1
                    continue

                writer.writerow(cleaned)
                kept += 1

    return kept, skipped


if __name__ == "__main__":
    kept, skipped = clean_csv()
    print(f"Rows kept: {kept}")
    print(f"Rows skipped: {skipped}")