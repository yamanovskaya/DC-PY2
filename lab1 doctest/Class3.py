import doctest


class Laser:
    def check_power(self, power: int) -> None:
        if not isinstance(power, int):
            raise TypeError("Мощность - целое число до 1000")
        if power < 0:
            raise ValueError("Мощность - не отрицательное число")
        return

    def check_len(self, len: int) -> None:
        if not isinstance(len, int):
            raise TypeError("Длина волны - целое число")
        if 100 <= len < 0:
            raise ValueError("Длина волны - не отрицательное число до 100 включительно")
        return

    def __init__(self, power: int, len: int):
        """
        Создание и подготовка к работе объекта "Лазер"

        :param power: Выставленная мощность, Вт
        :param len: Длина волны излучения, нм

        Примеры:
        >>> laser = Laser(0, 70)  # инициализация экземпляра класса
        """
        self.check_power(power)
        self.check_len(len)

        self.power = power
        self.len = len

    def is_ready(self) -> bool:
        """
        Функция которая проверяет включен ли лазер

        :return: Лазер включен?

        Примеры:
        >>> laser = Laser(1, 70)  # инициализация экземпляра класса
        >>> laser.is_ready()
        False
        """
        if self.power == 0:
            return True
        return False

    def new_power(self, new_power: int) -> int:
        """
        Функция которая присваивает координате новое значение

        :param new_power: Новая выставленная мощность

        :return: Новая выставленная мощность

        Примеры:
        >>> laser = Laser(1, 70)  # инициализация экземпляра класса
        >>> laser.new_power(100)
        100
        """
        self.check_power(new_power)
        self.power = new_power
        return self.power


if name == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации