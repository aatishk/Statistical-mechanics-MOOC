import math, random, pylab

def levy_free_path(xstart, xend, dtau, N):
    x = [xstart]
    for k in range(1, N):
        dtau_prime = (N - k) * dtau
        x_mean = (dtau_prime * x[k - 1] + dtau * xend) / \
                 (dtau + dtau_prime)
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
N = 80
dtau = beta / N
n_steps = 100000
x = [1.0] * N
data = []
Weight_old = math.exp(sum(-a ** 2/ 2.0 * dtau for a in x))
acc = 0
for step in range(n_steps):
	Ncut = random.randint(0,N/2)
	x_new = levy_free_path(x[0], x[Ncut], dtau, Ncut) + x[Ncut:]
	Weight_new = math.exp(sum(-a ** 2/ 2.0 * dtau for a in x_new))
	
	if random.uniform(0.0, 1.0) < Weight_new / Weight_old:
		x = x_new[:]
		acc += 1
		Weight_old = Weight_new
        
	#print x
	if step % 10 == 0:
		k = random.randint(0, N - 1)
		data.append(x[k])

print 'acc_ratio = ', acc/float(n_steps)
pylab.hist(data, bins=50, normed=True, label='QMC')
x_values = [0.1 * a for a in range (-30, 30)]
y_values = [math.sqrt(math.tanh(beta / 2.0)) / math.sqrt(math.pi) * \
                  math.exp( - xx **2 * math.tanh( beta / 2.0)) for xx in x_values]
pylab.plot(x_values, y_values, label='exact')
pylab.xlabel('$x$')
pylab.ylabel('$\\pi(x)$ (normalized)')
pylab.axis([-3.0, 3.0, 0.0, 0.6])
pylab.legend()
ProgType = 'free_levy_harmonic_path'
pylab.title(ProgType + ' $\\beta$ = ' + str(beta) + ', dtau = ' + str(dtau) + ', Nsteps = '+ str(n_steps))
pylab.savefig(ProgType + str(beta) + '.png')
pylab.show()