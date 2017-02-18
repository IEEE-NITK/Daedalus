function [reduced_basis,mu] = size_reduce(basis,mu,i)
	reduced_basis = basis
	for j=i-1:-1:1;
		j
		if(abs(mu(j,i))>0.5)
			reduced_basis(:,i) = reduced_basis(:,i) - round(mu(j,i))*basis(:,j)
			mu(:,i) = mu(:,i) - round(mu(j,i))*mu(:,j)
		endif
	endfor
endfunction
