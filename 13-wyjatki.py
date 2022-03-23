countries_capitals = {'Polska': 'Warszawa', 'Niemcy': 'berlin', 'Czechy': 'Praga'}

try:
	print(2 / 0)
	print(countries_capitals['usa'])
# except KeyError:
# 	print('Nie znaleziono klucza')
# except ZeroDivisionError:
# 	print('Nie można dzielić przez 0')
except:
	print('Nie znany błąd')
finally:
	print('To wykona się zawsze')
print('tutaj')
