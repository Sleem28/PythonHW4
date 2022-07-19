# Вычислить число c заданной точностью d

# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

def get_num_comma(f_num: float) -> int:
    symb = 0
    while(f_num < 1):
        symb += 1
        f_num *= 10
    return symb

pi = 3.14159265358979323846 # 20 digits
correct = False
while(not correct):
    try:
        d = (float(input('Введите точность числа пи от 0.1 до 0.0000000001: ')))
        correct = True
    except:
        print('Введена некорректная точность. Введите точность пи еще раз.')
        correct = False

print(f'Для точности {d} число пи будет равно {round(pi, get_num_comma(d))}')
