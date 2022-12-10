import doctest


class Microwave:
    def check_Power(self, power: int) -> None:
        if not isinstance(power, int):
            raise TypeError("Мощность - целое число")
        if power < 0:
            raise ValueError("Мощность - не отрицательное число")
        return

    def check_Time(self, time: int) -> None:
        if not isinstance(time, int):
            raise TypeError("Время готовки - целое число")
        if 15 <= time < 0:
            raise ValueError("Время готовки - не отрицательное число до 15 включительно")
        return

    def __init__(self, power: int, time: int):
        """
        Создание и подготовка к работе объекта "Микроволновка"

        :param power: Выставленная мощность, Вт
        :param time: Выставленное время, мин

        Примеры:
        >>> microwave = Microwave(600, 0)  # инициализация экземпляра класса
        """
        self.check_Power(power)
        self.check_Time(time)

        self.power = power
        self.time = time

    def is_ready(self) -> bool:
        """
        Функция которая проверяет готова ли микроволновка к работе

        :return: Микроволновка закончила греть?

        Примеры:
        >>> microwave = Microwave(600, 0)
        >>> microwave.is_ready()
        True
        """
        if self.time == 0:
            return True
        return False

    def new_time(self, new_time: int) -> int:
        """
        Функция которая присваивает координате новое значение

        :param new_time: Новое выставленное время

        :return: Новое выставленное время

        Примеры:
        >>> microwave = Microwave(600, 0)
        >>> microwave.new_time(10)
        10
        """
        self.check_Time(new_time)
        self.time = new_time
        return self.time


if name == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации