# ai_vs_manual_sort.py

data = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Rebbrown', 'age': 25},
    {'name': 'Naomi', 'age': 35}
]

# AI-suggested version using sorted()
def sort_by_key(data, key):
    return sorted(data, key=lambda x: x[key])

# Manual insertion sort version
def sort_by_key_manual(data, key):
    sorted_list = []
    for item in data:
        inserted = False
        for i, sorted_item in enumerate(sorted_list):
            if item[key] < sorted_item[key]:
                sorted_list.insert(i, item)
                inserted = True
                break
        if not inserted:
            sorted_list.append(item)
    return sorted_list

# Run both versions
sorted_ai = sort_by_key(data, 'age')
sorted_manual = sort_by_key_manual(data, 'age')

# Print results
print("AI-suggested sort:")
for item in sorted_ai:
    print(item)

print("\nManual sort:")
for item in sorted_manual:
    print(item)

# Basic comparison
print("\nComparison:")
print("AI version is shorter, uses built-in Timsort (O(n log n)), and is more readable.")
print("Manual version is educational but less efficient (O(n^2)) and verbose.")
