#Exercise: Retry Simulation
#Student: Animesh Acharya
#Day: 2
#Exercise: 2

attempt = 1
max_attempts = 3
operation_successful = False

while attempt <= max_attempts:
    print(f"Attempt {attempt}")

    # Stretch: simulate success on the second attempt
    if attempt == 2:
        operation_successful = True

    if operation_successful:
        break

    attempt += 1

if operation_successful:
    print("Operation completed successfully")
else:
    print("Operation failed after three attempts")

print()