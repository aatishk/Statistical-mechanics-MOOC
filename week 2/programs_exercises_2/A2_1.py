import random, pylab

def markov_disks_box(L, sigma):
	for steps in range(n_steps):
		a = random.choice(L)
		b = [a[0] + random.uniform(-delta, delta), a[1] + random.uniform(-delta, delta)]
		min_dist = min((b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2 for c in L if c != a)
		box_cond = min(b[0], b[1]) < sigma or max(b[0], b[1]) > 1.0 - sigma
		if not (box_cond or min_dist < 4.0 * sigma ** 2):
			a[:] = b    
	return L

L = [[0.25, 0.25], [0.75, 0.25], [0.25, 0.75], [0.75, 0.75]]
sigma = 0.1197
delta = 0.1
N = 4
n_steps = 200

n_runs = 1000000
histo_data = []
for run in range(n_runs):
    pos = markov_disks_box(L, sigma)
    for k in range(N): histo_data.append(pos[k][0])

pylab.hist(histo_data, bins=100, normed=True)
pylab.xlabel('x')
pylab.ylabel('frequency')
pylab.title('Probability distribution - Markov Disks Box')
pylab.grid()
pylab.savefig('markov_disks_histo.png')
pylab.show()

