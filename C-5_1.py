value = int(input("数値＞ "))
divisor = []  # 約数
for v in range(1, value + 1):
    if value % v == 0:
        divisor.append(v)

print(divisor)
