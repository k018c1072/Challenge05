seireki = int(input('西暦＞ '))

if seireki % 4 == 0 and seireki % 100 != 0 or seireki % 400 == 0:
    print('うるう年')
else:
    print('平年')
