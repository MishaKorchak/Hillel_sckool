user_input = input("Введіть строку: ")

chars = len(set(user_input))


if chars > 10:
    print(True)
else:
    print(False)