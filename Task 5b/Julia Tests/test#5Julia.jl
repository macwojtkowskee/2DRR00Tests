using LinearAlgebra
using Random

# Test #5: Least-squares

# Start the timer.
t = time()

# Set matrix size.
n = 4030
m = 4998

# Generate a random matrix with more rows than columns
random_matrix = rand(m, n)
random_vector = rand(m)

# Least-squares problem
qr(random_matrix) \ random_vector

elapsed_time = time() - t

println(n,'x', m)
println(elapsed_time)
