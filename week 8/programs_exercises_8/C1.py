import random, math

L = 6
N = L * L
nbr = {i : ((i // L) * L + (i + 1) % L, (i + L) % N,
            (i // L) * L + (i - 1) % L, (i - L) % N) \
                                    for i in range(N)}
nsteps = 1000000 * N
T = 2
beta = 1.0 / T
S = [random.choice([-1, 1]) for site in range(N)]
E = -0.5 * sum(S[k] * sum(S[nn] for nn in nbr[k]) \
                                for k in range(N))
Energies = []
for step in range(nsteps):
	if step % 10000 == 0:
		print "steps = ", step, "done, nsteps =", nsteps, ", percentage = ", 100 * step/nsteps
	
	k = random.randint(0, N - 1)
	Upsilon = random.uniform(0.0, 1.0)
	h = sum(S[nn] for nn in nbr[k])
	Sk_old = S[k]
	S[k] = -1
	if Upsilon < 1.0 / (1.0 + math.exp(-2.0 * beta * h)):
		S[k] = 1
	if S[k] != Sk_old:
		E -= 2.0 * h * S[k]
	Energies.append(E)
print sum(Energies) / len(Energies) / N