import random

def fitness(x):
    return -(x-5)**2 + 25

population = [random.randint(0,10) for _ in range(10)]

for i in range(10):
    population = sorted(population, key=fitness, reverse=True)
    population = population[:5] + [random.randint(0,10) for _ in range(5)]

best = max(population, key=fitness)

print("Best value:", best)
