import random, pylab

def markov_pi (N,d):
	n_hits = 0
	x = [0.0] * d
	radius_sq = 0.0
	sum_radius_sq = 0.0
	x0_list= []
	x1_list=[]
	x0_list.append(x[0])
	x1_list.append(x[1])

	for i in range(n_trials):		
		k = random.randint(0, d - 1)
		x_new_k = x[k] + random.uniform(-1.0, 1.0)

		radius_sq_new = radius_sq - (x[k] ** 2.0) + (x_new_k ** 2.0)

		if radius_sq_new < 1:
			x[k] = x_new_k
			radius_sq = radius_sq_new
			sum_radius_sq += radius_sq
			n_hits += 1
		else:
			sum_radius_sq += radius_sq

		x0_list.append(x[0])
		x1_list.append(x[1])

	pylab.plot(x0_list, x1_list, 'o')
	pylab.xlabel('x0')
	pylab.ylabel('x1')
	pylab.grid()
	pylab.title('x0 vs x1 scatterplot')
	pylab.savefig('x0_x1_scatterplot.png')
	pylab.show()
	
	return (n_hits, sum_radius_sq)

n_trials = 1000000
d = 2
(n_hits, sum_radius_sq) = markov_pi(n_trials,d)
print 4.0 * n_hits / float(n_trials), sum_radius_sq / float(n_trials)


