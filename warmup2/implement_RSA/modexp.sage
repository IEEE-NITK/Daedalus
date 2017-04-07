def modexp(a, b, n):
	a_power_b_mod_n = 1
	for i in list(Integer.binary(b)):
		a_power_b_mod_n = mod(a_power_b_mod_n*a_power_b_mod_n, n)
		if(Integer(i)==1):
			a_power_b_mod_n = mod(a_power_b_mod_n*a, n)
	return Integer(a_power_b_mod_n)
