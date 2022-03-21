name = " a Adam a "
# print(len(name))
# print(name.capitalize())  # pierwsza litera duża
# print(name.upper())  # wszystki literu duże
# print(name.lower())  # wszystki literu małe

print(name[0])  # A
print(name[0:2])  # Ad
print(name[2:])  # am
print(name[-3:])  # dam - od konca

str1 = 'jebać pis i putina'
print(str1.split(" "))  # string na tablice

join_str = "|"
print(join_str.join(['jebac','pis','putina','konfederacje']))

print(name.startswith('a'))  # wielkośc liter ma znaczenie
print(name.startswith('A'))

print(name.endswith('a'))  # wielkośc liter ma znaczenie
print(name.endswith('m'))


print(name.rstrip('m'))

print(name.strip('a'))

print(name.strip())  # usuwa spacje

bond = 7
print(str(bond).zfill(3))



