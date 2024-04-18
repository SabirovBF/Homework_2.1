a = ['Слов', 'два']
b, c = a[0], a[1]
a.remove(b)
a.remove(c)
a.append(c)
a.append(b)
print(a)