class Tyre:
    def __init__(self, width: int, height: int, diameter: int):
        """
        Создание и подготовка к работе объекта "Шина"

        :param width: Ширина шины
        :param height: Высота профиля
        :param diameter: Диаметр диска (в дюймах)

        Примеры:
        >>> tyre = Tyre(205, 55, 16)
        """

        if not isinstance(width, int):
            raise TypeError('Значение ширины должно быть целым числом')
        if not isinstance(height, int):
            raise TypeError('Значение высоты должно быть целым числом')
        if not isinstance(diameter, int):
            raise TypeError('Значение диаметра должно быть целым числом')
        if (width <= 0) or (height <= 0) or (diameter <= 0):
            raise ValueError('Некорректное значение аттрибута(ов) (значения должны быть больше 0)')
        self.width = width
        self.height = height
        self.diameter = diameter

    def __str__(self):
        return f'Шина {self.width}/{self.height} R{self.diameter}'

    def __repr__(self):
        return f'{self.__class__.__name__}(width={self.width}, height={self.height}, diameter={self.diameter}'

    def current_pressure(self) -> float:
        """
        Метод, который проверяет давление в колесе

        :return: Давление в колесе
        """
        ...

    def repair_tyre(self) -> None:
        """Метод, который ремонтирует шину"""
        ...


class WinterTyre(Tyre):
    def __init__(self, width: int, height: int, diameter: int, studded: bool):
        """
        Создание и подготовка к работе объекта "Шина"

        :param width: Ширина шины
        :param height: Высота профиля
        :param diameter: Диаметр диска (в дюймах)
        :param studded: Шипованное ли колесо

        Примеры:
        >>> tyre = WinterTyre(205, 55, 16, True)
        """
        if not isinstance(width, int):
            raise TypeError('Значение ширины должно быть целым числом')
        if not isinstance(height, int):
            raise TypeError('Значение высоты должно быть целым числом')
        if not isinstance(diameter, int):
            raise TypeError('Значение диаметра должно быть целым числом')
        if (width <= 0) or (height <= 0) or (diameter <= 0):
            raise ValueError('Некорректное значение аттрибута(ов) (значения должны быть больше 0)')
        super().__init__(width, height, diameter)
        self.studded = studded

    def __str__(self):  # Перегружаем метод, так как изменяется возвращаемая строка
        return f'Зимняя шина {self.width}/{self.height} R{self.diameter}'

    def __repr__(self):  # Перегружаем метод, так как добавился новый атрибут
        return f'{self.__class__.__name__}(width={self.width}, height={self.height}, diameter={self.diameter}, \
        studded={self.studded}'

    def repair_tyre(self) -> None:
        """
        Метод, который ремонтирует шину, а также, если шина является
        шипованной, то выполняет дошиповку
        """
        ...


if __name__ == "__main__":
    pass
