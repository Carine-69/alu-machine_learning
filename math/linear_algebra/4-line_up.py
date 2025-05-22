#!/usr/bin/env python3
"""

"""

def add_arrays(arr1, arr2):
    if len(arr1) != len(arr2):
        raise ValueError("arrays must have same length")
    return [x+y for x,y in zip(arr1, arr2)]

arr1 = [1,2,3,4]
arr2 = [5,6,7,8]
print(add_arrays(arr1, arr2))
        
