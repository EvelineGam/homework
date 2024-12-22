import math

def is_prime(func):
    def wrapper(*args):
        x = func(*args)
        calc = 0
        if x > 1:
            for i in range(2, (x // 2 + 1)):
                if x % i == 0 and x!= 2:
                    calc += 1
            if calc > 0:
                print('Составное')
            else:
                print('Простое')
        return x
    return wrapper

@is_prime
def sum_three(*args):
    return sum(args)

result = sum_three(2, 3, 6)
print(result)
