
# Part one
#
L = range(10)
for k in range(10):
    print L
    L = L[3:] + L[:3]
print
#
# Part two 
#
K = range(10)
for i in range(10):
    print K
    dummy = K.pop()
    K = [dummy] + K
print
#
# Part three
#
J = range(10)
for i in range(10):
    print K
    dummy = K.pop(0)
    K = K + [dummy]
print
#
# Part four
#
I = range(10)
weight = sum(a ** 2 for a in I)