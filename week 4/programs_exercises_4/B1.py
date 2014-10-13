import random, math
 
def Vol1_s(dimension):
    return math.pi ** (dimension / 2.0)/ math.gamma(dimension / 2.0 + 1.0)
 
def direct_pi(N,d):
    n_hits = 0
    for i in range(N):
    	sum_x2 = 0.0
    	flag = 0

    	for j in range(d):
    		x = random.uniform(-1.0, 1.0)
    		sum_x2 += (x ** 2.0)
    		if sum_x2 > 1.0:
    			flag = 1
    			break   	

    	if flag == 0:
    		n_hits += 1

    return n_hits
 
n_trials = 1000000
d = 1
f = open('hypersphere_volumes.txt', 'w')
f.write('d | estimation of Vol1_s(d) | Vol1_s(d) (exact) | n_hits\n')

while True:
	Vol1_s_exa = Vol1_s(d)
	
	n_hits = direct_pi(n_trials,d)
	Vol1_cube = float(2 ** d)
	Vol1_s_est = Vol1_cube * (float(n_hits) / float(n_trials))

	f.write(str(d) + '\t' + str(Vol1_s_est) + '\t\t' + str(Vol1_s_exa) + '\t\t'+ str(n_hits) + '\n')
	
	if n_hits > 0:		
		d += 1
	else:
		break
