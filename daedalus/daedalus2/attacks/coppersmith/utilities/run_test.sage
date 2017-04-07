load("LLL_algorithm.sage")
runtimes = []
for i in range(0,10):
	runtimes.append(0.0)
	for k in range(0,1):
		r = 0
		while(r!=i+2):
			A = random_matrix(ZZ, i+2)
			r = A.rank()
		t = cputime()
		res = LLL(A)
		print A
		print "Hello World"
		print res
		runtimes[i] = runtimes[i] + cputime(t)*0.1
print(runtimes)
