def count_letters(_string):
    small = capital = num = space = 0

    for char in _string:
        ascii_value = ord(char)

        if ascii_value == 32:
            space += 1
        elif 48 <= ascii_value <= 57:
            num += 1
        elif 65 <= ascii_value <= 90:
            capital += 1
        else:
            small += 1

    return [small, capital, num, space]


if __name__ == "__main__":
    strings = []
    while True:
        try:
            _string = input()
            strings.append(_string)
        except EOFError:
            break

    for _string in strings:
        result = count_letters(_string)
        print(" ".join(str(element) for element in result))
