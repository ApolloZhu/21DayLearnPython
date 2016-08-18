table = dict()
table = {'a':1,'b':2}
table['c'] = 3
print(table)

table = {'a':1,'b':2}
table.setdefault('c',3)
print(table)

table = dict.fromkeys(('a','b'),1)
table['b'] = 2
table.update({'c':3})
print(table)
