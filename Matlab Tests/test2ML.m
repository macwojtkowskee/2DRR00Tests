% Start the timer.
t = tic;

n = 2838; % Set matrix/vector size.
random_matrix = rand(n, n); % Generate a random matrix.
random_vector = rand(n, 1); % Generate a random vector.

random_matrix(random_matrix == 0) = rand;
random_vector(random_vector == 0) = rand;

eig(random_matrix);
elapsed_time = toc(t);

disp(n);
disp(elapsed_time);
