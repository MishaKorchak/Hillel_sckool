import unittest
from turtle import width


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)  # Викликаємо конструктор Employee явно
        self.department = department


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name, salary)  # Викликаємо конструктор Employee явно
        self.programming_language = programming_language


class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        Manager.__init__(self, name, salary, department)  # Явно викликаємо Manager.__init__
        Developer.__init__(self, name, salary, programming_language)  # Явно викликаємо Developer.__init__
        self.team_size = team_size




from abc import ABC, abstractmethod
import math

# Абстрактний клас "Фігура"
class Shape(ABC):
    @abstractmethod
    def area(self):
        """Метод для обчислення площі."""
        pass

    @abstractmethod
    def perimeter(self):
        """Метод для обчислення периметру."""
        pass

# Клас для прямокутника
class Rectangle(Shape):
    def __init__(self, width, height):
        self.__width = width  # Приватна властивість
        self.__height = height  # Приватна властивість

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)

# Клас для кола
class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius  # Приватна властивість

    def area(self):
        return math.pi * (self.__radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.__radius

# Клас для трикутника
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.__a = a  # Приватна властивість
        self.__b = b  # Приватна властивість
        self.__c = c  # Приватна властивість

        # Перевірка, чи можливо утворити трикутник
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError("Сторони не можуть утворити трикутник.")

    def area(self):
        s = self.perimeter() / 2  # Півпериметр
        return math.sqrt(s * (s - self.__a) * (s - self.__b) * (s - self.__c))

    def perimeter(self):
        return self.__a + self.__b + self.__c

# Створення об'єктів фігур
shapes = [
    Rectangle(4, 5),
    Circle(3),
    Triangle(3, 4, 5)
]

# Обчислення та виведення площі та периметру для кожної фігури
for shape in shapes:
    print(f"{shape.__class__.__name__}:")
    print(f"  Площа: {shape.area():.2f}")
    print(f"  Периметр: {shape.perimeter():.2f}")
    print()
