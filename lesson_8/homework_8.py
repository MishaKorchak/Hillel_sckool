
def sum_string(string):
    try:
        numbers = (int(num) for num in string.split(','))
        return sum(numbers)
    except ValueError:

        return "Не можу це зробити!"


strings = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]


for string in strings:
    result = sum_string(string)
    print(result)




