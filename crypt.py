from itertools import permutations

def solve_cryptarithm(word1, word2, result_word):
    # Combine all the unique letters from the input words
    unique_letters = ''.join(set(word1 + word2 + result_word))
    
    # Ensure that there are at most 10 unique letters
    if len(unique_letters) > 10:
        print("More than 10 unique letters, no solution possible.")
        return
    
    # Digits to assign to the letters
    digits = range(10)
    
    # Generate all possible digit assignments for the letters
    for perm in permutations(digits, len(unique_letters)):
        # Map letters to digits
        mapping = dict(zip(unique_letters, perm))
        
        # Ensure no leading zeroes in the input words
        if mapping[word1[0]] == 0 or mapping[word2[0]] == 0 or mapping[result_word[0]] == 0:
            continue
        
        # Convert letters to numbers
        num1 = int(''.join(str(mapping[letter]) for letter in word1))
        num2 = int(''.join(str(mapping[letter]) for letter in word2))
        result = int(''.join(str(mapping[letter]) for letter in result_word))
        
        # Check if the solution satisfies the equation
        if num1 + num2 == result:
            print(f"{word1}: {num1}, {word2}: {num2}, {result_word}: {result}")
            print(f"Mapping: {mapping}")
            return
    
    print("No solution found.")

# Get user input for the cryptarithm
word1 = input("Enter the first word: ").strip()
word2 = input("Enter the second word: ").strip()
result_word = input("Enter the result word: ").strip()

# Run the cryptarithm solver
solve_cryptarithm(word1, word2, result_word)
