countries = {}
countries['Polska'] = ('Warszawa', 38)
countries['Niemcy'] = ('Berlin', 83)
countries['Słowacja'] = ('Bratysława', 5.6)

def show_country(country):
	country_info = countries.get(country)
	print()
	print(country)
	print('-----------')
	print('Stolica:' + country_info[0])
	print('Populacja (mln):' + str(country_info[1]))

# for country in countries:
# 	print(country)

country_from_user = input("informacje o jakim kraju chcesz wyświetlić?:")

show_country(country_from_user)


