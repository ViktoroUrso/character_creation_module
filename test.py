from math import sqrt


message: str = 'Добро пожаловать в самую лучшую программу для вычисления '
'квадратного корня из заданного числа'

print(message)


def CalculateSquareRoot(Number: float) -> float:
    """ Вычисляет квадратный корень"""
    return sqrt(Number)


def calc(your_number: float) -> None:
    if your_number <= 0:
        return

    print(f"Мы вычислили квадратный корень из введённого вами числа."
          f"Это будет: {CalculateSquareRoot(your_number)}")


print(message)
calc(25.5)
