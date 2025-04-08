import numpy as np

# define the matrix to detect the patterns in the puzzle
horizontal_matrix = np.array([["X", "M", "A", "S"]])
vertical_matrix = np.array([["X", "M", "A", "S"]]).copy().T
inv_vertical_matrix = np.flip(vertical_matrix)
inv_horizontal_matrix = np.flip(horizontal_matrix)

# for part 2
pattern_x1 = np.array(["M", "A", "S", "M", "A", "S"])
pattern_x2 = np.array(["M", "A", "S", "S", "A", "M"])
pattern_x3 = np.array(["S", "A", "M", "M", "A", "S"])
pattern_x4 = np.array(["S", "A", "M", "S", "A", "M"])

if __name__ == "__main__":
    # got input_numbers simply using CTRL + F search and replace on original puzzle (X -> 1, M -> 2, A -> 3, S -> 4)
    path = "day4/input.txt"
    file = open(path, encoding="utf-8").read().strip().split("\n")
    matrix_puzzle = []
    for string in file:
        matrix_puzzle.append([i for i in string])
    matrix_puzzle = np.array(matrix_puzzle)
    

    # PART 1
    
    print(matrix_puzzle.shape) # 140x140
    vertical_count = 0
    horizontal_count = 0
    
    sliding_window_hor = np.lib.stride_tricks.sliding_window_view(matrix_puzzle, (1, 4)).reshape(-1, 1, 4)
    sliding_window_vert = np.lib.stride_tricks.sliding_window_view(matrix_puzzle, (4, 1)).reshape(-1, 4, 1)
    # horizontales 
    
    for window in sliding_window_vert:
        if np.all(window == vertical_matrix) or np.all(window == inv_vertical_matrix):
            vertical_count += 1
    print("Vertical count :", vertical_count)
    
    for window in sliding_window_hor:
        if np.all(window == horizontal_matrix) or np.all(window == inv_horizontal_matrix):
            horizontal_count += 1
    print("Horizontal count :", horizontal_count)
    
    # diagonales
    
    diagonal_count = 0
    sliding_window_diag = np.lib.stride_tricks.sliding_window_view(matrix_puzzle, (4, 4)).reshape(-1, 4, 4)
    for window in sliding_window_diag:
        diag1 = np.diagonal(window)
        diag2 = np.diagonal(np.rot90(window))
        if np.all(diag1 == horizontal_matrix) or np.all(diag1 == inv_horizontal_matrix):
            diagonal_count += 1
        if np.all(diag2 == horizontal_matrix) or np.all(diag2 == inv_horizontal_matrix):
            diagonal_count += 1
    print("Diagonal count :", diagonal_count)
    
    print("Total count :", vertical_count + horizontal_count + diagonal_count)
    
    # PART 2 
    
    sliding_window_x = np.lib.stride_tricks.sliding_window_view(matrix_puzzle, (3, 3)).reshape(-1, 3, 3)
    print(sliding_window_x.shape)
    
    count_x = 0
    for window in sliding_window_x:
        diag1 = np.diagonal(window)
        diag2 = np.diagonal(np.rot90(window))
        matrix_to_check = np.concatenate((diag1, diag2))
        if np.all(matrix_to_check == pattern_x1) or np.all(matrix_to_check == pattern_x2):
            count_x += 1
        if np.all(matrix_to_check == pattern_x3) or np.all(matrix_to_check == pattern_x4):
            count_x += 1
    print("Count X :", count_x)
    
    
    