#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # square each element of a square matrix and return as square matrix
    sqd = [[elem*elem for elem in inner] for inner in matrix]
    return sqd
