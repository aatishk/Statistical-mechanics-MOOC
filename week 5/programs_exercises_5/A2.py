import numpy

a = numpy.array([[1, 2, 3], [4, 5, 6]])
print a
b = numpy.array([[1, 2], [3, 4], [5, 6]])
print b

c = numpy.dot(a, b)
print c

d = numpy.dot(b, a)
print d

e = d * 2
print e
f = numpy.diag(c)
print f

g = numpy.diag(c).sum()
print g