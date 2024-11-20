from math import ceil, floor

def min_numbers_to_zero(S, N):
    print(S, N)
    # Initialize dp array with infinity
    dp = [float('inf')] * (N + 1)
    dp[0] = 0  # Base case

    
    # Compute dp values
    for i in range(1, N + 1):
        for s in S:
            if i - s >= 0:
                dp[i] = min(dp[i], dp[i - s] + 1)

    # Return result
    return dp[N] if dp[N] != float('inf') else -1  # -1 if no solution exists

# Example usage
file = open('part3.txt', 'r')

notes = []

for line in file.readlines():
    notes.append(int(line[:-1]))
    
file.close()

dots = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30, 37, 38, 49, 50, 74, 75, 100, 101]

bettles_count = 0

diff = 100

for note in notes:
        
    note_1 = note // 2
    note_2 = ceil(note / 2)
    
    bettles_count_1 = min_numbers_to_zero(dots, note_1)
    bettles_count_2 = min_numbers_to_zero(dots, note_2)
    
    if abs(bettles_count_2 - bettles_count_1) < diff:
        bettles_count += bettles_count_1
        bettles_count += bettles_count_2

print(bettles_count)

