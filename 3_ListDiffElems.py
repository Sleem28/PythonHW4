#Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
import random as rnd
#-----------------------------------------заполним массив разными знаениями-----------------------------------------------+
def fill_list(index:int) ->list:
    output_list = list()

    for i in range(index):
        output_list.append(rnd.randint(0,10))
    return output_list
#-----------------------------------------отберем разные значения из массива----------------------------------------------+
def get_dif_list(int_list:list) -> list:
    output_list = list()
    all_list = list()
    
    for item in int_list:
        if not item in output_list:
            all_list.append(item)

    for item in all_list:
        counter = 0
        for elem in int_list:
            if elem == item:
                counter += 1
        if counter == 1:
            output_list.append(item)
    return output_list
#-----------------------------------------------main()--------------------------------------------------------------------+
int_list = fill_list(20)

dif_list = get_dif_list(int_list)
print(f'Сгенерированная последовательность значений имеет вид{int_list}')
print(f'Список с уникальными, отсортированными значениями имеет вид{dif_list}')