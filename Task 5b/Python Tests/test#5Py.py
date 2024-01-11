import numpy as np
import time

# Test #5: Least-squares

# Start the timer.
t = time.time()

# Set matrix size.
n = 4030
m = 4998

# Generate a random matrix with more rows than columns
random_matrix = np.random.rand(m, n)
random_vector = np.random.rand(m)

# Least-squares problem (i think this should be OK, according to numpy docs...)
np.linalg.lstsq(random_matrix, random_vector, rcond=None)

elapsed_time = time.time() - t

print(n, "x", m)
print(elapsed_time)