import random, math, pylab

def Vol1_s(dimension):
    return math.pi ** (dimension / 2.0)/ math.gamma(dimension / 2.0 + 1.0)

dimensions_list = []
Vol1_s_list = []

for dimension in range(1,201):
	dimensions_list.append(dimension)
	Vol1_s_list.append(Vol1_s(dimension))
	print dimension, Vol1_s(dimension)

pylab.plot(dimensions_list, Vol1_s_list, ':k')
pylab.plot(dimensions_list, Vol1_s_list)
pylab.xlabel('dimension')
pylab.ylabel('Vol1_s')
pylab.yscale('log')
pylab.grid()
pylab.title('Volume of hypersphere as function of dimension')
pylab.savefig('Vol1_s_dim.png')
pylab.show()