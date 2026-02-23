#!/usr/bin/env python3
"""PCA module"""
import numpy as np


def pca(X, var=0.95):
    """Performs PCA on a dataset maintaining var fraction of variance.

    Args:
        X: numpy.ndarray of shape (n, d) with zero mean dimensions
        var: fraction of variance to maintain

    Returns:
        W: weights matrix, shape (d, nd)
    """
    U, s, Vh = np.linalg.svd(X)
    cumvar = np.cumsum(s ** 2) / np.sum(s ** 2)
    nd = np.argmax(cumvar >= var) + 1
    W = Vt[:nd].T

    return W