import cmath, math, random, pylab, os

def show_conf(L, title, fname):
    pylab.axes()
    for [x, y] in L:
        for delx in range(-1, 2):
            for dely in range(-1, 2):
                cir = pylab.Circle((x + delx, y + dely), radius = sigma,  fc = 'r')
                pylab.gca().add_patch(cir)
    pylab.axis('scaled')
    pylab.title(title)
    pylab.axis([0.0, 1.0, 0.0, 1.0])
    pylab.savefig(fname)
    pylab.show()

def dist(x, y):
    d_x = abs(x[0] - y[0]) % 1.0
    d_x = min(d_x, 1.0 - d_x)
    d_y = abs(x[1] - y[1]) % 1.0
    d_y = min(d_y, 1.0 - d_y)
    return d_x**2 + d_y**2


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
            if dist(L[i], L[j]) < 2.8 **2 * sigma_sq and i != j:
                n_neighbor += 1
                dx, dy = delx_dely(L[j], L[i])
                angle = cmath.phase(complex(dx, dy))
                vector += cmath.exp(6.0j * angle)
        if n_neighbor > 0: vector /= n_neighbor
        sum_vector += vector
    return sum_vector / float(N)

N =  64
filename = 'disk_configuration_0.72'
if os.path.isfile(filename):
    f = open(filename, 'r')
    L = []
    for line in f:
        a, b = line.split()
        L.append([float(a), float(b)])
    f.close()
    print 'starting from file', filename
else:
    N_sqrt = int(math.sqrt(N) + 0.5)
    delxy = 1./ 2. / N_sqrt
    two_delxy = 2.0 * delxy
    L = [ [delxy + i * two_delxy, delxy + j * two_delxy] \
        for i in range(N_sqrt) for j in range(N_sqrt)]
    print 'starting from scratch'
eta = 0.73
x_values = []
y_values = []
for iteration in range(40):
    eta -= 0.01
    print eta
    sigma = math.sqrt(eta / N / math.pi)
    sigma_sq = sigma ** 2
    delta = 0.3 * sigma
    n_steps = 10000
    average_Psi_6  = []
    for steps in range(n_steps):
        a = random.choice(L)
        b = [a[0] + random.uniform(-delta, delta), a[1] + random.uniform(-delta, delta)]
        min_dist_sq = min(dist(b, c) for c in L if c != a)
        if  min_dist_sq > 4.0 * sigma ** 2:
            a[:] = [b[0] % 1.0, b[1] % 1.0]
        if steps % 100 == 0:
            average_Psi_6.append(abs(Psi_6(L, sigma_sq)))
    y_values.append(sum(average_Psi_6)/len(average_Psi_6))
    x_values.append(eta)

pylab.plot(x_values, y_values)
pylab.title('Hard disks: global orientational order parameter $N=64$')
pylab.xlabel('$\eta$')
pylab.ylabel('$\Psi_6$')
pylab.axis([0.3, 0.8, 0.0, 0.8])
pylab.savefig('psi_6_eta_soln.png')
pylab.show()