#Exercise: Nested Order Summary
#Student: Animesh Acharya
#Day: 2
#Exercise: 7

orders = {
    "ORD-001": {
        "customer": "Anisha",
        "amount": 2500,
        "status": "Completed"
    },
    "ORD-002": {
        "customer": "Ravi",
        "amount": 1800,
        "status": "Pending"
    },
    "ORD-003": {
        "customer": "Maya",
        "amount": 3200,
        "status": "Completed"
    }
}

# 1. Print every order ID and customer
for order_id, details in orders.items():
    print(f"{order_id}: {details['customer']}")

# 2. Print only completed orders
print("\nCompleted orders:")
for order_id, details in orders.items():
    if details["status"] == "Completed":
        print(f"{order_id}: {details}")

# 3. Total amount of completed orders
total_completed_amount = sum(
    details["amount"] for details in orders.values() if details["status"] == "Completed"
)
print("\nTotal amount of completed orders:", total_completed_amount)

# 4. Count pending orders
pending_count = sum(1 for details in orders.values() if details["status"] == "Pending")
print("Number of pending orders:", pending_count)

# 5. Add a new order
orders["ORD-004"] = {
    "customer": "Sagar",
    "amount": 4100,
    "status": "Pending"
}
print("\nOrders after adding ORD-004:")
for order_id, details in orders.items():
    print(f"{order_id}: {details}")

print()