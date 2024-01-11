using LinearAlgebra

#Test #1

#Start the timer
t = time() 

n = 1 #Set size.

random_matrix = rand(n, n) # Generate a random n x n matrix 
random_vector = rand(n) # Generate a random n x 1 vector

# Ensure that both A and b do not contain any zeros
random_matrix[random_matrix .== 0] .= rand()  
random_vector[random_vector .== 0] .= rand()  

#Solving the linear system:
random_matrix \ random_vector

elapsed_time = time() - t

println(n) #this is just for the sake of convenience.
println(elapsed_time)