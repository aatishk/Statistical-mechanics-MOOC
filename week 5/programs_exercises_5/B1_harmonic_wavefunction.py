import math, pylab

n_states = 40
Energies = [0.5 + i for i in range(n_states)]
grid_x = [i * 0.2 for i in range(-25, 26)]
psi = {}
for x in grid_x:
    psi[x] = [math.exp(-x ** 2 / 2.0) / math.pi ** 0.25]
    psi[x].append(math.sqrt(2.0) * x * psi[x][0])
    for n in range(2, n_states+1):
        psi[x].append(math.sqrt(2.0 / n) * x * psi[x][n - 1] - math.sqrt((n - 1.0) / n) * psi[x][n - 2])

beta = 2

#Method a
Za = sum(math.exp(-beta * (n+0.5)) for n in range(n_states))
print 'Za =', Za

#Method b
Zb = 0
for n in range(n_states):
	sum = 0
	# Use trapezoidal rule to find the integral
	for x in grid_x:
		sum += psi[x][n+1]**2+psi[x][n]**2
	
	psi_sq = (0.2/2) * sum
	Zb += math.exp(-beta * (n+0.5)) * psi_sq
print 'Zb =', Zb

#Method c
Zc = 1/(2*math.sinh(beta/2.0))
print 'Zc =', Zc

constant = 1/Zb
print 'constant =', constant

pi_list = []
pi_list_exact = []

for x in grid_x:
	rho = 0
	for n in range(n_states):
		rho += math.exp(-beta * (n+0.5)) * psi[x][n] ** 2

	pi_list.append(constant * rho)
	pi_list_exact.append(math.sqrt(math.tanh(beta/2.0)/math.pi) * math.exp(-x**2 * math.tanh(beta/2.0)))


pylab.plot(grid_x, pi_list, 'o', label='density function')
#pylab.plot(grid_x, pi_list_exact, ':k')
pylab.title('$\pi(x)\ for\ Harmonic\ Oscillator\ [\\beta = 2]$')
pylab.xlabel('$x$')
pylab.ylabel('$\pi(x)$')
pylab.legend()
pylab.grid()
pylab.savefig("Probability_all.png")	
pylab.show()


