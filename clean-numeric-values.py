#Exercise: Clean Numeric Values
#Student: Animesh Acharya
#Day: 2
#Exercise: 3

raw_values = [100, None, 250, "invalid", 300, None, 450]

# --- Method 1: loop + continue + isinstance() ---
clean_values_loop = []

for value in raw_values:
    if not isinstance(value, int) or isinstance(value, bool):
        continue
    clean_values_loop.append(value)

print("Using loop + continue:", clean_values_loop)

# --- Method 2: list comprehension ---
clean_values_comprehension = [
    value for value in raw_values
    if isinstance(value, int) and not isinstance(value, bool)
]

print("Using list comprehension:", clean_values_comprehension)

print()