def digit_sum(n):
    # Calculate the sum of digits for a given number
    total = 0
    while n:
        total += n % 10
        n //= 10
    return total

def solution(A):
    # Initialize a dictionary to store the maximum number for each digit sum
    digit_sums = {}
    ans = -1  # Initialize the answer

    for num in A:
        # Calculate the sum of digits for the current number
        current_sum = digit_sum(num)

        if current_sum in digit_sums:
            # Update the answer if the sum of digits is already in the dictionary
            pair_sum = num + digit_sums[current_sum]
            ans = max(ans, pair_sum)
        else:
            # Add the current number to the dictionary
            digit_sums[current_sum] = num

    return ans

# Example usage
A1 = [51, 71, 17, 42]
A2 = [42, 33, 60]
A3 = [51, 32, 43]

print(solution(A1))  # Output: 93
print(solution(A2))  # Output: 102
print(solution(A3))  # Output: -1
