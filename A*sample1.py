import heapq

def astar(graph, start, goal):
    queue = [(0, start)]
    visited = set()

    while queue:
        (cost, node) = heapq.heappop(queue)

        if node == goal:
            return cost

        if node in visited:
            continue

        visited.add(node)

        for neighbor, weight in graph[node]:
            heapq.heappush(queue, (cost + weight, neighbor))

graph = {
    'A': [('B',1), ('C',4)],
    'B': [('C',2), ('D',5)],
    'C': [('D',1)],
    'D': []
}

print("Shortest cost:", astar(graph, 'A', 'D'))
