from collections import deque

def is_valid_state(m, c):
    return 0 <= m <= 3 and 0 <= c <= 3 and (m >= c or m == 0) and (3 - m >= 3 - c or 3 - m == 0)

def bfs():
    initial_state, goal_state = (3, 3, 0), (0, 0, 1)
    queue, visited = deque([(initial_state, [])]), set([initial_state])

    while queue:
        (m, c, b), path = queue.popleft()
        if (m, c, b) == goal_state: return path + [(m, c, b)]
        
        for dm, dc in [(-2, 0), (-1, 0), (0, -2), (1, 0), (0, 1), (0, -1)]:
            new_m, new_c = (m + dm, c + dc) if b == 0 else (m - dm, c - dc)
            if is_valid_state(new_m, new_c):
                new_state = (new_m, new_c, 1 - b)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, path + [(m, c, b)]))

    return None

solution = bfs()
if solution:
    for step in solution:
        print(f"Missionaries: {step[0]}, Cannibals: {step[1]}, Boat: {'Left' if step[2] == 0 else 'Right'}")
else:
    print("No solution found.")
