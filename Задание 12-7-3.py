money=int(input('введите размер депозита:'))

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

deposit=[]

for value in per_cent.values():
	deposit.append(round(value*money/100, 2))

print(deposit)

print("Максимальная сумма, которую вы можете заработать —", max(deposit))