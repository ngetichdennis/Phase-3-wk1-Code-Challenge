# def solution(A):
#     N = len(A)
#     total_bricks = sum(A)
#     target_bricks = 10
#     min_moves = float('inf')
    
#     # Calculate the total number of moves needed to make all boxes have 10 bricks
#     for i in range(N):
#         moves = 0
#         current_bricks = A[i]
#         j = i + 1
        
#         # Move bricks to the left
#         while current_bricks < target_bricks:
#             if j == N:
#                 break
#             moves += A[j] - target_bricks + current_bricks
#             current_bricks = A[j]
#             j += 1
        
#         # Move bricks to the right
#         if current_bricks > target_bricks:
#             j = i - 1
#             while current_bricks > target_bricks:
#                 if j == -1:
#                     break
#                 moves += current_bricks - target_bricks + A[j]
#                 current_bricks = A[j]
#                 j -= 1
        
#         min_moves = min(min_moves, moves)
    
#     # Check if it is possible to make all boxes have 10 bricks
#     if min_moves == float('inf') or min_moves > total_bricks:
#         return -1
#     else:
#         return min_moves
# min_moves=solution([11, 10, 8, 12, 8, 10, 11])
# print(min_moves)
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