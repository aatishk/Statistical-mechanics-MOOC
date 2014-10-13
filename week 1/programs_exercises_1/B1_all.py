import random, pylab

def markov(N, delta): 
    x, y = 1.0, 1.0
    n_hits = 0
    for i in range(N):
        del_x, del_y = random.uniform(-delta, delta), random.uniform(-delta, delta)
        if abs(x + del_x) < 1.0 and abs(y + del_y) < 1.0:
			x, y = x + del_x, y + del_y
			n_hits += 1
    return n_hits

n_runs = 500
n_trials = 1000

acc_ratios=[]
deltas_list=[]

for deltax10 in range(1,51):
	delta = deltax10/float(10)
		
	for run in range(n_runs):
		acc_ratio= markov(n_trials, delta) / float(n_trials)
		acc_ratios.append(acc_ratio)
		deltas_list.append(delta)
		
#print deltas_list
#print ave_acc_ratios

pylab.plot(deltas_list, acc_ratios, 'o')
pylab.xlabel('$\delta$')
pylab.ylabel('Acceptance ratio')
pylab.title('Markov chain: Acceptance ratio as a function of $\delta$')
pylab.savefig('markov_chain_acc_ratios.png')
pylab.show()
