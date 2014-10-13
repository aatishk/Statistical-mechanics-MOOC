import random, math

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

n_trials_list = [1, 10, 100, 1000, 10000, 100000, 1000000]

f = open('Monte_Carlo_errors.txt', 'w')
f.write('n_trials | <Vol1_s(20)> |  Error  | Vol1_s(20) (exact result)\n')
f.flush()

for n_trials in n_trials_list:
	print 'n_trials =', n_trials, 'starting'	

	sum_Vol1_s_20 = 0.0
	sum_Vol1_s_20_sq = 0.0
	
	for run in range(20):
		Vol1_s = []

		# 1d volume is 1.0 and 2d volume is 2.0
		Vol1_s.append(1.0)
		Vol1_s.append(2.0)

		for d in range(1, 20):
			Q_average = markov_pi (n_trials, d)
			Vol1_s.append(Vol1_s[d] * 2 * Q_average)
		
		sum_Vol1_s_20 += Vol1_s[20]
		sum_Vol1_s_20_sq += Vol1_s[20] ** 2.0
	
		print 'run = ', run+1, '/ 20 done'
	
	mean_Vol1_s_20 = sum_Vol1_s_20/20.0
	mean_Vol1_s_20_sq = sum_Vol1_s_20_sq/20.0
	
	error_Vol1_s_20 = math.sqrt( (mean_Vol1_s_20_sq - (mean_Vol1_s_20 ** 2.0))/20.0 )
	
	f.write(str(n_trials)+'\t'+str(mean_Vol1_s_20)+'\t'+str(error_Vol1_s_20)+'\t')
	f.write(str(Vol1_s_exact(20))+'\n')
	
	f.flush()
	print 'n_trials =', n_trials, 'done\n'
