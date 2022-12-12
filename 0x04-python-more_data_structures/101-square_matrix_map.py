#!/usr/bin/python3

def square_matrix_map(matrix=[]):
    # square each element of a square matrix and return as square matrix
    return (list(map(lambda x: list(map(lambda y: y ** 2, x[:])), matrix)))
