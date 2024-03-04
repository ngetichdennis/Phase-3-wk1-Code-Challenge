def generate_string(N):
    # Calculate the number of times each letter should appear
    letters_count = N // 26
    remainder = N % 26

    # Create a list of letters from 'a' to 'z'
    letters = [chr(ord('a') + i) for i in range(26)]

    # Construct the string
    result = ''.join(letters_count * letter for letter in letters)
    result += ''.join(letters[:remainder])  # Add any remaining letters

    return result

# Example usage
print(generate_string(3)) 
print(generate_string(5))  
print(generate_string(30))  