import os, random, math, pylab, cmath, numpy

def delx_dely(x, y):
    d_x = (x[0] - y[0]) % 1.0
    if d_x > 0.5: d_x -= 1.0
    d_y = (x[1] - y[1]) % 1.0
    if d_y > 0.5: d_y -= 1.0
    return d_x, d_y

def Psi_6(L, sigma_sq):
    sum_vector = 0j
    for i in range(N):
        vector  = 0j
        n_neighbor = 0
        for j in range(N):
            if dist_sq(L[i], L[j]) < 2.8 **2 * sigma_sq and i != j:
                n_neighbor += 1
                dx, dy = delx_dely(L[j], L[i])
                angle = cmath.phase(complex(dx, dy))
                vector += cmath.exp(6.0j * angle)
        if n_neighbor > 0: vector /= n_neighbor
        sum_vector += vector
    return sum_vector / float(N)

def dist(x,y):
    d_x = abs(x[0] - y[0]) % 1.0
    d_x = min(d_x, 1.0 - d_x)
    d_y = abs(x[1] - y[1]) % 1.0
    d_y = min(d_y, 1.0 - d_y)
    return  math.sqrt(d_x**2 + d_y**2)

def dist_sq(x,y):
    d_x = abs(x[0] - y[0]) % 1.0
    d_x = min(d_x, 1.0 - d_x)
    d_y = abs(x[1] - y[1]) % 1.0
    d_y = min(d_y, 1.0 - d_y)
    return  (d_x**2 + d_y**2)
    
N=64
eta_start=0.72
eta_end=0.2

sqrt_N = int(math.sqrt(N))

sigma = math.sqrt(eta_start/(math.pi*N))
inter_disk_distance = (1.0-(sqrt_N*2.0*sigma))/sqrt_N

filename = 'N_C3_disk_configuration.txt'
if os.path.isfile(filename):
    f = open(filename, 'r')
    L = []
    for line in f:
        a, b = line.split()
        L.append([float(a), float(b)])
    f.close()
    print 'starting from file', filename
else:
    L = []
    for k in range(sqrt_N):
    	x = (2*k+1)*(sigma+inter_disk_distance/2.0)
    	for l in range(sqrt_N):
    		y = (2*l+1)*(sigma+inter_disk_distance/2.0)
    		L.append([x, y])
    print 'starting from scratch'

n_steps = 10000
Psi_6_list = []
eta_list = []
acc_prob_list = []
delta = 0.01

for eta in numpy.arange(eta_start, eta_end, -0.01):
	sigma = math.sqrt(eta/(math.pi*N))
	
	print 'sigma =', sigma
	print 'delta =', delta
	count_Psi_6 = 0
	total_Psi_6 = 0.0
	acc_steps = 0
	
	for steps in range(n_steps):
		a = random.choice(L)
		b = [a[0] + random.uniform(-delta, delta), a[1] + random.uniform(-delta, delta)]  
	
		min_dist = min(dist(b, c) for c in L if c != a)
		if not (min_dist < 2.0 * sigma):
			a[:] = b
			a[0] = a[0] % 1
			a[1] = a[1] % 1  
			acc_steps += 1

		if steps > 0:
			if (steps % 100) == 0:
				count_Psi_6 +=1
				total_Psi_6 += abs(Psi_6(L, sigma*sigma))
	
				delta += 0.01 * ((float(acc_steps)/steps) - 0.5)

	eta_list.append(eta)
	Psi_6_list.append(total_Psi_6/count_Psi_6)
	acc_prob_list.append(float(acc_steps)/steps)
	print 'eta = ', eta, ', Avg Psi_6 = ', total_Psi_6/count_Psi_6
	print 'Acc ratio = ', float(acc_steps)/steps, '\n' 

pylab.plot(eta_list,Psi_6_list, 'bo')
pylab.plot(eta_list,Psi_6_list, ':k')
pylab.xlabel('$\eta$')
pylab.ylabel('Average $\Psi_6$')
pylab.title('My Markov Disks - Average $\Psi_6$ vs. $\eta$')
pylab.grid()
pylab.savefig('Psi_6_eta.png')
pylab.show()

pylab.plot(eta_list,acc_prob_list, 'bo')
pylab.plot(eta_list,acc_prob_list, ':k')
pylab.xlabel('$\eta$')
pylab.ylabel('$p_{acceptance}$')
pylab.title('My Markov Disks - $p_{acceptance}$ vs. $\eta$')
pylab.grid()
pylab.savefig('p_accept_eta.png')
pylab.show()

f = open(filename, 'w')
for a in L:
   f.write(str(a[0]) + ' ' + str(a[1]) + '\n')
f.close()