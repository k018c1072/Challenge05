words = []
first = 'り'
tail = ''

while True:
    word = input('答え＞ ')

    # 最初のしりとりは『り』から始まる
    if not words and word[0] != first:
        print('もう一度答えてください')
        continue

    # 最初以降は一つ前の単語の最後の文字で始まる単語を答える
    if words and tail != word[0]:
        print('もう一度答えてください')
        continue
    else:
        tail = word[-1]

    # すでに答えた単語を答えると負け
    if word in words:
        print('あなたの負けです')
        break

    # 単語の最後が『ん』のものを答えると負け
    if tail == 'ん':
        print('あなたの負けです')
        break

    # 単語を追加
    words.append(word)
