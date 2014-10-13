import math, random, pylab

def V(x):
    pot =  x ** 2 / 2 + cubic * x ** 3 + quartic * x ** 4
    return pot
    
def levy_free_path(xstart, xend, dtau, N):
    x = [xstart]
    for k in range(1, N):
        dtau_prime = (N - k) * dtau
        x_mean = (dtau_prime * x[k - 1] + dtau * xend) / (dtau + dtau_prime)
        sigma = math.sqrt(1.0 / (1.0 / dtau + 1.0 / dtau_prime))
        x.append(random.gauss(x_mean, sigma))
        wrap = random.randint(0, N - 1)
        x = x[wrap:] + x[:wrap]
    return x

def levy_harmonic_path(xstart, xend, dtau, N):
    x = [xstart]
    for k in range(1, N):
        dtau_prime = (N - k) * dtau
        Ups1 = 1.0 / math.tanh(dtau) + 1.0 / math.tanh(dtau_prime)
        Ups2 = x[k - 1] / math.sinh(dtau) + xend / math.sinh(dtau_prime)
        x.append(random.gauss(Ups2 / Ups1, 1.0 / math.sqrt(Ups1)))
        wrap = random.randint(0, N - 1)
        x = x[wrap:] + x[:wrap]
    return x

def rho_free(x, y, beta):
    return math.exp(-(x - y) ** 2 / (2.0 * beta))

beta = 20.0
N = 100
dtau = beta / N
n_steps = 100000

cubic = -1
quartic = 1

for LevyType in range(2):
	acc = 0
	data = []
	x = [1.0] * N
	
	if LevyType == 0:
		Weight_old = math.exp(sum(-V(a) * dtau for a in x))
	else:
		Weight_old = math.exp(sum(-(V(a) - a ** 2 / 2.0) * dtau for a in x))
	
	for step in range(n_steps):
		if LevyType == 0:
			Ncut = random.randint(0,N/2)
			x_new = levy_free_path(x[0], x[Ncut], dtau, Ncut) + x[Ncut:]
			Weight_new = math.exp(sum(-V(a) * dtau for a in x_new))
		else:
			Ncut = random.randint(0,N/2)
			x_new = levy_harmonic_path(x[0], x[Ncut], dtau, Ncut) + x[Ncut:]
			Weight_new = math.exp(sum(-(V(a) - a ** 2 / 2.0) * dtau for a in x_new))
		
		if random.uniform(0.0, 1.0) < Weight_new / Weight_old:
			x = x_new[:]
			acc += 1
			Weight_old = Weight_new
        
		if step % 10 == 0:
			k = random.randint(0, N - 1)
			data.append(x[k])

	print 'LevyType =', LevyType, 'acc_ratio = ', acc/float(n_steps)
	if LevyType == 0:
		mylabel = 'Free Levy'
	else:
		mylabel = 'Harmonic Levy'
	pylab.hist(data, bins=50, normed=True, label=mylabel, histtype='step')

pylab.xlabel('$x$')
pylab.ylabel('$\\pi(x)$ (normalized)')
pylab.axis([-3.0, 3.0, 0.0, 1.0])
pylab.legend()
ProgType = 'free_and_harmonic_Levy'
pylab.title(ProgType + ' $\\beta$ = ' + str(beta) + ', dtau = ' + str(dtau) + ', Nsteps = '+ str(n_steps))
pylab.savefig(ProgType + str(beta) + '.png')
pylab.show()