def coppersmith (f , N , epsilon=0.001 , fastLLL=False, debug=False ) :
	if epsilon > 1 / 7.0 or epsilon <= 0 :
		print ( " invalid epsilon " )
		return None
	f.change_ring ( Integers ( N ) )
	delta=f.degree ( )
	m=ceil ( 1 /(delta* epsilon) )
	R.< x >=ZZ [ ]
	# construction of the g [i , j ]( x )
	g=[]
	for j in range (0 , delta ) :
		g.append ( [ ] )
		for i in range (1 , m + 1 ) :
			g [ j ].append ( x ^ j * N ^ ( i ) * f ^ ( m - i ) )
 	X=ceil ( 0.5 * N ^ ( 1 / delta - epsilon ) )
	if debug : print ( " X=" + str ( X ) )
	size=m * delta
	# construct B from g [i , j ]( X * x )
	B=matrix ( ZZ , size , size )
	compteur=0

	for i in range ( - m +1 , 1 ) :
		for j in range (0 , delta ) :
			polylist=g [ j ] [ - i ] ( X * x ).list ( )
			vector=[ 0 ] * size
			vector [ 0 : len ( polylist ) ]=polylist
			vector.reverse ( )
			B.set_column ( compteur , vector )
			compteur=compteur + 1
	if debug : show ( B )
	if debug : print " LLL starts "
	coeffs=[ ]
	coeffs = B.transpose ( ).LLL( ).transpose ( ).column ( 0 ).list ( )
	coeffs.reverse ( )
	g=0*x
	for i in range (0 , size ) :
		g=g + Integer ( coeffs [ i ] / X ^ i ) * x ^ i
	roots=g.roots ( multiplicities=False )
	result=[ ]

	for i in range (0 , len ( roots ) ) :
		if gcd (N , f ( roots [ i ] ) ) >=N :
			result.append ( roots [ i ] )
	return result

R.< x >=ZZ [ ]
f=( x - 1 ) * ( x - 2 ) * ( x - 3 ) * ( x - 4 ) * ( x - 40 )
print coppersmith (f , 10000 )
