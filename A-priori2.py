from itertools import combinations

transactions = [
    ['bread','milk'],
    ['bread','butter'],
    ['milk','butter'],
    ['bread','milk','butter']
]

items = ['bread','milk','butter']

for combo in combinations(items,2):
    count = 0
    for t in transactions:
        if set(combo).issubset(t):
            count += 1
    print(combo, "appears", count, "times")
