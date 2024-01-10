import random as random
import numpy as np
import time
from numpy import linalg

#Test #2: Computing eigenvalues.

#Start the timer.
t = time.time()

n = 2838 #Set matrix/vector size.
random_matrix = np.random.rand(n, n) #Generate a random matrix of the defined size.
random_vector = np.random.rand(n) #Generate a random vector of the same row-size as the matrix.

#Since our instruction notes that the vectors are 'dense', we make sure there are no 0's.
random_matrix[random_matrix == 0] = np.random.rand()
random_vector[random_vector == 0] = np.random.rand()

linalg.eig(random_matrix)
elapsed_time = time.time() - t

print(n) #for ease of measuring.
print(elapsed_time)