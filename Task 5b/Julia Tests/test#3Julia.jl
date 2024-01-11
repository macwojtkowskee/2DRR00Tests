using Random
using BenchmarkTools
using LinearAlgebra

# Test #3: Looping over dot-product.

# Start the timer.
t = time()

n = 19888 # Set vector size.
random_vector1 = rand(n, 1) # Generate the first vector.
random_vector2 = rand(n, 1) # Generate the second vector.

# Ensuring both vectors are dense.
random_vector1[findall(random_vector1 .== 0)] .= rand()
random_vector2[findall(random_vector2 .== 0)] .= rand()

# Creating a loop for dot product operations.
for i in 1:10^6
    LinearAlgebra.dot(random_vector1, random_vector2)
end

elapsed_time = time() - t

println(n) # for ease of measuring.
println(elapsed_time)
