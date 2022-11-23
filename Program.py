# -*- coding: utf8 -*-
import logging
from random import randint
import random


#Запуск логера
logging.basicConfig(filename='app.log', level=logging.DEBUG)
logging.info('Statred')

print("Давай сыграем в игру? Угадай число.")
while True:
    try:
        N = int(input('Введи число N'))
        K = int(input('Введи количество попыток'))
        logging.info(f'Введено число {N}')
        logging.info(f'Введено число {K}')
        break
    except ValueError:
        print(" Введи число! ")
        logging.error("ValueError", exc_info=True)

a = list(range(1, N + 1))
b = random.choices(a)
logging.info(f'Попробуй угадать мое число:)')
(type(b), ' - ', b)

c = 1
while True:
    while True:
        try:
            d = int(input("Попробуй угадай мое число :)"))
            logging.info(f'попытка {c} Введено {d}')
            break
        except ValueError:
            print(" Вводи число ! ")
    if c < K:
        if N < b[0]:
            print("Попробуй еще раз, твое число меньше b")
        elif d > b[0]:
            print("Попробуй еще раз, твое число больше b")
        elif d == b[0]:
            print("Поздаравляю, вы угадали!")
            logging.info(f'Число {b} угадано! ')
            break
    else:
        print("К сожалению, но вы не угадали!!! \nПопытки закончились, попробуйте в другой раз!")
        logging.info(f'попытки закончились')
        break
    c += 1
print("Спасибо за игру :)")    
