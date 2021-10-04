kolvo = int(input('Введите количество посетителей: '))
summa = 0
for age_posetiteli in range(kolvo):
	age = int(input('Введите возраст посетителя: '))
	if age < 18:
		summa = summa + 0
	if 18 <= age < 25:
		summa = summa + 990
	if age >= 25:
		summa = summa + 1390
if kolvo > 3:
	summa = summa * 0.9
print(f'Стоимость заказа равна: ', summa)