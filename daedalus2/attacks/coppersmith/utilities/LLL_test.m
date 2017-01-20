function reduced_basis = LLL_test(basis)
	m = size(basis)(2)
	u = zeros(m,m)
	orthogonal_basis = zeros(m,m)
	for i=1:m
		u(i,:) = zeros(1,m)
		u(i,i) = 1
		orthogonal_basis(:,i) = basis(:,i)
		for j=1:i-1
			u(j,i) = (basis(:,i)'*orthogonal_basis(:,j))/(orthogonal_basis(:,j)'*orthogonal_basis(:,j))
			orthogonal_basis(:,i) = orthogonal_basis(:,i) - u(j,i)*orthogonal_basis(:,j)
		endfor
		[basis,u] = reduce(i,basis,u)
	endfor
	i = 1
	while(i<m)
		c= 4/3
		if((basis(:,i)'*basis(:,i)) <= c*(basis(:,i+1)'*basis(:,i+1)))
			i = i+1
		else
			orthogonal_basis(:,i+1) = orthogonal_basis(:,i+1) + u(i,i+1)*orthogonal_basis(:,i)
			u(i,i) = (basis(:,i)'*orthogonal_basis(:,i+1))/(orthogonal_basis(:,i+1)'*orthogonal_basis(:,i+1))
			u(i+1,i) = 1 
			u(i,i+1) = 1 
			orthogonal_basis(:,i) = orthogonal_basis(:,i) - u(i,i)*orthogonal_basis(:,i+1)
			temp = u(:,i)
			u(:,i) = u(:,i+1)
			u(:,i+1) = temp 
			temp = orthogonal_basis(:,i)
			orthogonal_basis(:,i) = orthogonal_basis(:,i+1)
			orthogonal_basis(:,i+1) = temp 
			temp = basis(:,i)
			basis(:,i) = basis(:,i+1)
			basis(:,i+1) = temp 
			for k=1+2:m
				u(i,k) = (basis(:,k)'*orthogonal_basis(:,i))/(orthogonal_basis(:,i)'*orthogonal_basis(:,i))
				u(i+1,k) = (basis(:,k)'*orthogonal_basis(:,i+1))/(orthogonal_basis(:,i+1)'*orthogonal_basis(:,i+1))
			endfor
			if(abs(u(i,i+1))>0.5)
				[basis,u] = reduce(i+1,basis,u)
			endif
			i = max(i-1,1)
		endif
	endwhile
	reduced_basis = basis
endfunction

function [r_basis,u] = reduce(i,basis,u)
	j = i-1
	while(j>0)
		basis(:,i) = basis(:,i) - round(u(j,i))*basis(:,j)
		u(:,i) = u(:,i) - round(u(j,i))*u(:,j)
		j = j-1
	endwhile
	r_basis = basis
endfunction



