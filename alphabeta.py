import math

def alpha_beta(stones, alpha, beta, is_maximizing):
    if stones == 0:
        return -1 if is_maximizing else 1
    best_score = -math.inf if is_maximizing else math.inf
    for move in range(1, min(3, stones) + 1):
        score = alpha_beta(stones - move, alpha, beta, not is_maximizing)
        best_score = max(best_score, score) if is_maximizing else min(best_score, score)
        alpha = max(alpha, best_score) if is_maximizing else min(beta, best_score)
        if beta <= alpha:
            break
    return best_score

def best_move(stones):
    best_score = -math.inf
    best_move = None
    for move in range(1, min(3, stones) + 1):
        score = alpha_beta(stones - move, -math.inf, math.inf, False)
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def nim_game():
    stones = int(input("Enter the initial number of stones: "))
    while stones > 0:
        print(f"Stones remaining: {stones}")
        move = int(input("Your turn. Take 1, 2, or 3 stones: "))
        if move < 1 or move > 3 or move > stones:
            print("Invalid move. Try again.")
            continue
        stones -= move
        if stones == 0:
            print("You lose! AI wins!")
            break
        ai_move = best_move(stones)
        print(f"AI takes {ai_move} stones.")
        stones -= ai_move
        if stones == 0:
            print("You win! AI loses!")

# Run the game
nim_game()
