import pylab, math, numpy

def V(x):
    pot =  x ** 2 / 2 + cubic * x ** 3 + quartic * x ** 4
    return pot

def Energy(n, cubic, quartic):
    return n + 0.5 - 15.0 / 4.0 * cubic **2 * (n ** 2 + n + 11.0 / 30.0) \
         + 3.0 / 2.0 * quartic * (n ** 2 + n + 1.0 / 2.0)

def Z(cubic, quartic, beta, n_max):
    Z = sum(math.exp(-beta * Energy(n, cubic, quartic)) for n in range(n_max + 1))
    return Z

cubic = -0.5
quartic = 0.5
x_max = 5.0
nx = 100
dx = 2.0 * x_max / (nx - 1)
x = [i * dx for i in range(-(nx - 1) / 2, nx / 2 + 1)]
y = [V(a) for a in x]
pylab.plot(x, y, label = 'Anharmonic [cubic = -0.5, quartic = 0.5]')

cubic = 0.0
quartic = 0.0
y = [V(a) for a in x]
pylab.title('Potential of Harmonic and Anharmonic Oscillators')
pylab.xlabel('x')
pylab.ylabel('Potential')
pylab.plot(x, y, label='Harmonic [cubic = 0, quartic = 0]')
pylab.legend(loc=9)
pylab.grid()
pylab.axis([-4.0, 4.0, 0.0, 3.0])
pylab.savefig("Potentials.png")
pylab.close()


for n in range(0,11):
	energy_list =[]
	cq_list = []
	legend = 'n ='+ str(n)
	for cq in numpy.arange(0, 1.0, 0.01):
		energy_list.append(Energy(n, -cq, cq))
		cq_list.append(cq)
	
	pylab.plot(cq_list, energy_list , label = legend)

pylab.title('$E_n$ for Anharmonic Oscillator with 0 < quartic = -cubic < 1')
pylab.xlabel('quartic (= -cubic)')
pylab.ylabel('$E_n$ (quartic, cubic)')
pylab.legend(loc=3)
pylab.grid()
pylab.savefig("Energy_1.png")	
pylab.close()

for n in range(0,11):
	energy_list =[]
	cq_list = []
	legend = 'n ='+ str(n)
	for cq in numpy.arange(0, 0.5, 0.01):
		energy_list.append(Energy(n, -cq, cq))
		cq_list.append(cq)
	
	pylab.plot(cq_list, energy_list, label = legend)

pylab.title('$E_n$ for Anharmonic Oscillator with 0 < quartic = -cubic < 0.5')
pylab.xlabel('quartic (= -cubic)')
pylab.ylabel('$E_n$ (quartic, cubic)')
pylab.legend(loc=3)
pylab.grid()
pylab.savefig("Energy_0.5.png")	
pylab.close()

print 'Partition Sum (n=100, beta=1) is', Z(0, 0, 1, 100), 1/(2*math.sinh(0.5))
print 'Partition Sum (n=100, beta=10) is', Z(0, 0, 10, 100), 1/(2*math.sinh(5))
print 'Partition Sum (n=100, beta=0.1) is', Z(0, 0, 0.1, 100), 1/(2*math.sinh(0.05))
