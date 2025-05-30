#!/usr/bin/env python3
def determinant(matrix):
    """
    Calculates the determinant of a square matrix.

    Parameters:
        matrix (list of lists): A square matrix (same number of rows and columns)

    Returns:
        float: The determinant of the matrix, rounded to 10 decimal places

    Raises:
        TypeError: If the input is not a list of lists
        ValueError: If the matrix is not square
    """

    
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    # Check if matrix is square: all rows must have the same length as the number of rows
    size = len(matrix)
    if any(len(row) != size for row in matrix):
        raise ValueError("matrix must be a square matrix")

    # Special case: 0x0 matrix (represented as [[]]) is defined to have determinant = 1
    if matrix == [[]]:
        return 1


    # Convert to NumPy array for matrix operations
    np_matrix = np.array(matrix)

    # Use NumPy's determinant function
    det = np.linalg.det(np_matrix)

    # Round result to 10 decimal places to avoid floating-point inaccuracies
    return round(det, 10)
