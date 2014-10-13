import math, numpy, pylab

# V(x) function from preparation program 3
def V(x):
    pot =  x ** 2 / 2 + cubic * x ** 3 + quartic * x ** 4
    return pot
    
# Z function from preparation program 3
def Z(cubic, quartic, beta, n_max):
    Z = sum(math.exp(-beta * Energy(n, cubic, quartic)) for n in range(n_max + 1))
    return Z

def Znew(cubic, quartic, beta, n_max):
	sum = 0
	for n in range(n_max + 1):
		Z = math.exp(-beta * Energy(n, cubic, quartic))
		print 'n =', n, 'Z =', Z, 'E =', Energy(n, cubic, quartic), 'beta E =', 2.0*Energy(n, cubic, quartic)
		sum += Z
	print
	return sum
    
def Energy(n, cubic, quartic):
	return n + 0.5 - 15.0 / 4.0 * cubic **2 * (n ** 2 + n + 11.0 / 30.0) + 3.0 / 2.0 * quartic * (n ** 2 + n + 1.0 / 2.0)

    
def rho_free(x, xp, beta):
    return (math.exp(-(x - xp) ** 2 / (2.0 * beta)) / math.sqrt(2.0 * math.pi * beta))

def rho_aharmonic_trotter(grid, beta):
    return numpy.array([[rho_free(x, xp, beta) * numpy.exp(-0.5 * beta * (V(x) + V(xp))) for x in grid] for xp in grid])

x_max = 5.0
nx = 100
dx = 2.0 * x_max / (nx - 1)
grid_x = [i * dx for i in range(-(nx - 1) / 2, nx / 2 + 1)]
beta_tmp = 2.0 ** (-5)
beta     = 2.0

#print 'cubic \t quartic \t Z_a \t Z_b \t Z_c'

for int_cubic in range(0, 9):
	cubic = -0.1*int_cubic
	quartic = -1*cubic
	beta_tmp = 2.0 ** (-5)
	rho = rho_aharmonic_trotter(grid_x, beta_tmp)

	#for n in range(10):
	#	print 'Energy', n, cubic, quartic, Energy(n,  cubic, quartic)
	#print
	
	while beta_tmp < beta:
		rho_x_x = numpy.diag(rho)
		sum_rho_x_x = numpy.diag(rho_x_x).sum()
	
		#a. Use Z to calculate Partition function		
		Z_a = Z(cubic, quartic, beta_tmp, 5)

		#b. Use trapezoidal rule to calculate the integral from density
		Z_b = (2*sum_rho_x_x - rho_x_x[0] - rho_x_x[-1])*dx/2
	
		#c. Use analytical formula for comparison with simple harmonic oscillator  
		Z_c = 1/(2*math.sinh(beta_tmp/2))

		rho = numpy.dot(rho, rho)
		rho *= dx    
		beta_tmp *= 2.0
	
	if int_cubic == 5:
		rho_x_x_qc_0p5 = rho_x_x
		Z_b_qc_0p5 = Z_b
	
	print cubic, '\t', quartic, '\t', Z_a, '\t', Z_b, '\t', Z_c

# Part 2

constant = 1/Z_b_qc_0p5
print 'constant =', constant

normalized_rho_x_x = rho_x_x_qc_0p5 * constant

f = open('matrix_squaring_beta_2.txt', 'w')
for k in range(len(grid_x)):
    f.write(str(grid_x[k]) + ' ' + str(normalized_rho_x_x[k]) + '\n')
f.close()

pylab.plot(grid_x, normalized_rho_x_x, 'o')
pylab.title('$\pi(x)\ for\ Anharmonic\ Oscillator\ [\\beta = 2,\ cubic = -quartic = -0.5]$')
pylab.xlabel('$x$')
pylab.ylabel('$\pi(x)$')
pylab.grid()
pylab.savefig("Probability_trotter2.png")	
pylab.show()


 
