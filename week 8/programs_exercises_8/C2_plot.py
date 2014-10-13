import pylab

T_list = [5.0, 4.0, 3.0, 2.5, 2.4, 2.3]
t_list = [20, 32, 90, 469, 1037, 4230 ]

pylab.plot (T_list, t_list, "o")
pylab.plot (T_list, t_list)
pylab.xlabel("Temperature")
pylab.ylabel("Average Coupling Time")
pylab.title("Heatbath Algorithm, Coupling for L=32")
pylab.savefig("C2.png")
pylab.grid()
pylab.show()