function reduced_basis = LLL_wiki(lattice_basis)
	[Q,R] = qr(lattice_basis)
	k = 1
	while(k<=size(lattice_basis)(2))
		for j=k:-1:1
			j
			if(abs(R(k,j))>0.5)
				lattice_basis(:,k) = lattice_basis(:, k) - round(R(k,j))*lattice_basis(:, j)
				Q,R = qr(lattice_basis);
			endif
		endfor
	endwhile
	lattice_basis
endfunction
