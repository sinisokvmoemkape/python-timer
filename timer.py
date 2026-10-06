import datetime as data
import time
from playsound3 import playsound

info = []
txt = 'Введите час: '
txt2 = 'Введите минуту: '
name = input('Введите название своего Будильника: ')

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


time_make = data.datetime.now()
hour_make = time_make.hour
year_make = time_make.year
minute_make = time_make.minute


hour1 = info[0] 
minute1 = info[1]
print(f'Будильник поставлен на : {hour1} : {minute1}')
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
file = open('history.txt', 'a')
file.write(f'''\nНазвание Будильника - {name}
Время Создание Будильника - {hour_make} : {minute_make} Год - {year_make}
Время окончания Будильника - {hour1} : {minute1} Год - {year}''')
file.close()
info.clear()
# while True:
playsound('melody.mp3')
    # if sound.is_alive:
    #         time.sleep(0.5)
    #         if not sound.is_alive:
    #             sound.stop()
                
 
    
    
        



