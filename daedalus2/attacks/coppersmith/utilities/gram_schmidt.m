function [orthogonal_basis, mu] = gram_schmidt(basis)
	n = size(basis)(1)
	orthogonal_basis = zeros(n,n)
	mu = zeros(n,n)
	orthogonal_basis(:,1) = basis(:,1)
	mu(1,1) = 1
	for i=2:n;
		orthogonal_basis(:,i) = basis(:,i)
		mu(i,i) = 1
		for j=1:i-1;
			mu(j,i) = (basis(:,i)'*orthogonal_basis(:,j))/(orthogonal_basis(:,j)'*orthogonal_basis(:,j))
			orthogonal_basis(:,i) = orthogonal_basis(:,i) - mu(j,i)*orthogonal_basis(:,j)
		endfor
	endfor
endfunction

