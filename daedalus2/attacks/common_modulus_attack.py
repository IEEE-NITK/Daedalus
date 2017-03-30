from sage.all import *

errors = []

def common_modulus_attack(inputs,results={}):
	#{'c1':"attacks/cm_c1",'c2':"attacks/cm_c2",'pubkey1':"attacks/cm_pubkey_1",'pubkey2':"attacks/cm_pubkey_2"}
	try:
		n1=inputs['N'][0]
		e1=inputs['E'][0]

		n2=inputs['N'][1]
		e2=inputs['E'][1]

		c1=inputs['C'][0]
		c2=inputs['C'][1]

		if(n1!=n2):
			globals()['errors'].append('Unable to implement common modulus attack.Modulii are different.')
		else:
			n=n1
			g,u,v=xgcd(e1,e2)

			result=(power_mod(c1,u,n)*power_mod(c2,v,n))%n
			results["common modulus attack"]=result
		
	except Exception as e:
		globals()['errors'].append(e)

	return {'errors': globals()['errors'], 'results': results}

# if __name__ == '__main__':
# 	a=common_modulus_attack()
# 	print a
