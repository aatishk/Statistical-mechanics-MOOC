import random, math, pylab

def dist(x, y):
    return math.sqrt((x[0] -y[0]) ** 2 + (x[1] - y[1]) ** 2)

def tour_length(cities, N):
    return sum (dist(cities[k + 1], cities[k]) for k in range(N - 1)) + dist(cities[0], cities[N - 1])

N = 10
seeds = [12345, 54321, 56789, 98765]
for seed in range(len(seeds)):
	random.seed(seeds[seed])
	cities = [(random.uniform(0.0, 1.0), random.uniform(0.0, 1.0)) for i in range(N)]
	for run in range(10):
		random.seed()
		energy_min = float('inf')
		print "seed =", seeds[seed], "run =", run
		for iter in xrange(1000000):
			random.shuffle(cities)
			energy =  tour_length(cities, N)
			if energy < energy_min:
				print energy
				energy_min = energy
				new_cities = cities[:]
		cities = new_cities[:]
		for i in range(1,N):
			pylab.plot([cities[i][0], cities[i - 1][0]], [cities[i][1], cities[i - 1][1]], 'bo-')
		pylab.plot([cities[0][0], cities[N - 1][0]], [cities[0][1], cities[N - 1][1]], 'bo-')
		pylab.title("Energy_min = "+str(energy_min)+", seed = "+str(seeds[seed])+", run = "+str(run))
		pylab.axis('scaled')
		pylab.axis([0.0, 1.0, 0.0, 1.0])
		pylab.savefig('TSP_configuration_N_'+str(N)+'_seed_'+str(seeds[seed])+'_run_'+str(run)+'.png')
		pylab.close()