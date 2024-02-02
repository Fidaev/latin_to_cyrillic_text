def latin_to_cyrillic_text(text):
    latin_to_cyrillic = {
        'a': 'а',
        'A': 'А',
        'b': 'б',
        'B': 'Б',
        'c': 'с',
        'C': 'С',
        'd': 'д',
        'D': 'Д',
        'e': 'е',
        'E': 'Е',
        'f': 'ф',
        'F': 'Ф',
        'g': 'г',
        'G': 'Г',
        'h': 'x',
        'H': 'X',
        'i': 'и',
        'I': 'И',
        'j': 'ж',
        'J': 'Ж',
        'k': 'к',
        'K': 'К',
        'l': 'л',
        'L': 'Л',
        'm': 'м',
        'M': 'М',
        'n': 'н',
        'N': 'Н',
        'o': 'о',
        'O': 'О',
        'p': 'п',
        'P': 'П',
        'q': 'к',
        'Q': 'К',
        'r': 'р',
        'R': 'Р',
        's': 'с',
        'S': 'С',
        't': 'т',
        'T': 'Т',
        'u': 'у',
        'U': 'У',
        'v': 'в',
        'V': 'В',
        'x': 'х',
        'X': 'Х',
        'y': 'й',
        'Y': 'Й',
        'z': 'з',
        'Z': 'З',
        'sh': 'ш',
        'Sh': 'Ш',
        'ch': 'ч',
        'Ch': 'Ч',
        'y\'': 'й',
        'Y\'': 'Й',
        'ya': 'я',
        'Ya': 'Я',
        'yu': 'ю',
        'Yu': 'Ю',
        'yo': 'ё',
        'TS': 'Ц',
        'Ts': 'Ц',
        'ts': 'ц',
        'Yo': 'Ё'
    }

    cyrillic_text = ''
    i = 0
    while i < len(text):
        if i + 1 < len(text) and text[i:i + 2] in latin_to_cyrillic:
            cyrillic_text += latin_to_cyrillic[text[i:i + 2]]
            i += 2
        elif text[i] in latin_to_cyrillic:
            cyrillic_text += latin_to_cyrillic[text[i]]
            i += 1
        else:
            cyrillic_text += text[i]
            i += 1
    print(cyrillic_text)


def main():
    latin_to_cyrillic_text("text")


if __name__ == '__main__':
    main()
