#  #  #  #  #
#  #  #  #  #
#  #  #  #  #
#  #  #  #  #
#  #  #  #  #

#  #  #  #  #
#           #
#           #
#           #
#  #  #  #  #

def is_edge(x, y, length):
    return 0 in (x, y) or length - 1 in (x, y)


def draw_square(length, symbol, solid):
    # symbol += '  '
    # print(f'{symbol * length}\n' * length)

    for i in range(length):
        for j in range(length):
            if is_edge(i, j, length) or solid:
                print(f'{symbol}  ', end='')
            else:
                print(f'   ', end='')
        print()


draw_square(5, '#', False)

numbers = [int(i) for i in input('Введіть числа:').split() if i.isnumeric()]
print(numbers)

def find_sum(list):
    # return sum(list)
    for item in list:
        # розрахунок суми

def range_sum(start, end):
    return sum(range(start, end + 1))

import math
math.factorial()