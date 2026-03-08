import random

population = [random.randint(0,100) for _ in range(10)]

for generation in range(5):
    population = sorted(population, reverse=True)
    best = population[:5]

    children = []
    for i in range(5):
        child = (best[i] + best[(i+1)%5]) // 2
        children.append(child)

    population = best + children

print("Best solution:", max(population))
