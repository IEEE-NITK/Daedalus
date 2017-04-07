function reduced_basis = LLL(lattice_basis)
	[orthogonal_basis, mu] = gram_schmidt(lattice_basis)
	n = size(lattice_basis)(2)
	w=1 
	while w<n
		[lattice_basis,mu] = size_reduce(w,lattice_basis,mu)
		[orthogonal_basis, mu] = gram_schmidt(lattice_basis)
		check = lovasz_condition(orthogonal_basis(:,w+1),orthogonal_basis(:,w),mu(w,w+1))
		if(check == 1)
			w = w+1
		else
			temp = lattice_basis(:,w)
			lattice_basis(:,w) = lattice_basis(:,w+1)
			lattice_basis(:,w+1) = temp
			[orthogonal_basis,mu] = gram_schmidt(lattice_basis)
			w = max(w-1,1)
		endif
	endwhile
	reduced_basis = lattice_basis
endfunction

function check = lovasz_condition(b_k,b_k1,mu)
	l1 = b_k'*b_k;
	l2 = b_k1'*b_k1;
	coeff = 0.75 - mu*mu
	check = 0
	if(l1>=coeff*l2)
		check = 1
	endif 
endfunction

