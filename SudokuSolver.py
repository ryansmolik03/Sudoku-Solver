import math
import sys

# default board
board = [[5, 3, 0, 0, 7, 0, 0, 0, 0], 
         [6, 0, 0, 1, 9, 5, 0, 0, 0],
         [0, 9, 8, 0, 0, 0, 0, 6, 0],
         [8, 0, 0, 0, 6, 0, 0, 0, 3],
         [4, 0, 0, 8, 0, 3, 0, 0, 1],
         [7, 0, 0, 0, 2, 0, 0, 0, 6],
         [0, 6, 0, 0, 0, 0, 2, 8, 0], 
         [0, 0, 0, 4, 1, 9, 0, 0, 5],
         [0, 0, 0, 0, 8, 0, 0, 7, 9]]

# print board functionality
def print_board(b):
    for r in range(len(b)):
        if r % 3 == 0 and r != 0:
            print("- - -   - - -   - - -")
        for c in range(len(b[0])):
            if c % 3 == 0 and c != 0:
                print("| ", end="")
            if c == 8:
                print(b[r][c])
            else:
                print(str(b[r][c]) + " ", end="")

# find empty space utility function
def find_empty_space(b):
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == 0:
                return (i, j)
    return None

# check if a space is valid
def is_valid(b, num, pos):
    # check if row is valid
    for c in range(len(b[0])):
        if b[pos[0]][c] == num and pos[1] != c:
            return False

    # check if column valid
    for r in range(len(b)):
        if b[r][pos[1]] == num and pos[0] != r:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for r in range(box_y * 3, box_y * 3 + 3):
        for c in range(box_x * 3, box_x * 3 + 3):
            if b[r][c] == num and (r, c) != pos:
                return False
    return True

# solve the game
def solve(b):
    empty = find_empty_space(b)
    if not empty:
        return True
    else:
        row, col = empty
    
    for i in range(1, 10):
        if is_valid(b, i, (row, col)):
            b[row][col] = i

            if solve(b):
                return True
        
            b[row][col] = 0

    return False

print_board(board)
solve(board)
print("SOLUTION\n")
print_board(board)