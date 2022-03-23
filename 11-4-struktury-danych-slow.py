countries_capitals = {'Polska': 'Warszawa', 'Niemcy': 'berlin'}
print(countries_capitals)
countries_capitals['Czechy'] = 'Praga'

for key in countries_capitals.keys():
	print(key)

for val in countries_capitals.values():
	print(val)

for key, val in countries_capitals.items():
	print(key + ': ' + val)

print(countries_capitals['Polska'])
# print(countries_capitals['usa'])  # wywali błąd
print(countries_capitals.get('Polska'))
# print(countries_capitals.get('usa'))  # NIE będzie błędu, zwraca None
# print(countries_capitals.setdefault('usa', 'capital'))  # jeśli nie będzie


print(countries_capitals.pop('Polska'))  # zwraca wartość dla klucza i usuwa ze słownika
print(countries_capitals)

print(countries_capitals.popitem())  # zwraca OSTANIO dodaną wartość ze słownika
print(countries_capitals)

countries_capitals.clear()  # wyczyszczenie słownika
print(countries_capitals)
