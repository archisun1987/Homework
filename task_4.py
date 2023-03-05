n = int(input("Введите целое положительное число: "))
maxi = n % 10
n = n // 10
while n > 0:
    if n % 10 > maxi:
        maxi = n % 10
    n = n // 10
print('Максимальное число: ', maxi)
