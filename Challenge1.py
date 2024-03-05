
def solution(A):
    N = len(A)
    total_bricks = sum(A)
    target_bricks = 10
    min_moves = float('inf')
    
    # Calculate the total number of moves needed to make all boxes have 10 bricks
    for i in range(N):
        moves = 0
        remaining_bricks = target_bricks - A[i]
        if remaining_bricks < 0:
            continue
        for j in range(i + 1, N):
            moves += abs(remaining_bricks - A[j]) // target_bricks
            remaining_bricks -= A[j]
            if remaining_bricks == 0:
                break
        else:
            continue
        min_moves = min(min_moves, moves)
    
    # Check if it is possible to make all boxes have 10 bricks
    if min_moves == float('inf'):
        return -1
    return min_moves
min_moves=solution([11, 10, 8, 12, 8, 10, 11])
print(min_moves)