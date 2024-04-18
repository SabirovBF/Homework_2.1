list_a = ['a','c','b']
list_b = ['a','b','e','d']
list_a.extend(list_b)
list_a.sort()
list_b = list(set(list_a))
list_b.sort()
print(list_a, list_b, sep='\n')
