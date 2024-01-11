using Random
using LinearAlgebra
using BenchmarkTools

# Test #2: Computing eigenvalues.

# Start the timer.
t = time()

n = 2838 # Set size.

random_matrix = rand(n, n) # Generate a random matrix of the defined size.
random_vector = rand(n)    # Generate a random vector of the same row-size as the matrix.

# Since our instruction notes that the vectors are 'dense', we make sure there are no 0's.
random_matrix[findall(random_matrix .== 0)] .= rand()
random_vector[findall(random_vector .== 0)] .= rand()

eigvals(random_matrix)
elapsed_time = time() - t

println(n) 
println(elapsed_time)
