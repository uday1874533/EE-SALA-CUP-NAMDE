# cook your dish here
# not done try:
    
def rot_k_cipher(S, T, U):
    N = len(S)
    K = (ord(T[0]) - ord(S[0])) % 26

    result = ''
    for i in range(N):
        char = U[i]
        rotated_char = chr((ord(char) - ord('a') + K) % 26 + ord('a'))
        result += rotated_char

    return result

# Read the number of queries
Q = int(input())

# Iterate through each query
for _ in range(Q):
    # Read the length of the strings
    N = int(input())

    # Read the strings S, T, and U
    S = input()
    T = input()
    U = input()

    # Calculate the ROT-K cipher of U
    cipher = rot_k_cipher(S, T, U)

    # Print the result
    print(cipher)
