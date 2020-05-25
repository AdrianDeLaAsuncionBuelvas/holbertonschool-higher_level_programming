#!/usr/bin/python3
"""
multiplies 2 matrices by using the module NumPy
"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):

    """
    lazy_matrix_mul -- function that multipli 2 matrices
    m_a -- matrix a
    m_b -- matrix b
    """

    return np.matmul(m_a, m_b)
