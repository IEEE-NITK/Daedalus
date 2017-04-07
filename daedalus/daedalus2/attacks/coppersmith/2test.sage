load("coppersmith_method.sage")
p  = 1379321
q  = 1571023
n  = p*q
e  = 5
d  = 197314381133
M  = 612301
for i in range(-10,10):
	MA = M + i
	C  =  384635054622
	R.< x > = ZZ [ ]
	f = ( MA + x ) ^ e - C
	print i
	print coppersmith(f , p *q , 0.01 , True)

