#Exercise: Batch Processor
#Student: Animesh Acharya
#Day: 2
#Exercise: 1

for batch_number in range(1, 11):
    print(f"Processing batch {batch_number}")
    if batch_number % 3 == 0:
        print("Checkpoint reached")

print()