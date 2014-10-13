import math, numpy, pylab

def rho_free(x, xp, beta):
    return (math.exp(-(x - xp) ** 2 / (2.0 * beta)) /
            math.sqrt(2.0 * math.pi * beta))

def rho_harmonic_trotter(grid, beta):
    return numpy.array([[rho_free(x, xp, beta) * \
                         numpy.exp(-0.5 * beta * 0.5 * (x ** 2 + xp ** 2)) \
                         for x in grid] for xp in grid])

x_max = 5.0
nx = 100
dx = 2.0 * x_max / (nx - 1)
grid_x = [i * dx for i in range(-(nx - 1) / 2, nx / 2 + 1)]
beta_tmp = 2.0 ** (-5)
beta     = 2.0 ** (3)
rho = rho_harmonic_trotter(grid_x, beta_tmp)
print 'Beta \t Z_a \t Z_b'

while beta_tmp < beta:
    rho_x_x = numpy.diag(rho)
    sum_rho_x_x = numpy.diag(rho_x_x).sum()
    
	# Part 1
    #Use trapezoidal rule to calculate the integral from density
    Z_a = (2*sum_rho_x_x - rho_x_x[0] - rho_x_x[-1])*dx/2
    
    #Use analytical formula   
    Z_b = 1/(2*math.sinh(beta_tmp/2))

    rho = numpy.dot(rho, rho)
    rho *= dx    
    beta_tmp *= 2.0
    print beta_tmp,'\t',Z_a, '\t', Z_b

# Part 2
# Last iteration stored the density (rho_x_x) for beta = 8

constant = 1/Z_a
print 'constant =', constant

normalized_rho_x_x = rho_x_x * constant

pi_list_exact = []
for x in grid_x:
	pi_list_exact.append(math.sqrt(math.tanh(beta/2.0)/math.pi) * math.exp(-x**2 * math.tanh(beta/2.0)))

pylab.plot(grid_x, normalized_rho_x_x, 'o', label='Trotter')
pylab.plot(grid_x, pi_list_exact, ':k', label='exact')
pylab.title('$\pi(x)\ for\ Harmonic\ Oscillator\ [\\beta = 8]$')
pylab.xlabel('$x$')
pylab.ylabel('$\pi(x)$')
pylab.legend()
pylab.grid()
pylab.savefig("Probability_trotter.png")	
pylab.show()


 