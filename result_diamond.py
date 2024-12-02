import math


class Rhombus:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a  # Використовуємо __setattr__
        self.angle_a = angle_a  # Використовуємо __setattr__

    def __setattr__(self, name, value):
        """Перевірки для атрибутів."""
        if name == "side_a":
            if value <= 0:
                raise ValueError("Сторона ромба повинна бути більше 0.")
        elif name == "angle_a":
            if value <= 0 or value >= 180:
                raise ValueError("Кут ромба повинен бути більше 0 і менше 180 градусів.")
            # Автоматично обчислюємо кут β
            object.__setattr__(self, "angle_b", 180 - value)

        # Встановлюємо значення атрибута
        object.__setattr__(self, name, value)

    def perimeter(self):
        """Обчислює периметр ромба."""
        return 4 * self.side_a

    def info(self):
        """Виводить інформацію про ромб."""
        print(f"Сторона a: {self.side_a}")
        print(f"Кут α: {self.angle_a}°")
        print(f"Кут β: {self.angle_b}°")
        print(f"Периметр: {self.perimeter():.2f}")


# Створюємо ромб
romb = Rhombus(5, 60)
romb.info()
