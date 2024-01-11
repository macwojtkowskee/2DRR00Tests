% Start the timer.
t = tic;

% Set matrix size.
n = 47;
m = 44;

random_matrix1 = rand(m, n); % Generate the first matrix.
random_matrix2 = rand(n, m); % Generate the second matrix.

result_matrix = zeros(m, m);

% Ensuring both matrices are dense.
random_matrix1(random_matrix1 == 0) = rand;
random_matrix2(random_matrix2 == 0) = rand;

% Creating a loop for multiplying matrices.
for i = 1:10^6
    result_matrix = result_matrix + random_matrix1 * random_matrix2;
end

elapsed_time = toc(t); %end timer.

disp([n, m]); % for ease of measuring.
disp(elapsed_time);
