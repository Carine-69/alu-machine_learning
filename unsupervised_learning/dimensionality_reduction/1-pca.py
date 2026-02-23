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
    X_mean = X - np.mean(X, axis=0)
    _, _, Vt = np.linalg.svd(X_mean)
    W = Vt[:ndim].T
    T = X_mean @ W

    return T