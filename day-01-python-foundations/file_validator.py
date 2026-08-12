Exercise: File Validator
Student: Animesh Acharya
Day: 1
Exercise: 3

# Input values
valid_extensions = (".csv", ".json", ".parquet")

# User input
file_name = input("Enter a file name: ")
# Cleaning
file_name_clean = file_name.strip().lower()

# Validation and output
if file_name_clean.endswith(valid_extensions):
    print(f"'{file_name}' is a valid file type.")
else:
    print(f"'{file_name}' is NOT a valid file type.")
