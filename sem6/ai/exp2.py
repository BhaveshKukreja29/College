graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

def dfs(graph, start, goal):
    stack = [start]
    visited = []

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.append(node)

        if node == goal:
            print("Goal found:", node)
            return visited

        for neighbor in reversed(graph[node]):
            if neighbor not in visited:
                stack.append(neighbor)

    print("Goal not found")
    return visited

start = input("Enter start node: ")
goal = input("Enter goal node: ")

path = dfs(graph, start, goal)
print("DFS traversal:", path)
