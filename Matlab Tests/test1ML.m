%Test #1:

% Start the timer.
tic;

n = 13181; % Set matrix/vector size.
random_matrix = rand(n, n); % Generate a random matrix.
random_vector = rand(1, n); % Generate a random vector.

% Since the instruction notes that the vectors are 'dense', we make sure there are no 0's.
random_matrix(random_matrix == 0) = rand;
random_vector(random_vector == 0) = rand;

% Establish a linear system solution.
b = linsolve(random_matrix, random_vector.');
elapsed_time = toc;

disp(n); %just to make sure.
disp(elapsed_time);

