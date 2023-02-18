def parse_int(string, numwords={}):
    string = string.replace('-', ' ')
    if not numwords:
        units = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
                "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
                "sixteen", "seventeen", "eighteen", "nineteen"]
        scalesunitsru = ['', 'одна', 'две', 'три']
        unitsru = ["ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь",
                 "девять", "десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать",
                 "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
        tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
        tensru = ["", "", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят",
                  "девяносто"]
        hundredsru = ['', 'сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот',
                     'девятьсот']
        scales = ["hundred", "thousand", "million", "billion", "trillion"]
        scalesru = ["", "тысяча", "миллион", "миллиард", "триллион"]
        unitscalesru = ['тысяч', 'тысячи', 'миллиона', 'миллионов', 'миллиардов', 'миллиарда', 'триллионов',
                        'триллиона']
        numwords["and"] = (1, 0)
        numwords["и"] = (1, 0)
        for idx, word in enumerate(units):
            numwords[word] = (1, idx)
        for idx, word in enumerate(tens):
            numwords[word] = (1, idx * 10)
        for idx, word in enumerate(unitsru):
            numwords[word] = (1, idx)
        for idx, word in enumerate(scalesunitsru):
            numwords[word] = (1, idx)
        for idx, word in enumerate(tensru):
            numwords[word] = (1, idx * 10)
        for idx, word in enumerate(scales):
            numwords[word] = (10 ** (idx * 3 or 2), 0)
        for idx, word in enumerate(scalesru):
            numwords[word] = (1, 10 ** (idx * 3))
        for idx, word in enumerate(hundredsru):
            numwords[word] = (1, idx * 100)
        for word in unitscalesru:
            if 'тысяч' in word:
                numwords[word] = (10 ** 3, 0)
            elif 'миллион' in word:
                numwords[word] = (10 ** 6, 0)
            elif 'миллиард' in word:
                numwords[word] = (10 ** 9, 0)
            elif 'триллион' in word:
                numwords[word] = (10 ** 12, 0)
    current = result = 0
    for word in string.split():
        if word not in numwords:
            raise Exception("Illegal word: " + word)
        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0
    return result + current


print(parse_int('двести двадцать восемь'))
