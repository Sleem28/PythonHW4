# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
#----------------------------------------Заполняет список простыми числами до числа, переданного в аргументы--------------------------------------------+
def fill_list_simple_nums(num:int) -> list:
    output_list = list()
    
    for i in range(2,num):
        is_simple = True
        for k in range(2,i):
            if i%k == 0:
                is_simple = False
        if is_simple:
            output_list.append(i)
    return output_list
#------------------------------------------Ищет простые множители для 2 множителей---------------------------------------------------------------------+
def get_list_for_two_multiplier(num: int, simple_list:list) -> list:
    output_list = list()
    for i in range(0,len(simple_list)-1):
        first_elem = simple_list[i]
        for k in range(1,len(simple_list)):
            sec_elem = simple_list[k]
            if first_elem * sec_elem == num:
                if not output_list.__contains__([sec_elem,first_elem]):
                    output_list.append([first_elem,sec_elem])
    return output_list
#------------------------------------------Ищет простые множители для 3 множителей---------------------------------------------------------------------+
def get_list_for_three_multiplier(num: int, simple_list:list) -> list:
    output_list = list()
    for i in range(0,len(simple_list)-2):
        first_elem = simple_list[i]
        for k in range(1,len(simple_list)-1):
            sec_elem = simple_list[k]
            for j in range(2,len(simple_list)):
                third_elem = simple_list[j]
                if first_elem * sec_elem * third_elem== num:
                    if (not output_list.__contains__([sec_elem,first_elem,third_elem])) \
                        and (not output_list.__contains__([third_elem,sec_elem,first_elem]))\
                        and (not output_list.__contains__([sec_elem,third_elem,first_elem])):
                        output_list.append([first_elem,sec_elem,third_elem])
    return output_list
#----------------------------------------------Main()--------------------------------------------------------------------------------------------------+
num = int(input('Введите натуральное число: '))

simple_list = fill_list_simple_nums(num)

two_mult_list = get_list_for_two_multiplier(num,simple_list)
three_mult_list = get_list_for_three_multiplier(num,simple_list)

if(len(two_mult_list)>0):
    print(f'Список простых множителей числа {num} из двух множителей имеет вид {two_mult_list}')
else:
    print(f'Число {num} не разлаживается на 2 простых множителя.')

if(len(three_mult_list)>0):
    print(f'Список простых множителей числа {num} из трех множителей имеет вид {three_mult_list}')
else:
    print(f'Число {num} не разлаживается на 3 простых множителя.')





