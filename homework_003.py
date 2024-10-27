alice_in_wonderland = '"Would you tell me ' please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

# Task 01: Define the variable with multiple lines
from tomlkit import string

alice_in_wonderland = '''"Would you tell me ' please, which way I ought to go from here?"
"That depends a good deal on where you want to get to," said the Cat.
"I don't much care where ——" said Alice.
"Then it doesn't matter which way you go," said the Cat.
"—— so long as I get somewhere," Alice added as an explanation.
"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'''

# Task 02: Find and display all single quote characters (')
single_quotes_indices = [index for index, char in enumerate(alice_in_wonderland) if char == "'"]
print("Indices of single quotes:", single_quotes_indices)

# Task 03: Print the variable
print(alice_in_wonderland)


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
    
#Додавання 
a = 100
b = 500
result = a + b
print(f"Сума чисел {a} + {b} дорівнює {result}.")
Сума чисел 100 і 500 дорівнює 600.

#Віднімання
a = 500 
b = 100 
result = a - b 
print(f" {a} - {b} {result}.")
 500  100 400.
 
#Множення 
a = 1000
a = 5000
b = 10000
result = b * a
print(f"{a} множення {b} дорівнює {result}.")
5000 * 10000 = 50000000.

#Ділення

aple = 500
pear = 5555
result = aple / pear
print(f"{aple} ділемо на {pear} дорівнює{result}.")
500 ділемо на 5555 дорівнює0.09000900090009001.


"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?

black_see =436.402
azov_see = 37.800
result = black_see * azov_see
print(f"{black_see} * {azov_see} площа морів {result}.")
436.402 * 37.8 площа морів 16495.9956.
"""


# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
# Загальна кількість товарів
total_product = 375291
# Сума товарів на першому та другому складах
first_sum = 250449
# Сума товарів на другому та третьому складах
second_third = 222950
# Обчислення кількості товарів на складах
# Перший склад (x)
x = total_product - second_third  # Кількість товарів на першому складі
# Другий склад (y)
y = first_sum - x                  # Кількість товарів на другому складі
# Третій склад (z)
z = second_third - y                # Кількість товарів на третьому складі
# Виведення результатів
print(f"Кількість товарів на першому складі: {x}.")
print(f"Кількість товарів на другому складі: {y}.")
print(f"Кількість товарів на третьому складі: {z}.")
Кількість товарів на першому складі: 152341.
Кількість товарів на другому складі: 98108.
Кількість товарів на третьому складі: 124842.

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
# Вхідні дані
monthly_payment = 1179  # Місячний платіж в грн
duration_years = 1.5    # Тривалість сплати в роках
# Переведення тривалості сплати в місяці
duration_months = duration_years * 12
# Обчислення вартості комп'ютера
total_cost = monthly_payment * duration_months
# Вивід результату
print(f"Вартість комп'ютера дорівнює {total_cost} грн.")
Вартість комп'ютера дорівнює 21222.0 грн.

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9

print(f"8019 : 8 остача = {a}")
print(f"9907 : 9 остача = {b}")
print(f"2789 : 5 остача = {c}")
print(f"7248 : 6 остача = {d}")
print(f"7128 : 5 остача = {e}")
print(f"19224 : 9 остача = {f}")
8019 : 8 остача = 3
9907 : 9 остача = 7
2789 : 5 остача = 4
7248 : 6 остача = 0
7128 : 5 остача = 3
19224 : 9 остача = 0

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
pizza_big = 274
pizza_small = 218
juce = 35
cupckace = 350
woter = 21
result = pizza_big + pizza_small + juce + cupckace + woter
print(F"{result}  скільки потрібно коштів ")
898  скільки потрібно коштів

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""


# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?