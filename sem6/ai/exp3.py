from collections import deque

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

def bfs(graph, start, goal):
    queue = deque([start])
    visited = []

    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        visited.append(node)

        if node == goal:
            print("Goal found:", node)
            return visited

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)

    print("Goal not found")
    return visited

def ucs(graph, cost, start, goal):
    queue = [(0, start)]
    visited = []

    while queue:
        queue.sort()
        curr_cost, node = queue.pop(0)

        if node in visited:
            continue
        visited.append(node)

        if node == goal:
            print("Goal found:", node, "with cost:", curr_cost)
            return visited

        for neighbor in graph[node]:
            if neighbor not in visited:
                edge_cost = cost.get((node, neighbor), 1)
                queue.append((curr_cost + edge_cost, neighbor))

    print("Goal not found")
    return visited

start = input("Enter start node: ")
goal = input("Enter goal node: ")

print("\n--- BFS ---")
path = bfs(graph, start, goal)
print("BFS traversal:", path)

print("\n--- UCS ---")
path = ucs(graph, cost, start, goal)
print("UCS traversal:", path)
