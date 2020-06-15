value = int(input("数値＞ "))
hoge = []

for v in range(1, value + 1):
    if v % 15 == 0:
        hoge.append('FizzBuzz')
    elif v % 3 == 0:
        hoge.append('Fizz')
    elif v % 5 == 0:
        hoge.append('Buzz')
    else:
        hoge.append(v)

print(hoge)
