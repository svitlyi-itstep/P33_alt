def function(count):
    if count <= 0:
        return
    print(f'Hello! {count=}')
    function(count - 1)
    print(f'Bye! {count=}')


function(5)

# 5! = 1 * 2 * 3 * 4 * 5
# n! = 1 * 2 * ... * n

# 5! = 5 * 4!
# n! = n * n-1!
# 0! = 1

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(f'{factorial(5)=}')





# 5 ^ 3 = 5 * 5 * 5
# x ^ n = x * x * x

# 5 ^ 3 = 5 * 5 ^ 2
# x ^ n = x * x ^ n - 1


# sum(1, 5) = 1 + sum(2, 5)
# a + sum(a - 1, b)