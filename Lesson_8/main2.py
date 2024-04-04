import random

secret = random.randint(1, 500)

import time

start = time.time()

end = time.time()

print(f'Пройшло {round(end - start, 2)} секунд')

for i in range(1, 10):
    print(i, end="  ")
print()

'''

    Програма має просити користувача ввести число від 1 до 9. Якщо користувач ввів число поза цим
    діапазоном — виводити помилку і просити ввести ще раз.

    Використовувати можна тільки 1 input!

'''

number = -1

while number < 1 or number > 9:
    number = int(input('Введіть число від 1 до 9:'))

    if 1 <= number <= 9:
        active = False
    else:
        print('Некоректне введення! Спробуйте ще раз')