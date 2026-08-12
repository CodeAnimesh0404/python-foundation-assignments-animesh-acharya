valid_extensions = (".csv", ".json", ".parquet")

file_name = input("Enter a file name: ")
file_name_clean = file_name.strip().lower()

if file_name_clean.endswith(valid_extensions):
    print(f"'{file_name}' is a valid file type.")
else:
    print(f"'{file_name}' is NOT a valid file type.")