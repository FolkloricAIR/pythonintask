﻿#Шпилёва М.А. Задание №5 Вариант 19
#Напишите программу, которая бы при запуске случайным образом отображала
#название одной из восьми планет Солнечной системы.
import random
print ('Программа случайным образом отображает название одной из планет Солнечной системы:')
planets=['Меркурий', 'Венера', 'Земля', 'Марс', 'Юпитер', 'Сатурн', 'Уран', 'Нептун']
print(random.choice(planets))
input('Нажмите Enter')