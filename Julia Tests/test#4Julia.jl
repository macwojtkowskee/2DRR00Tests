using Random
using BenchmarkTools
using LinearAlgebra

# Test #3: Looping over multiplication.

# Start the timer.
t = time()

# Set matrix size.
n = 50
m = 42

random_matrix1 = rand(m, n) # Generate the first matrix.
random_matrix2 = rand(n, m) # Generate the second matrix.

# Ensuring both matrixs are dense.
random_matrix1[findall(random_matrix1 .== 0)] .= rand()
random_matrix2[findall(random_matrix2 .== 0)] .= rand()

# Creating a loop for multiplication operations.
for i in 1:10^6
    random_matrix1 * random_matrix2
end

elapsed_time = time() - t

println(n, "x", m) # for ease of measuring.
println(elapsed_time)
