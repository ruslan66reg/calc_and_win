from math import pi


def calc_area(radius: float) -> float:
    """Возвращает площадь круга."""
    return pi * radius**2


def report(r: float | int) -> None:
    """Печатает площадь круга."""
    print(f"Площадь круга радиусом {r} равна {calc_area(r):.2f}")


if __name__ == '__main__':
    report(3)
