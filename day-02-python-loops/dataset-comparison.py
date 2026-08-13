#Exercise: Dataset Comparison
#Student: Animesh Acharya
#Day: 2
#Exercise: 5

dataset_a = {
    "customer",
    "sales",
    "product",
    "employee"
}

dataset_b = {
    "sales",
    "product",
    "supplier",
    "inventory"
}

all_datasets = dataset_a | dataset_b
common_datasets = dataset_a & dataset_b
only_in_a = dataset_a - dataset_b
only_in_b = dataset_b - dataset_a

print("All unique dataset names:", all_datasets)
print("Datasets in both groups:", common_datasets)
print("Datasets only in dataset_a:", only_in_a)
print("Datasets only in dataset_b:", only_in_b)

print()



