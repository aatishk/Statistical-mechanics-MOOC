import random, pylab

n_trials = 100000
unif_list =[]
unifsq_list = []

for trial in range(n_trials):
	unif_list.append(random.uniform (-1.0, 1.0))
	unifsq_list.append(random.uniform (-1.0, 1.0) ** 2.0)


pylab.hist(unif_list, bins=100, normed=True)
pylab.xlabel('x')
pylab.ylabel('Frequency')
pylab.grid()
pylab.title('Uniform distribution')
pylab.savefig('Uniform_distribution.png')
pylab.show()

pylab.hist(unifsq_list, bins=100, normed=True)
pylab.xlabel('$x^2$')
pylab.ylabel('Frequency')
pylab.grid()
pylab.title('Uniform squared distribution')
pylab.savefig('Uniform_sq_distribution.png')
pylab.show()