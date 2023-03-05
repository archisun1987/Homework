prof = int(input("Введите прибыль фирмы: "))
exp = int(input("Введите затраты фирмы: "))
res = abs(prof - exp)
if prof > exp:
    print("Финансовый результат: прибыль. Её величина: ", res)
elif prof < exp:
    print("Финансовый результат: убыток. Его величина: ", res)
else:
    print("Финансовый результат: прибыль равна убыткам.")

ren = float('{:.2f}'.format(res / prof))
if prof > exp:
    print('Рентабельность =', ren)

if prof >= exp:
    staff = int(input("Введите численность сотрудников фирмы: "))
    ppo = res / staff
    print("Прибыль на одного сотрудника фирмы: ", ppo)
