# set — NIE powtarzalne elementy, lista bez duplikatów,
# NIE może być z duplikowanych wartości,
# elementy muszą być NIE mutowalne (nie można dodać listy)
# elementy nie są uporządkowane,
# imiona[0] NIE działa
pusty_set = set()
pusty_set.add('test')
imiona = {'kamil', 'Zygmunt', 'Adam', 'Mariusz', 'Zygmunt'}
imiona.add('Marta')
imiona.remove('Zygmunt')  # jeżeli dany element nie istnieje to będzie błąd
imiona.discard('Adadm')  # jeżeli dany element nie istnieje to NIE będzie błędu
print(imiona)

set3 = imiona.union(pusty_set)  # zwraca nowy set, nie modyfikuje obecne
for i in set3:
	print(i)
print()

set4 = set3.difference(imiona)  # różnica w setach jest w set3, ale nie ma w imiona
for i in set4:
	print(i)
print()

set5 = set3.intersection(imiona)  # część wspólna
for i in set5:
	print(i)
print()

set6 = set3.symmetric_difference(imiona)  # różnica w setach jest w jednym secie, ale nie ma w drugim
for i in set6:
	print(i)
print()

# imiona.update(pusty_set)  # zwraca nowy set, nie modyfikuje obecne
# for i in imiona:
# 	print(i)

lista = ['Gosia', 'Bóc']

lista.extend(set6)  # dodanie setu do listy

print(lista)


