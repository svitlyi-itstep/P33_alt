# for i in range(20, 1, -1):
#     print(i)
#
# message = ''
#
# while message != 'quit':
#     message = input('Enter message: ')


'''
    Input: a, b – границі діапазону
    
    Вивести всі непарні числа від a до b, включаючи b.
'''

# a = int(input('Enter a:'))
# b = int(input('Enter b:'))
#
# if a % 2 == 0:
#     a += 1
#
# for i in range(a, b + 1, 2):
#     print(i)
#
#
# sum = 0
# for i in range(a, b+1):
#     sum += 1
# print(sum)

max_number = None

while True:
    number = int(input('Enter number: '))

    if max_number is None or number > max_number:
        max_number = number

    print('Max: ', max_number)
    if number == 7:
        break

