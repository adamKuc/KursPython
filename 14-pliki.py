file = open('file.txt', 'w+')
# r - do odczytu
# w - do zapisu
# w+ - do zapisu i odczytu

countries_capitals = {'Polska': 'Warszawa', 'Niemcy': 'berlin', 'Czechy': 'Praga'}

for country, capital in countries_capitals.items():
	file.write(country + ': ' + capital + "\n")
file.close()

### odczyt

file = open('file.txt')
for line in file.readlines():
	print(line.strip())
file.close()
