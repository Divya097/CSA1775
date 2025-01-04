from queue import PriorityQueue

def a_star(graph, start, goal, heuristic):
    open_set = PriorityQueue()
    open_set.put((0, start))
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    came_from = {}

    while not open_set.empty():
        _, current = open_set.get()
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return [start] + path[::-1], g_score[goal]

        for neighbor, weight in graph[current].items():
            new_g = g_score[current] + weight
            if new_g < g_score[neighbor]:
                g_score[neighbor] = new_g
                open_set.put((new_g + heuristic[neighbor], neighbor))
                came_from[neighbor] = current

    return None, float('inf')

# Example usage
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
heuristic = {'A': 7, 'B': 6, 'C': 2, 'D': 0}
path, cost = a_star(graph, 'A', 'D', heuristic)
print("Path:", path)
print("Cost:", cost)
