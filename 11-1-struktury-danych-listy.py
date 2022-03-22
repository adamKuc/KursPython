# lista — mogą istnieć duplikaty, liczy się kolejność, możemy usuwać, sortować

# lista = []
# lista.append('Adam')
# lista.append('kamil')
# print(lista)

lista = ['kamil', 'Zygmunt', 'Adam', 'Mariusz', 'Zygmunt', 1]
lista2 = ['Gosia', 'Bóc']
lista3 = lista2 + lista + lista2
print(lista3)
# print(lista[0])
# print()
# lista.reverse()  # odwrócenie listy
# lista.sort()  # liczy się wielkość liter
# lista.sort(reverse=True)  # liczy się wielkość liter odwrotoność
for name in lista:
	print(name)
# print(lista.count('Zygmunt'))  # zlicz wystąpienia w liście, liczy się wielkość znaków
# print(len(lista))
# print(lista)
# print(lista.pop(0))  # pop zwraca element i usuwa z listy
# # print(lista[0])
# print()
# print(lista)
# lista.remove('Zygmunt')  # remove - usuwa z listy pierwsdze wystąpienie danej wartości
# print()
# print(lista)
# lista.clear()  # czyści listę
