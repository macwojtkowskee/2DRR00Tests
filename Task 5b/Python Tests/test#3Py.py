import random as random
import numpy as np
import time

#Test #3: Looping over dot-product.

#Start the timer.
t = time.time()

n = 19888 #Set vector size.
random_vector1 = np.random.rand(n, 1) #Generate the first matrix.
random_vector2 = np.random.rand(n, 1) #Generate the second matrix.

#Ensuring both vectors are dense.
random_vector1[random_vector1 == 0] = np.random.rand()
random_vector2[random_vector2 == 0] = np.random.rand()

#Creating a loop for dot product operations.
for i in range(10**6):
    np.vdot(random_vector1, random_vector2)

elapsed_time = time.time() - t

print(n) #for ease of measuring.
print(elapsed_time)