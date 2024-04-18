students = {'Schultz', 'Django', 'Brunhilde', 'Fritz'}
employees = {'Schultz', 'Django', 'Calvin', 'Butch', 'Fritz'}
print('Все ', students.union(employees))
print('Учится и работает ', students.intersection(employees))
print('Работает ', employees.difference(students))
print('Учится, либо работает: ',  employees.symmetric_difference(students))
print('*' * 10)
print('Все ', students | employees)
print('Учится и работает ', students & employees)
print('Работает ', employees - students)
print('Учится, либо работает: ',  employees ^ students)
