function reduced_basis = LLL(basis)
	n = size(basis)(2)
	[U,mu] = gram_schmidt(basis)
	[basis, mu] = size_reduce(basis,mu,1)
	i = 1
	while(i<n)
		if(lovasz_condition(U(:,i),U(:,i+1),mu(i,i+1))==1)
			i = i+1
		else
			temp = basis(:,i)
			basis(:,i) = basis(:,i+1)
			basis(:,i+1) = temp
			[U,mu]= gram_schmidt(basis)
			[basis,mu] = size_reduce(basis,mu,i+1)
			i = max(i-1,1)
	
		endif
	endwhile
	reduced_basis=basis
endfunction

function decision = lovasz_condition(b1,b2,mu12)
	decision = 0
	if(0.75*(b1'*b1)<=(mu12*b1+b2)'*(mu12*b1+b2))
		decision = 1 
	endif
	endfunction
