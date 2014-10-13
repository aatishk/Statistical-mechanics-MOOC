import random, math, os, pylab

def energy(S, N, nbr):
    E = 0.0
    for k in range(N):
        E -=  S[k] * sum(S[nn] for nn in nbr[k])
    return 0.5 * E
    
def x_y(k, L):
	y = k // L
	x =k -y *L 
	return x, y

L = 32
N = L *L
nbr = {i : ((i // L) * L + (i + 1) % L, (i + L) % N,
              (i // L) * L + (i - 1) % L, (i - L) % N) \
                                      for i in range(N)}
T = 2.27
filename = 'local_'+ str(L) + '_' + str(T) + '.txt'

if os.path.isfile(filename):
	f = open(filename, 'r')
	S = []
	for line in f:
		S.append(int(line))
	f.close()
	print 'starting from file', filename
else:
	S = [random.choice([1, -1]) for k in range(N)]
	print 'starting from scratch'
nsteps = N * 1000
beta = 1.0 / T

E = [energy(S, N, nbr)]

for step in xrange(nsteps):
	if step % 10000 == 0:
		print "steps = ", step, "done, nsteps =", nsteps, ", percentage = ", 100 * step/nsteps
	k = random.randint(0, N - 1)
	delta_E = 2.0 * S[k] * sum(S[nn] for nn in nbr[k])
	if random.uniform(0.0, 1.0) < math.exp(-beta * delta_E):
		S[k] *= -1
	E.append(energy(S, N, nbr))

E_mean = sum(E)/ len(E)
E2_mean = sum(a ** 2 for a in E) / len(E)
cv = (E2_mean - E_mean ** 2 ) / N / T ** 2

print L, nsteps, cv

f = open(filename, 'w')
for a in S:
	f.write(str(a) + '\n')
f.close()