def is_valid(node, color, graph, colors):
    """Check if coloring node with color is valid."""
    for neighbor in graph[node]:
        if colors[neighbor] == color:
            return False
    return True

def solve_map_coloring(graph, color_options, colors, node):
    """Recursive function to solve the map coloring problem."""
    # If all nodes are colored, return True
    if node == len(graph):
        return True

    # Get the current node
    current_node = list(graph.keys())[node]

    # Try all colors for the current node
    for color in color_options:
        if is_valid(current_node, color, graph, colors):
            colors[current_node] = color  # Assign the color
            if solve_map_coloring(graph, color_options, colors, node + 1):
                return True
            colors[current_node] = None  # Backtrack

    return False

# Example graph (Map) representation
graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E"],
    "E": ["C", "D"]
}

# Available colors
color_options = ["Red", "Green", "Blue"]

# Initialize colors for all nodes as None
colors = {node: None for node in graph}

# Solve the problem
if solve_map_coloring(graph, color_options, colors, 0):
    print("Solution found:")
    print(colors)
else:
    print("No solution exists.")
