function A = LLL_reduction(A,delta)
% LLL lattice reduction
% Matlab implementation by K. Shum
% The input A is a square matrix. Columns of input A are the basis vectors 
% The output A is a square matrix, whose columns are LLL-redcued basis
% vectors

if nargin == 1
    delta = .75; % the default value of the parameter delta
end

m = length(A); % the dimension of the vector space
B = zeros(m,m); % Columns of B are the vectors after the Gram-Schmidt process
mu = zeros(m,m); % The matrix mu stores the GS coefficients
M = zeros(1,m); % M(i) is the norm squared of the i-th column of B

% Gram-Schmidt orthogonalization
B(:,1) = A(:,1); % Set the first column of B as the same
 % as the first column of A
M(1) = dot(B(:,1), B(:,1));
for i = 2:m
    mu(i,1:(i-1)) = (A(:,i)'* B(:,1:(i-1))) ./ M(1:(i-1));
    B(:,i) = A(:,i) - B(:,1:(i-1))*mu(i,1:(i-1))';
    M(i) = dot(B(:,i), B(:,i));
end
mu*B
