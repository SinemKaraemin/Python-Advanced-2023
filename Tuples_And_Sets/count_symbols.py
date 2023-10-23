text = list(input())
counter = {letter: text.count(letter) for letter in text}

for k, v in sorted(counter.items()):
    print(f'{k}: {v} time/s')
