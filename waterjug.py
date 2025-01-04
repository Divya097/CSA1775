from math import gcd
from collections import deque

def water_jug_problem(a, b, c):
    if c > max(a, b) or c % gcd(a, b) != 0:
        return -1

    visited = set()
    queue = deque([(0, 0, 0)])  # (jug1, jug2, steps)
    while queue:
        jug1, jug2, steps = queue.popleft()
        if (jug1, jug2) in visited:
            continue
        visited.add((jug1, jug2))
        if jug1 == c or jug2 == c:
            print(f"Conclusion: It is possible to measure exactly {c} liters using {a} and {b} liter jugs.")
            return steps
        # Add possible states
        queue.extend([
            (a, jug2, steps + 1), (jug1, b, steps + 1),  # Fill jugs
            (0, jug2, steps + 1), (jug1, 0, steps + 1),  # Empty jugs
            (max(0, jug1 - (b - jug2)), min(b, jug1 + jug2), steps + 1),  # Pour jug1 -> jug2
            (min(a, jug1 + jug2), max(0, jug2 - (a - jug1)), steps + 1)   # Pour jug2 -> jug1
        ])
    print(f"Conclusion: It is not possible to measure exactly {c} liters using {a} and {b} liter jugs.")
    return -1

# Example Usage
a, b, c = 3, 5, 4
result = water_jug_problem(a, b, c)
if result != -1:
    print(f"Minimum steps required: {result}")
else:
    print("No solution exists.")
