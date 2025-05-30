#!/usr/bin/env python3
def determinant(matrix):
    """
    Calculates the determinant of a square matrix.

    Parameters:
        matrix (list of lists): A square matrix represented as a list of lists.

    Returns:
        float: The determinant of the matrix, rounded to avoid floating-point errors.

    Raises:
        TypeError: If the input is not a list of lists.
        ValueError: If the matrix is not square.
    """

    # Check that the input is a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    # Check that the matrix is square (rows and columns are equal)
    if any(len(row) != len(matrix) for row in matrix):
        raise ValueError("matrix must be a square matrix")

    # Handle 0x0 matrix (defined as determinant = 1)
    if matrix == [[]]:
        return 1

    # Convert the matrix to a NumPy array and calculate the determinant
    # Round the result to avoid floating-point inaccuracies
    return round(np.linalg.det(np.array(matrix)), 10)
