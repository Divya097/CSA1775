from collections import deque

def bfs(graph, start):
    # Create a set to track visited nodes
    visited = set()
    # Create a queue for BFS
    queue = deque([start])

    # List to store the BFS traversal
    traversal = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            traversal.append(node)

            # Add all unvisited neighbors to the queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return traversal

# Example graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Run BFS starting from node 'A'
result = bfs(graph, 'A')
print("BFS Traversal:", result)
