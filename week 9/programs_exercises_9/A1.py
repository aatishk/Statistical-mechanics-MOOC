import math, random

def V(x):
    pot =  -4.0 * x ** 2   -0.5 * x ** 3 +  x ** 4
    return pot

#gamma = 0.001953
gamma = 0.5
n_iter = 1000
n_plus = 0
for iteration in range(n_iter):
    T = 2.0
    x = 0
    delta = 0.1
    step = 0
    n_accept = 0
    while T > 0.0001:
        step += 1
        if step == 100:
            T *= (1.0 - gamma)
            if n_accept < 20:
               delta *= 0.5
            step = 0
            n_accept = 0
        x_new = x + random.uniform(-delta, delta)
        if random.uniform(0.0, 1.0) < math.exp(- (V(x_new) - V(x)) / T):
            x = x_new
            n_accept += 1
    if x > 1.58 and x < 1.62: 
    	n_plus += 1
print gamma, n_plus / float(n_iter), x