sec = int(input("Введите время в секундах"))
hour = float('{:.2f}'.format(sec / 3600))
minute = float('{:.2f}'.format(sec / 60))
print(f'Время в формате ч:м:с - {hour} : {minute} : {sec}')
