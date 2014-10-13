import random, math, pylab

def markov_pi(N, delta): 
	x, y = 1.0, 1.0
	n_hits = 0
	for i in range(N):
		del_x, del_y = random.uniform(-delta, delta), random.uniform(-delta, delta)
		if abs(x + del_x) < 1.0 and abs(y + del_y) < 1.0:
			x, y = x + del_x, y + del_y
		if x**2 + y**2 < 1.0: 
			n_hits += 1
	return n_hits

n_runs = 500
n_trials = 1000

deltas_list=[]
sigmas=[]

for deltax10 in range(1,51):
	delta = deltax10/float(10)
	deltas_list.append(delta)

	sigma = 0.0
	for run in range(n_runs):
		pi_est = 4.0 * markov_pi(n_trials, delta) / float(n_trials)
		sigma += (pi_est - math.pi) ** 2
	sigmas.append(math.sqrt(sigma/float(n_runs)))

pylab.plot(deltas_list, sigmas, 'o')
pylab.xlabel('$\delta$')
pylab.ylabel('$\sigma$')
pylab.title('Markov chain: Standard deviation $\sigma$ as a function of $\delta$')
pylab.savefig('markov_chain_stat_error.png')
pylab.show()