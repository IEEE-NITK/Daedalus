from sage.all import *

errors=[]

def hastad_simple(inputs,results={}):
	#={'key1':"attacks/key1",'key2':"attacks/key2",'key3':"attacks/key3",'c1':"attacks/c1",'c2':"attacks/c2",'c3':"attacks/c3"}
	
	try:

		n1=inputs['N'][0]
		e1=inputs['E'][0]

		n2=inputs['N'][1]
		e2=inputs['E'][1]

		n3=inputs['N'][2]
		e3=inputs['E'][2]



		if(e1!=e2 or e2!=e3):
			globals()['errors'].append("e values are not the same")
		else:
			e=e1

		c1=inputs['C'][0]
		c2=inputs['C'][1]
		c3=inputs['C'][2]

		if(gcd(n1,n2)!=1 or gcd(n2,n3)!=1 or gcd(n1,n3)!=1):
			globals()['errors'].append("The three public moduli are not coprime. Hence hastad attack not possible")
		else:
			#As gcd(n1,n2,n3)=1 and m^3 < n1*n2*n3, CRT can be applied to find m^3
			m_cubed=CRT_list([c1,c2,c3],[n1,n2,n3])
			# print "M^3 is ",m_cubed

			f=x**3-m_cubed
			roots=f.roots(multiplicities=False,ring=IntegerRing())
			# print "The message is ",roots[0]
			results['hastad simple attack']=roots
			if(len(roots) == 0):
				globals()['errors'].append('No solution found')

	except Exception as e:
		globals()['errors'].append(e)

	return {'errors': globals()['errors'], 'results': results}


# if __name__ == '__main__':
# 	a=simple_hastad()
# 	print a


