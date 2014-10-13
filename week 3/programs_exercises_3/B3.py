import os, random, math, pylab

def show_conf(L, sigma, title, fname):
    pylab.axes()
    for [x, y] in L:
        for ix in range(-1, 2):
            for iy in range(-1, 2):
                cir = pylab.Circle((x + ix, y + iy), radius = sigma,  fc = 'r')
                pylab.gca().add_patch(cir)
    pylab.axis('scaled')
    pylab.title(title)
    pylab.axis([0.0, 1.0, 0.0, 1.0])
    pylab.savefig(fname)
    pylab.show()

def dist(x,y):
    d_x = abs(x[0] - y[0]) % 1.0
    d_x = min(d_x, 1.0 - d_x)
    d_y = abs(x[1] - y[1]) % 1.0
    d_y = min(d_y, 1.0 - d_y)
    return  math.sqrt(d_x**2 + d_y**2)

N=64 #Number of disks
eta=0.72 #desired density
sqrt_N = int(math.sqrt(N)) # Number of disks in one row or column in the starting state

sigma = math.sqrt(eta/(math.pi*N)) #Note L=1 used for calculating disk radius
inter_disk_distance = (1.0-(sqrt_N*2.0*sigma))/sqrt_N #Separation between two disks for L=1 box

print 'inter_disk_distance = ', inter_disk_distance

filename = 'N_disk_configuration.txt'
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
    for k in range(sqrt_N): # Writing the kth row
		x = (2*k+1)*(sigma+inter_disk_distance/2.0) # x for all disks in a row
		for l in range(sqrt_N): #writing lth disk for kth row
			y = (2*l+1)*(sigma+inter_disk_distance/2.0) # y for each disk
			L.append([x, y])
    print 'starting from scratch'

delta = 0.1
n_steps = 0 # set to 0 to dump the initial configuration

for steps in range(n_steps):
    a = random.choice(L)
    b = [a[0] + random.uniform(-delta, delta), a[1] + random.uniform(-delta, delta)]
    b[0] = b[0] % 1 # put back in box
    b[1] = b[1] % 1 # put back in box
    min_dist = min(dist(b, c) for c in L if c != a)
    if not (min_dist < 2.0 * sigma):
        a[:] = b

# Write all disk positions in file to read during next run
f = open(filename, 'w')
for a in L:
   f.write(str(a[0]) + ' ' + str(a[1]) + '\n')
f.close()

# Using pylab to generate the plot
title = 'My Markov Disks, N =' + str(N) +', $\eta$ = '+ str(eta)
show_conf(L, sigma, title, 'N_disks.png')  