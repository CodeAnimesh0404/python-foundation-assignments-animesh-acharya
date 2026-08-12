Exercise: Pipeline Health Status
Student: Animesh Acharya
Day: 1
Exercise: 5

# Function to evaluate pipeline health
def check_pipeline(rows_loaded, rows_failed, runtime_minutes):
    failure_rate = (rows_failed / rows_loaded) * 100

    # Classification
    if failure_rate <= 2 and runtime_minutes <= 20:
        status = "Healthy"
    elif failure_rate <= 5:
        status = "Warning"
    else:
        status = "Critical"

    # Output
    print(f"Rows loaded: {rows_loaded}")
    print(f"Rows failed: {rows_failed}")
    print(f"Runtime: {runtime_minutes} minutes")
    print(f"Failure rate: {failure_rate:.2f}%")
    print(f"Pipeline status: {status}")
    print("-" * 30)

# Main data given in the exercise
rows_loaded = 9800
rows_failed = 200
runtime_minutes = 18
check_pipeline(rows_loaded, rows_failed, runtime_minutes)

# Test case 1
check_pipeline(9500, 500, 15)

# Test case 2
check_pipeline(9900, 100, 30)


