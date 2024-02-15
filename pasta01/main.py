#!/usr/bin/env python

import numpy as np
import time

# Generate random matrices
matrix1 = np.random.rand(1000, 1000)
matrix2 = np.random.rand(1000, 1000)

# Perform matrix multiplication and measure the time
start_time = time.time()
result = np.dot(matrix1, matrix2)
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

print(f"The matrix multiplication took {elapsed_time} seconds.")
