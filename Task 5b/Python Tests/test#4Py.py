import random as random
import numpy as np
import time

#Test #4: Looping over multiplication.

#Start the timer.
t = time.time()

#Set matrix size.
n = 50
m = 39

random_matrix1 = np.random.rand(m, n) #Generate the first matrix.
random_matrix2 = np.random.rand(n, m) #Generate the second matrix.

result_matrix = np.zeros((m, m)) #this should fix my problem, but i'm not sure about .zeros

#Ensuring both matrices are dense.
random_matrix1[random_matrix1 == 0] = np.random.rand()
random_matrix2[random_matrix2 == 0] = np.random.rand()

#Creating a loop for multiplying matrices.
for i in range(10**6):
    result_matrix += np.dot(random_matrix1, random_matrix2)

elapsed_time = time.time() - t

print(n, m) #for ease of measuring.
print(elapsed_time)