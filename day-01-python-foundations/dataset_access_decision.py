#Exercise: Dataset Access Decision
#Student: Animesh Acharya
#Day: 1
#Exercise: Stretch

# Input values
allowed_roles = ["analyst", "scientist", "engineer"]
restricted_datasets = ["salary_data", "personal_data"]

# Function to evaluate access decision
def check_access(user_role, is_active, requested_dataset):
    # Collect all reasons for denial
    reasons = []

    if not is_active:
        reasons.append("the user is inactive")
    if user_role not in allowed_roles:
        reasons.append("the role is not allowed")
    if requested_dataset in restricted_datasets:
        reasons.append("the dataset is restricted")

    # Output
    print(f"Role: {user_role}, Active: {is_active}, Dataset: {requested_dataset}")
    if reasons:
        for reason in reasons:
            print(f"Access denied because {reason}.")
    else:
        print(f"Access granted to '{requested_dataset}'.")
    print("-" * 30)

# Main data given to create: everything valid -> granted
user_role = "analyst"
is_active = True
requested_dataset = "sales_data"
check_access(user_role, is_active, requested_dataset)

# Test case 1: inactive user
check_access("analyst", False, "sales_data")

# Test case 2: role not allowed
check_access("manager", True, "sales_data")

# Test case 3: restricted dataset
check_access("engineer", True, "salary_data")

# Test case 4: multiple problems at once
check_access("scientist", False, "personal_data")
