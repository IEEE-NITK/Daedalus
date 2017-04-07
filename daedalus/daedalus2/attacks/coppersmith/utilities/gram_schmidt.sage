def projection(v_k,u_k):
	coefficient = (u_k.inner_product(v_k)/u_k.inner_product(u_k))
	return coefficient*u_k
def projection_sum(v_k, Sdash):
	sum = vector(QQ, {len(v_k)-1:0})
	for u_k in Sdash:
		sum = sum + projection(v_k,u_k)
	return sum
def gram_schmidt(S):
	S_dash=[]
	for v_k in S:
		S_dash.append(v_k - projection_sum(v_k,S_dash))
	return S_dash

