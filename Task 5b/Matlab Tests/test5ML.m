% Start the timer.
t = tic;

% Set matrix size.
n = 1476;
m = 2297;

random_matrix = rand(m, n);
random_vector = rand(m, 1);

% Least-squares problem 
lscov(random_matrix, random_vector);

elapsed_time = toc(t);

disp([n, m]);
disp(elapsed_time);