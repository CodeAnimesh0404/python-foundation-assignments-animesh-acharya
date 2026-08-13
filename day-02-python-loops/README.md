# Day 2: Loops, Collections & Dictionaries

## Topics Covered:

- for loops and range()
- while loops
- break and continue
- isinstance()
- List comprehensions
- Sets and set operations
- Dictionaries and dictionary comprehensions
- Nested dictionaries
  
##Exercises:

1. Batch Processor
2. Retry Simulation
3. Clean Numeric Values
4. Sales List Analysis
5. Dataset Comparison
6. Student Score Dictionary
7. Nested Order Summary
8. Stretch: Contact Book Menu
   
## What I Learned:

I practiced using for loops with range() to process numbered batches, and used the modulo operator (%) to trigger an action after every third iteration. I also worked with while loops to control retry logic, using a counter and a boolean flag to decide when to stop the loop with break, and when to fall through and report a failure. For cleaning messy data, I used isinstance() combined with continue to skip invalid values, then rewrote the same logic more concisely with a list comprehension. I also got more comfortable with sets (union, intersection, difference) for comparing two collections, and with dictionaries — including dictionary comprehensions for filtering key-value pairs, and nested dictionaries for representing structured records like orders and contacts.

## Challenges Faced:

One challenge in the numeric cleaning exercise was that isinstance(value, int) also returns True for booleans, since bool is a subclass of int in Python. I solved this by adding an extra check (not isinstance(value, bool)) so that True/False values wouldn't accidentally be treated as valid numbers. Another challenge was in the retry simulation, making sure the "success" flag was checked in the right order relative to break, so the attempt counter and printed messages stayed accurate. For the contact book stretch exercise, the main challenge was making sure searching for or deleting a contact that doesn't exist wouldn't crash the program — I handled this by checking if name in contacts before accessing or removing anything.

## How to Run

Run each file using:
```
python batch_processor.py
python retry_simulation.py
python clean_numeric_values.py
python sales_list_analysis.py
python dataset_comparison.py
python student_score_dictionary.py
python nested_order_summary.py
python contact_book.py
