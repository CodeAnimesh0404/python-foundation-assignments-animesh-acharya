#Exercise: Sales List Analysis
#Student: Animesh Acharya
#Day: 2
#Exercise: 4

monthly_sales = [85000, 120000, 95000, 140000, 75000, 160000]

# 1. Sorted list from highest to lowest
sorted_sales_desc = sorted(monthly_sales, reverse=True)
print("Sorted (highest to lowest):", sorted_sales_desc)

# 2. Only values above 100000
high_sales = [amount for amount in monthly_sales if amount > 100000]
print("Sales above 100000:", high_sales)

# 3. Each amount with 13% tax added
sales_with_tax = [round(amount * 1.13, 2) for amount in monthly_sales]
print("Sales with 13% tax added:", sales_with_tax)

# 4. Total sales amount
total_sales = sum(monthly_sales)
print("Total sales:", total_sales)

# 5. Average sales amount
average_sales = total_sales / len(monthly_sales)
print("Average sales:", round(average_sales, 2))

print()