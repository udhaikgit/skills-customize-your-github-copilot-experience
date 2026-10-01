# 📘 Assignment: Cleaning Messy CSV Data with Python

## 🎯 Objective

Use Python's built-in `csv` module to inspect and clean a small student-record dataset. Normalize text, validate values, and save clean rows without installing extra packages.

## 📝 Tasks

### 🛠️ Inspect the Dataset

#### Description
Open the provided `data.csv` file and inspect its rows using the `csv` module. Identify examples of inconsistent text, missing values, and values outside the expected ranges.

#### Requirements
Completed program should:

- Read the file with `csv.DictReader`
- Report the number of data rows
- Identify at least three different data-quality problems in the file


### 🛠️ Clean and Validate Records

#### Description
Complete `clean_student()` in the starter code. Return a cleaned record for valid rows, or `None` for a row that should be skipped.

#### Requirements
Completed program should:

- Remove extra whitespace from student names and format names consistently
- Accept only integer grades from 9 through 12 and attendance percentages from 0 through 100
- Skip rows with a blank name, missing or invalid grade, or missing or out-of-range attendance
- Convert valid grade and attendance values to integers


### 🛠️ Save Clean Data and Report

#### Description
Use the provided file-writing structure to save valid records to `cleaned-data.csv` and report how many rows were kept or skipped.

#### Requirements
Completed program should:

- Write valid records with `csv.DictWriter` and include a header row
- Save exactly 4 valid rows and skip exactly 5 invalid rows from the provided dataset
- Print the number of kept and skipped rows after processing