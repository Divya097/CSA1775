from itertools import permutations

def tsp_brute_force(graph, start):
    # Get all vertices except the starting vertex
    vertices = list(graph.keys())
    vertices.remove(start)
    
    # Generate all possible routes
    min_cost = float('inf')
    best_path = None

    for perm in permutations(vertices):
        current_path = [start] + list(perm) + [start]  # Route includes returning to the start
        current_cost = 0
        
        # Calculate the cost of the current path
        for i in range(len(current_path) - 1):
            current_cost += graph[current_path[i]][current_path[i + 1]]
        
        # Update minimum cost and best path
        if current_cost < min_cost:
            min_cost = current_cost
            best_path = current_path
    
    return best_path, min_cost

# Example graph as an adjacency matrix
graph = {
    'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
}

# Starting node
start_node = 'A'

# Solve TSP
best_path, min_cost = tsp_brute_force(graph, start_node)
print("Best Path:", " -> ".join(best_path))
print("Minimum Cost:", min_cost)
