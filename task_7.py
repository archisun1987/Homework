a = int(input("Введите километраж в первый день:"))
b = int(input("Введите километраж который необходимо достич:"))
day = 1
print(day, "день:", a)
while a < b:
    a = float('{:.2f}'.format(a + a * 0.1))
    day += 1
    print(day, "день:", a)
    continue
if a >= b:
    print(f"На {day}-й день cпортсмен достиг результата - не менее {b} км.")
