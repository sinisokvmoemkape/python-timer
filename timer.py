import datetime as data
import time

info = []
txt = 'Введите час: '
txt2 = 'Введите минуту: '
while True:
    try:
        ahour = info.append(int(input(txt)))
        bmin = info.append(int(input(txt2)))
        if info[0] in range(0, 24) and info[1] in range(0, 60):
            print('данные успешно занесены')
            break
        else:
            info.clear()
            print('вводите толко в пределе 24ех часового формата')
            continue       
    except ValueError:
        print('вводите только целые числа')
        continue
hour1 = info[0] 
minute1 = info[1]
print(f'Время конца таймера: {hour1} : {minute1}')
while True:
    timenow = data.datetime.now()
    hour = timenow.hour
    year = timenow.year
    minute = timenow.minute
    second = timenow.second
    print(f'\rТекущее Время - {hour} : {minute} : {second}, Год - {year} ',end='')
    time.sleep(1)
    if hour1 == hour and minute1 == minute:
        break
print(f'\n{hour1} : {minute1} - ВРЕМЯ ВЫШЛО!!!')


    


