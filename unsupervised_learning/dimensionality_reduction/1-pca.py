#!/usr/bin/env python3
"""PCA v2 module"""
import numpy as np


def pca(X, ndim):
    """Performs PCA on a dataset reducing to ndim dimensions.

    Args:
        X: numpy.ndarray of shape (n, d)
        ndim: new dimensionality

    Returns:
        T: numpy.ndarray of shape (n, ndim)
    """
    X_m = X - np.mean(X, axis=0)
    U, s, Vh = np.linalg.svd(X_m)
    W = Vh[:ndim].T
<<<<<<< HEAD
    return np.matmul(X_m, W)
=======
    return np.matmul(X_m, W)
>>>>>>> 1dda5fc1366d665f9a61058724fed1a438d2f4e4
