import random, math

L = 32
N = L * L
nbr = {i : ((i // L) * L + (i + 1) % L, (i + L) % N,
            (i // L) * L + (i - 1) % L, (i - L) % N) \
                                    for i in range(N)}
T = 2.3
beta = 1.0 / T

t_coup_ave = []
for run in range(10):
	t_coup = []
	for iter in range(10):
		#print iter
		S0 = [1] * N
		S1 = [-1] * N
		step = 0
		while True:
			step += 1
			k = random.randint(0, N - 1)
			Upsilon = random.uniform(0.0, 1.0)
			h = sum(S0[nn] for nn in nbr[k])
			S0[k] = -1
			if Upsilon < 1.0 / (1.0 + math.exp(-2.0 * beta * h)):
				S0[k] = 1
			h = sum(S1[nn] for nn in nbr[k])
			S1[k] = -1
			if Upsilon < 1.0 / (1.0 + math.exp(-2.0 * beta * h)):
				S1[k] = 1
			if step % N == 0:
				n_diff = sum(abs(S0[i] - S1[i]) for i in range(N))
				if n_diff == 0:
					t_coup.append(step / N)
					break
	print t_coup
	print run, sum(t_coup) / len(t_coup)
	t_coup_ave.append(sum(t_coup) / len(t_coup))
print sum(t_coup_ave) / len(t_coup_ave)