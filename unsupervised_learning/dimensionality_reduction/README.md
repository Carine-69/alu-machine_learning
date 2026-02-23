# Dimensionality Reduction

## Description

This project covers dimensionality reduction techniques including Principal Component Analysis (PCA) and t-distributed Stochastic Neighbor Embedding (t-SNE). These techniques are used to reduce the number of features in a dataset while preserving as much information as possible.

## Learning Objectives

- What is eigendecomposition?
- What is singular value decomposition?
- What is the difference between eig and svd?
- What is dimensionality reduction and what are its purposes?
- What is principal components analysis (PCA)?
- What is t-distributed stochastic neighbor embedding (t-SNE)?
- What is a manifold?
- What is the difference between linear and non-linear dimensionality reduction?
- Which techniques are linear/non-linear?

## Requirements

- Ubuntu 16.04 LTS
- Python 3.5
- NumPy 1.15
- pycodestyle 2.4

## Files

| File | Description |
|------|-------------|
| `0-pca.py` | PCA function that maintains a given fraction of variance |
| `1-pca.py` | PCA function that reduces data to a given number of dimensions |

## Usage

### Task 0 - PCA

```python
import numpy as np
pca = __import__('0-pca').pca

X = np.random.normal(size=(50, 6))
X_m = X - np.mean(X, axis=0)
W = pca(X_m, var=0.95)
T = np.matmul(X_m, W)
```

### Task 1 - PCA v2

```python
import numpy as np
pca = __import__('1-pca').pca

X = np.loadtxt("mnist2500_X.txt")
T = pca(X, 50)
```

## Data

- `mnist2500_X.txt` - MNIST dataset (2500 samples, 784 dimensions)
- `mnist2500_labels.txt` - Labels for the MNIST dataset