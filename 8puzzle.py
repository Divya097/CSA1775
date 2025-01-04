import heapq

def heuristic(board, goal):
    return sum(abs(b % 3 - g % 3) + abs(b // 3 - g // 3) 
               for b, g in ((board.index(i), goal.index(i)) for i in range(1, 9)))

def neighbors(board):
    i = board.index(0)
    moves = []
    for d in (-1, 1, -3, 3):
        j = i + d
        if 0 <= j < 9 and not (i % 3 == 0 and d == -1) and not (i % 3 == 2 and d == 1):
            new_board = board[:]
            new_board[i], new_board[j] = new_board[j], new_board[i]
            moves.append(new_board)
    return moves

def solve_8_puzzle(initial, goal):
    heap = [(heuristic(initial, goal), 0, initial, [])]
    visited = set()

    while heap:
        _, moves, board, path = heapq.heappop(heap)
        if board == goal:
            return path + [board]
        visited.add(tuple(board))
        for neighbor in neighbors(board):
            if tuple(neighbor) not in visited:
                heapq.heappush(heap, (moves + 1 + heuristic(neighbor, goal), moves + 1, neighbor, path + [board]))

initial = [1, 2, 3, 4, 0, 5, 6, 7, 8]
goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]

solution = solve_8_puzzle(initial, goal)
if solution:
    for step in solution:
        for i in range(0, 9, 3):
            print(step[i:i+3])
        print()
else:
    print("No solution found.")
