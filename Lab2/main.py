import random

# s-box
# C-R-A-Q-W-X-V-Y-T-E
# Randomly pick a letter to assign to another (Could have letter assigned to its self)
# Q-T- Use a list to remember which letters have been used so that it doesn't get reused

sbox = {
    'C': 'Q',
    'R': 'T',
    'A': 'W',
    'Q': 'E',
    'W': 'C',
    'X': 'R',
    'V': 'Y',
    'Y': 'V',
    'T': 'A',
    'E': 'X'
}

ptext = 'CRATEWARTARTQVYTEVYQ'

# Generate a box with n columns, for shifting rows
matrix = [['C', 'R', 'A', 'T'],
          ['E', 'W', 'A', 'R'],
          ['T', 'A', 'R', 'T'],
          ['Q', 'V', 'Y', 'T'],
          ['E', 'V', 'Y', 'Q']]

# Implementing SubByte
print(matrix)
for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        # print(matrix[r][c], end=' ')
        matrix[r][c] = sbox[matrix[r][c]]
        # print(sbox[matrix[r][c]])

print(matrix)


