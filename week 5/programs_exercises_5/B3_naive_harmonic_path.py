import math, random, pylab

def rho_free(x, y, beta):
    return math.exp(-(x - y) ** 2 / (2.0 * beta))

beta = 2.0
N = 8
dtau = beta / N
delta = 1.0
n_steps = 100000
x = [0.0] * N
x_list = []
for step in range(n_steps):
    k = random.randint(0, N - 1)
    knext, kprev = (k + 1) % N, (k - 1) % N
    x_new = x[k] + random.uniform(-delta, delta)
    old_weight  = (rho_free(x[knext], x[k], dtau) *
                   rho_free(x[k], x[kprev], dtau) *
                   math.exp(-0.5 * dtau * x[k] ** 2))
    new_weight  = (rho_free(x[knext], x_new, dtau) *
                   rho_free(x_new, x[kprev], dtau) *
                   math.exp(-0.5 * dtau * x_new ** 2))
    if random.uniform(0.0, 1.0) < new_weight / old_weight:
        x[k] = x_new
    
    if step % 10 == 0:
    	k = random.randint(0, N - 1)
    	x_list.append(x[k])

x_max = 5.0
nx = 100
dx = 2.0 * x_max / (nx - 1)
grid_x = [i * dx for i in range(-(nx - 1) / 2, nx / 2 + 1)]

pi_list_exact = []
for x in grid_x:
	pi_list_exact.append(math.sqrt(math.tanh(beta/2.0)/math.pi) * math.exp(-x**2 * math.tanh(beta/2.0)))
pylab.plot(grid_x, pi_list_exact, 'k--', label='Analytical', linewidth=1.5)

n, bins, patches=pylab.hist(x_list, bins=50, normed=1, histtype='stepfilled', label='Monte Carlo')
pylab.setp(patches, 'facecolor', 'g', 'alpha', 0.75)
pylab.title('$\pi(x)\ for\ Harmonic\ Oscillator\ [\\beta = 2]$')
pylab.xlabel('$x$')
pylab.ylabel('$\pi(x)$')
pylab.legend()
pylab.grid()
pylab.savefig("Probability_MC.png")	
pylab.show()