import random, pylab, math

def Vol1_s(dimension):
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
d = 200
Q_average = markov_pi (n_trials, d)

print d, 2 * Q_average, Vol1_s(d + 1) / Vol1_s(d)


