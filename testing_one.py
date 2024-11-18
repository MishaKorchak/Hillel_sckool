def numbers(a ,b):
    return a == b,a < b,a > b,a % b
print(numbers(1000,300))

def is_more_than_ten(unique_chars_count):

    if unique_chars_count > 10:
        return True
    else:
        return False


user_input = input("Введіть строку: ")


unique_chars_count = len(set(user_input))


result = is_more_than_ten(unique_chars_count)

# Вивід результату
print(f"Унікальних символів: {unique_chars_count}")
print(f"Результат перевірки (більше 10): {result}")
