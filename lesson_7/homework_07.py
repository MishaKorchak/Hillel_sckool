# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= number:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > "25":
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multi  += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15

_____________________________________________________________________________________
                                    ##Вірний код такий  :
def multiplication_table(number):
    # Ініціалізуємо змінну множника
    multiplier = 1

    # Оновлюємо умову циклу
    while True:
        result = number * multiplier

        # Якщо результат більше 25, виходимо з циклу
        if result > 25:
            break

        # Друкуємо результат
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Збільшуємо значення множника
        multiplier += 1
# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum(a,b):
    return a + b
print(sum(50,100))

lambda_sum = lambda a,b: a + b
print(lambda_sum(a=50,b=50))

_____________________________________________________________________________________
# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

numbers = [1, 2, 3, 4, 5]
average = calculate_average(numbers)
print(average)
_____________________________________________________________________________________
# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def revers(s):
    return s[::-1]
result = revers("Hello my first programm")
print(result)
_____________________________________________________________________________________
# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def find_longest_word(words):
    if not words:
        return False
    return max(words,key=len)
words = ["apple", "banana", "cherry", "date", "elderberry"]
longest_word = find_longest_word(words)
print(longest_word)
_____________________________________________________________________________________
# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):

    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
"1.У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
"Скільки всього дерев посадили в саду""

def calculate_total_trees(apple_trees):
    pear_trees = apple_trees + 5 # Кількість груш - на 5 більше, ніж яблунь
    plum_trees = apple_trees - 2  # Кількість слив - на 2 менше, ніж яблунь
    total_trees = apple_trees + pear_trees + plum_trees # Обчислюємо загальну кількість дерев
    return total_trees
apple_trees = 4  # Кількість яблунь
total = calculate_total_trees(apple_trees)
print("Всього дерев у саду:", total)  # Виведе: Всього дерев у саду: 15

_____________________________________________________________________________________



