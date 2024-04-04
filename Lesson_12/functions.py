def show_sum(a, b):
    print(f'{a} + {b} = {a + b}')

def show_dif(a, b):
    result = a - b
    return result

def show_div(a, b):
    if b == 0:
        return None
    result = a / b
    return result


a = int(input('Введіть перше число:'))
b = int(input('Введіть друге число:'))

result = show_sum(a, b)
print(f'{result=}')
result_2 = show_dif(a, b)
print(f'{result_2=}')

'''
    Переписати код. Зробити функції для операцій -, *, /.
'''
def find_max(a, b, c, d):
    return max(a, b, c, d)