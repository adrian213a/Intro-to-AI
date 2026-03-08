from itertools import combinations

transactions = [
    ['bread', 'milk'],
    ['bread', 'butter'],
    ['milk', 'butter'],
    ['bread', 'milk', 'butter']
]

# Minimum support (how many times item must appear)
min_support = 2

items = set(item for transaction in transactions for item in transaction)

print("Frequent 1-itemsets:")

for item in items:
    count = sum(1 for transaction in transactions if item in transaction)
    if count >= min_support:
        print(item, "appears", count, "times")
