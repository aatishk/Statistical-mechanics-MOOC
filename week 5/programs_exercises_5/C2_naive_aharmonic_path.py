import math, random, pylab

# V(x) function from preparation program 3
def V(x):
    pot =  x ** 2 / 2 + cubic * x ** 3 + quartic * x ** 4
    return pot
    
def rho_free(x, y, beta):
    return math.exp(-(x - y) ** 2 / (2.0 * beta))

cubic = -0.5
quartic = 0.5

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
                   math.exp(-1.0 * dtau * V(x[k])))
    new_weight  = (rho_free(x[knext], x_new, dtau) *
                   rho_free(x_new, x[kprev], dtau) *
                   math.exp(-1.0 * dtau * V(x_new)))
    if random.uniform(0.0, 1.0) < new_weight / old_weight:
        x[k] = x_new
    
    if step % 10 == 0:
    	k = random.randint(0, N - 1)
    	x_list.append(x[k])

filename = 'matrix_squaring_beta_2.txt'
f = open(filename, 'r')
x_sq_matrix = []
y_sq_matrix = []
for line in f:
    a, b = line.split()
    x_sq_matrix.append(float(a))
    y_sq_matrix.append(float(b))
f.close()

pylab.plot(x_sq_matrix, y_sq_matrix, 'o', label='Square Matrix', linewidth=1.5)

n, bins, patches=pylab.hist(x_list, bins=50, normed=1, histtype='stepfilled', label='Monte Carlo')
pylab.setp(patches, 'facecolor', 'g', 'alpha', 0.75)
pylab.title('$\pi(x)\ for\ Anharmonic\ Oscillator\ [\\beta = 2,\ cubic = -quatric = -0.5]$')
pylab.xlabel('$x$')
pylab.ylabel('$\pi(x)$')
pylab.legend()
pylab.grid()
pylab.savefig("Probability_MC2.png")	
pylab.show()
