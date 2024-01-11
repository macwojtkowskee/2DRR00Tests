import random as random
import numpy as np
import time

#Test #1: Solving a linear system.

#Start the timer.
t = time.time()

n = 1 #Set matrix/vector size.
random_matrix = np.random.rand(n, n) #Generate a random matrix of the defined size.
random_vector = np.random.rand(n) #Generate a random vector of the same row-size as the matrix.

#Since the instruction notes that the vectors are 'dense', we make sure there are no 0's.
random_matrix[random_matrix == 0] = np.random.rand()
random_vector[random_vector == 0] = np.random.rand()

#Establish a linear system solution.
b = np.linalg.solve(random_matrix,random_vector)
elapsed_time = time.time() - t

print(n) #for ease of measuring.
print(elapsed_time)