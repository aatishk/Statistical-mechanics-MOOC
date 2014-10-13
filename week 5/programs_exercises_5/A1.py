Names = {}
Names['Albert'] = 'Einstein'
Names['Satyendra'] = 'Bose'
Names['Richard'] = 'Feynman'
Names['Ludwig'] = 'Boltzmann'
# checkpoint 1
print '1'
for name in Names: print name, Names[name]
print
a = Names.pop('Albert')

# checkpoint 2
print '2'
print 'a =', a
for name in Names: print name, Names[name]
print

del Names['Richard']
# checkpoint 3
print '3'
for name in Names: print name, Names[name]
print

L = Names.keys()
M = Names.values()
#checkpoint 4
print '4'
for name in Names: print name, Names[name]
print L, M

b = 'Wolfgang' in Names
#checkpoint 5
print '5'
for name in Names: print name, Names[name]
print b