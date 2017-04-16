def partial_key_exposure(input):

	N = input['N']
	qbar = input['qbar']
	F.<x> = PolynomialRing(Zmod(N), implementation='NTL')
	pol = x - qbar
	dd = pol.degree()

	beta = 0.5
	epsilon = beta/7
	mm = ceil(beta**2/(dd*epsilon))
	tt = floor(dd*mm*((1/beta)-1))
	XX = ceil(N**((beta**2/dd)-epsilon))

	roots = coppersmith_howgrave_univariate(pol, N, beta, mm, tt, XX)
	for root in roots:
		if(root == qbar):
	
			roots.remove(root)
	result = {}
	result['results'] = roots
	result['errors']  = 'No error'
	if(len(roots) == 0):
		result['errors'] = 'No solution found'
	return result
	
