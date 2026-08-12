# Day 1: Python Foundations

## Topics Covered

- Variables
- Data types
- String methods
- Operators
- Conditional statements

## Exercises

1. Sales Summary
2. Data Quality Checker
3. File Validator
4. Customer Record Cleaner
5. Pipeline Health Status
6. Dataset Access Decision

## What I Learned

I practiced storing values in variables and using f-strings to build clean, formatted output for reports. I got comfortable using conditional logic (if/elif/else) to classify data into categories, like flagging problematic rows or pipeline health, based on percentage thresholds. I also learned how string methods like `.strip()`, `.lower()`, and `.title()` are essential for cleaning messy, real-world text input before using it.

## Challenges Faced

One challenge was deciding how strict conditional checks should be — for example, in the pipeline health exercise, a low failure rate combined with a high runtime initially seemed like it should count as "Healthy," but the rules required both conditions to hold. I solved this by carefully re-reading the requirements and testing edge cases directly with `print()` statements to confirm the logic matched expectations. Another challenge was validating file extensions case-insensitively, which I solved using `.strip().lower()` before comparing against the allowed extensions.

## How to Run

Run each file using:
```
python sales_summary.py
python data_quality_checker.py
python file_validator.py
python customer_record_cleaner.py
python pipeline_health_status.py
python dataset_access_decision.py
```

