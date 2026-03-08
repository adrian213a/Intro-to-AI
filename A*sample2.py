import heapq

# Graph with distances
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [('F', 2)],
    'E': [('F', 4)],
    'F': []
}

# Heuristic values (estimated distance to goal)
heuristic = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 2,
    'E': 2,
    'F': 0
}

def astar(start, goal):
    queue = [(0, start, [])]
    visited = set()

    while queue:
        (cost, node, path) = heapq.heappop(queue)

        if node in visited:
            continue

        path = path + [node]

        if node == goal:
            return path, cost

        visited.add(node)

        for neighbor, weight in graph[node]:
            new_cost = cost + weight + heuristic[neighbor]
            heapq.heappush(queue, (new_cost, neighbor, path))

path, cost = astar('A', 'F')

print("Shortest Path:", path)
print("Cost:", cost)
