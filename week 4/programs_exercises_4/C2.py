import random, pylab, math

def Vol1_s_exact(dimension):
    return math.pi ** (dimension / 2.0)/ math.gamma(dimension / 2.0 + 1.0)
    
def markov_pi (N,d):
	x = [0.0] * d
	radius_sq = 0.0
	sum_Q = 0

	for i in range(n_trials):		
		k = random.randint(0, d - 1)
		x_new_k = x[k] + random.uniform(-1.0, 1.0)
		radius_sq_new = radius_sq - (x[k] ** 2.0) + (x_new_k ** 2.0)

		if radius_sq_new < 1:
			x[k] = x_new_k
			radius_sq = radius_sq_new
		
		x_supp = random.uniform(-1.0, 1.0)
		if radius_sq + x_supp ** 2 < 1:
			sum_Q +=1 		
	
	return (float(sum_Q)/float(N))

n_trials = 1000000
# Volume of 1 dimensional sphere is 2.0
Vol1_s = []

# 1d volume is 1.0 and 2d volume is 2.0
Vol1_s.append(1.0)
Vol1_s.append(2.0)

for d in range(1, 200):
	Q_average = markov_pi (n_trials, d)
	print d, '/ 200 done'
	Vol1_s.append(Vol1_s[d] * 2 * Q_average) 

print 'Vol1_s(5) estim = ', Vol1_s[5]
print 'Vol1_s(5) exact = ', Vol1_s_exact(5)

print 'Vol1_s(200) estim = ', Vol1_s[200]
print 'Vol1_s(200) exact = ', Vol1_s_exact(200)

pylab.plot(range(0,201), Vol1_s, ':k')
pylab.plot(range(0,201), Vol1_s)
pylab.xlabel('dimension')
pylab.ylabel('Vol1_s from acccordian')
pylab.yscale('log')
pylab.grid()
pylab.title('Volume of hypersphere as function of dimension')
pylab.savefig('Vol1_s_accordion.png')
pylab.show()



