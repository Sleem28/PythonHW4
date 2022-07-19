# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import os
import random as rnd
from time import sleep
#-----------------------------------------------Выводит в консоль степень числа------------------------------------------------------+
def get_degree(degree:int) -> str:
    dict = {1: '\u00B9',
            2: '\u00B2',
            3: '\u00B3',
            4: '\u2074',
            5: '\u2075',
            6: '\u2076',
            7: '\u2077',
            8: '\u2078',
            9: '\u2079'}
    return dict[degree]
#----------------------------------------------Генерирует список списков с коэффициентами a b c--------------------------------------+
def get_coef_list(elements:int) -> list:
    output_list = list()
    for i in range(0,elements):
        output_list.append([rnd.randint(0,100), rnd.randint(0,100), rnd.randint(0,100)])
    return output_list
#---------------------------------------------Пишем многочлены в файл----------------------------------------------------------------+
def write_polinomials_to_file(path:str, coef_list:list,degree:str, k:str):
    with open(path,'a') as data:
        for item in coef_list:
            text = f'Запишем в файл строку {item[0]}*x{degree} + {item[1]}*x{degree} + {item[2]} = 0'
            # Если писать эту строку в файл, то бъет ошибку декодировки стринг в чар из-за знака степени, поэтому запишу в файл по питоновски
            # Как это победить не решил, нет времени
            print(text)
            data.write(f'{item[0]}*x**{k} + {item[1]}*x**{k} + {item[2]} = 0\n')
#------------------------------------------------------------main()------------------------------------------------------------------+

path = os.path.join('Folder', 'polinomials.txt')
k_l = '\u1d4f'

print(f'Изначальный вид многочленов в уравнении имеет вид: a*x{k_l} + b*x{k_l} + c')
k = int(input('Задайте натуральную степень k: '))
sk = get_degree(k)
print('Сгенерируем список коэффициентов a, b и c.')
lsts = int(input('Введите количество списков коэффициентов: '))
coef_list = get_coef_list(elements=lsts)
print('Подставим значения степени и коэффициентов многочлена из списка. Запишем их в файл polinomials.txt.')
write_polinomials_to_file(path=path, coef_list=coef_list,degree=sk,k=str(k))
