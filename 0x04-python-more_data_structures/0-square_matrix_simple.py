#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    square = 0
    for i in matrix:
            square = [j**2 for j in i]
            new_matrix.append(square)
    return (new_matrix)
