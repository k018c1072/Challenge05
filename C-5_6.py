import math
value = int(input('数値＞ '))


def is_prime(n):
    if n == 1:
        return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True


if is_prime(value):
    print('素数です')
else:
    print('素数ではありません')
