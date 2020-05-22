#!/usr/bin/python3
"""
Divides all elements of a Matrix
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix
    matrix -- Recives the Matrix
    div -- Receives the number to divide
    Return:
    A new Matrix
    """
    new_matrix = []
    row_check = 0

    if not any(matrix):
        raise TypeError("matrix must be a matrix (list of lists) of\
 integers/floats")
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of\
 integers/floats")

    """
    the length of the lines is evaluated
    """
    if matrix[0] is not None:
        row_check = len(matrix[0])
        """
        it is evaluated if div receives an integer or float
        """
    if type(div) is not int and type(div) is not float:
        raise TypeError("must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    for rows in matrix:
        """
        a new row is created containing each row
        """
        new_row = []
        if type(rows) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of\
            integers/floats")
        if len(rows) != row_check:
            raise TypeError("Each row of the matrix must have the same size")
        for num_colum in rows:
            """
            it is evaluated if the matrix contains int or float
            """
            if type(num_colum) is not int and type(num_colum) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of\
 integers/floats")
            """
            division is made and saved in the matrix containing the rows
            """
            new_row.append(round(num_colum/div, 2))
        new_matrix.append(new_row)
    return new_matrix
