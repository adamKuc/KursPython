def show_tasks():
	task_id = 0
	for task in tasks:
		print('[' + str(task_id) + '] ' + task)
		task_id += 1


def add_task():
	task = input("wpisz treść zadania: ")
	tasks.append(task)
	print('Dodano zadanie')


def del_task():
	task_id = int(input("nr zadania do usunięcia: "))
	if task_id < 0 or task_id > len(tasks) - 1:
		print('Błędny numer')
		return
	tasks.pop(task_id)
	print('Usunięto zadanie')


def save_tasks():
	file = open('zadania.txt', 'w+')
	for task in tasks:
		file.write(task + "\n")
	file.close()
	print('Zapisano zadanie')


def load_tasks():
	try:
		file = open('zadania.txt')
		for line in file.readlines():
			tasks.append(line.strip())
		file.close()
	except FileNotFoundError:
		print('Brak pliku do wczytania')


user_choice = 0

tasks = []
# tasks.append("Zabić putina")
load_tasks()

while user_choice != 5:
	if user_choice == 1:
		show_tasks()
	elif user_choice == 2:
		add_task()

	elif user_choice == 3:
		del_task()
	elif user_choice == 4:
		save_tasks()
	print()
	print('1. pokaz zadania')
	print('2. Dodaj zadania')
	print('3. Usuń')
	print('4. Zapisz zmiany do pliku')
	print('5. Wyjdź')
	user_choice = int(input('Podaj liczbę: '))
