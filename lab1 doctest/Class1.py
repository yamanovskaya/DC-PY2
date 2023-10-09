import doctest


class Positioner:
    def check_coordX(self, coord: int) -> None:
        if not isinstance(coord, int):
            raise TypeError("Координата X - целое число")
        if coord < 0:
            raise ValueError("Координата X - не отрицательное число")
        return

    def check_coordY(self, coord: int) -> None:
        if not isinstance(coord, int):
            raise TypeError("Координата Y - целое число")
        if coord < 0:
            raise ValueError("Координата Y - не отрицательное число")
        return

    def __init__(self, x_coord: int, y_coord: int, busy_flag: bool):
        """
        Создание и подготовка к работе объекта "Позиционер"

        :param x_coord: Координата оси X относительно нулевого положения
        :param y_coord: Координата оси Y относительно нулевого положения
        :param busy_flag: Флаг занятости занят/в движении-true, свободен-false

        Примеры:
        >>> positioner = Positioner(500, 0, False)  # инициализация экземпляра класса
        """
        self.check_coordX(x_coord)
        self.check_coordY(y_coord)
        if not isinstance(busy_flag, bool):
            raise TypeError("Флаг - логический тип bool")

        self.x_coord = x_coord
        self.y_coord = y_coord
        self.busy_flag = busy_flag

    def is_null_position(self) -> bool:
        """
        Функция которая проверяет находится ли позиционер в нулевой точке

        :return: Позиционер в нулевой точке?

        Примеры:
        >>> positioner = Positioner(500, 0, False)
        >>> positioner.is_null_position()
        False
        >>> positioner = Positioner(0, 0, False)
        >>> positioner.is_null_position()
        True
        """
        if self.x_coord == 0 and self.y_coord == 0:
            return True
        return False

    def new_pos(self, new_x: int, new_y: int) -> tuple:
        """
        Функция которая присваивает координате новое значение

        :param new_x: Координата оси X относительно нулевого положения
        :param new_y: Координата оси Y относительно нулевого положения

        :return: Новые координаты

        Примеры:
        >>> positioner = Positioner(500, 0, False)
        >>> positioner.new_pos(1,1)
        (1, 1)
        """
        self.check_coordX(new_x)
        self.check_coordY(new_y)
        self.x_coord = new_x
        self.y_coord = new_y
        return self.x_coord, self.y_coord


if name == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации