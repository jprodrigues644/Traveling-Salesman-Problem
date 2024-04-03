import random
from utils import calculate_cost, generate_random_solution
#Question 1
def load_instance(file_path):
    dimension = 0
    matrix = []

    def read_dimension(line):
        nonlocal dimension
        dimension = int(line.split(":")[1])

    def read_edge_weights(lines, start_index):
        nonlocal dimension, matrix
        matrix = [[9999] * dimension for _ in range(dimension)]
        for i in range(dimension):
            row_values = lines[start_index + i].split()
            for j in range(dimension):
                if i != j:
                    matrix[i][j] = int(row_values[j])

    with open(file_path, 'r') as file:
        lines = file.readlines()

        for line in lines:
            if line.startswith("COMMENT") or line.strip() == "":
                continue

            if line.startswith("DIMENSION"):
                read_dimension(line)

            if line.startswith("EDGE_WEIGHT_SECTION"):
                read_edge_weights(lines, lines.index(line) + 1)

    return dimension, matrix

def load_symmetric_matrix(file_path):
    dimension = 0
    matrix = []

    def read_dimension(line):
        nonlocal dimension
        dimension = int(line.split(":")[1])

    def read_edge_weights(lines, start_index):
        nonlocal dimension, matrix
        matrix = [[9999] * dimension for _ in range(dimension)]
        for i in range(dimension):
            row_values = lines[start_index + i].split()
            for j in range(i, dimension):
                if i != j:
                    matrix[i][j] = int(row_values[j - i])
                    matrix[j][i] = matrix[i][j]

    with open(file_path, 'r') as file:
        lines = file.readlines()

        for line in lines:
            if line.startswith("COMMENT") or line.strip() == "":
                continue

            if line.startswith("DIMENSION"):
                read_dimension(line)

            if line.startswith("EDGE_WEIGHT_SECTION"):
                read_edge_weights(lines, lines.index(line) + 1)

    return dimension, matrix









     
     
    
    

    
   
         
         
     
    