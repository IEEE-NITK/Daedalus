N = 90581
e = 17993

continued_fraction =  continued_fraction(e/N)
convergents = []
for i in range(0,len(continued_fraction)):
    convergents.append([continued_fraction.denominator(i), continued_fraction.numerator(i)])
print convergents 


