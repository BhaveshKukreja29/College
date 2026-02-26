graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

cost = {
    ('A', 'B'): 1,
    ('A', 'C'): 4,
    ('B', 'D'): 3,
    ('B', 'E'): 8,
    ('C', 'F'): 5,
    ('C', 'G'): 2
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 3,
    'D': 9,
    'E': 0,
    'F': 1,
    'G': 0
}

def greedy(graph, heuristic, start, goal):
    queue = [(heuristic[start], start)]
    visited = []

    while queue:
        queue.sort()
        _, node = queue.pop(0)

        if node in visited:
            continue
        visited.append(node)

        if node == goal:
            print("Goal found:", node)
            return visited

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((heuristic[neighbor], neighbor))

    print("Goal not found")
    return visited

def a_star(graph, cost, heuristic, start, goal):
    queue = [(heuristic[start], 0, start)]
    visited = []

    while queue:
        queue.sort()
        f, g, node = queue.pop(0)

        if node in visited:
            continue
        visited.append(node)

        if node == goal:
            print("Goal found:", node, "with cost:", g)
            return visited

        for neighbor in graph[node]:
            if neighbor not in visited:
                edge_cost = cost.get((node, neighbor), 1)
                new_g = g + edge_cost
                new_f = new_g + heuristic[neighbor]
                queue.append((new_f, new_g, neighbor))

    print("Goal not found")
    return visited

start = input("Enter start node: ")
goal = input("Enter goal node: ")

print("\n--- Greedy Best First Search ---")
path = greedy(graph, heuristic, start, goal)
print("Greedy traversal:", path)

print("\n--- A* Search ---")
path = a_star(graph, cost, heuristic, start, goal)
print("A* traversal:", path)
