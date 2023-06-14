#!/usr/bin/python3
# function that computes the square value of all integers of a matrix.

def square_matrix_simple(matrix=[]):
    for row in matrix:
        matrix[row] ** 2
        
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)