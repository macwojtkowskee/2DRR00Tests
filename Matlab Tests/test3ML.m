% Start the timer.
t = tic;

n = 14710; % Set vector size.
random_vector1 = rand(n, 1); % Generate the first matrix.
random_vector2 = rand(n, 1); % Generate the second matrix.

% Ensuring both vectors are dense.
random_vector1(random_vector1 == 0) = rand;
random_vector2(random_vector2 == 0) = rand;

% Creating a loop for dot product operations.
for i = 1:10^6
    dot(random_vector1, random_vector2);
end

elapsed_time = toc(t);

disp(n); % for ease of measuring.
disp(elapsed_time);