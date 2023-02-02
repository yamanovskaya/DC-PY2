if __name__ == "__main__":
    # Write your solution here
    class StepperDevice:
        """ Базовый класс устройства с шаговым двигателем.
         @param STEPPER_MODEL_LIST: список доступных моделей ШД
         @param __instance: адрес нового созданного обьекта, созданного методом __new__ базового класса object
         @param obj_counter: счетчик объектов класса
         @param OBJ_MAX_NUM: максимальное количество объектов класса
         """
        STEPPER_MODEL_LIST = ['FL42STH25-0404 A', 'FL42STH25-0404 B', 'FL42STH47-1684M A']
        __instance = None
        obj_counter = 0
        OBJ_MAX_NUM = 5

        def __new__(cls, *args, **kwargs):
            """
            Метод для ограничения количества обьектов одного класса, паттерн Simgleton
            @param args: параметры
            @param kwargs: параметры
            """
            cls.obj_counter += 1
            if cls.obj_counter <= cls.OBJ_MAX_NUM:
                cls.__instance = super().__new__(cls)
            else:
                raise ValueError('too many class objects')
            return cls.__instance

        def __init__(self, name: str, stepper_model: str, axe_len: int, max_speed: int, __move_xy: int = 0):
            """
            Создание и подготовка к работе объекта "Устройство с ШД"
            :@param move_xy: заданная координата, шаг
            :@param name: Название устройства
            :@param stepper_model: Модель используемого ШД, должно быть указано в перечне ШД STEPPER_MODEL_LIST
            :@param axe_len: Диапазон движения относительно нулевого положения, шаг
            :@param max_speed: Максимально допустимая скорость вращения, шаг/c
            """
            self.__move_xy = 0
            self.check_name(name)
            self.check_max_speed(max_speed)
            self.check_stepper_model(stepper_model)
            self.check_axe_len(axe_len)

            self.name = name
            self.stepper_model = stepper_model
            self.axe_len = axe_len
            self.max_speed = max_speed

        @classmethod
        def check_name(cls, value):
            """ Метод для проверки значения атрибута name.
            :@param value: переданное на проверку значение атрибута name
            """
            if not isinstance(value, str):
                raise TypeError('attribute name must have type str')

        @classmethod
        def check_stepper_model(cls, value):
            """ Метод для проверки значения атрибута stepper_model.
            :@param value: переданное на проверку значение атрибута stepper_model"""
            if not isinstance(value, str):
                raise TypeError('attribute stepper_model must have type str')
            if not value in cls.STEPPER_MODEL_LIST:
                raise ValueError('stepper model is not registered in STEPPER_MODEL_LIST')

        @classmethod
        def check_axe_len(cls, value):
            """ Метод для проверки значения атрибута axe_len.
            :@param value: переданное на проверку значение атрибута axe_len"""
            if not isinstance(value, int):
                raise TypeError('attribute axe_len must have type int')

        @classmethod
        def check_max_speed(cls, value):
            """ Метод для проверки значения атрибута max_speed.
            :@param value: переданное на проверку значение атрибута max_speed"""
            if not isinstance(value, int):
                raise TypeError('attribute max_speed must have type int')
            if not 0 <= value < 30000:
                raise ValueError('attribute max_speed is out of range due to acceleration table')

        def __str__(self):
            """ Краткое описание обьекта класса """
            return f'Устройство {self.name}, модель двигателя - {self.stepper_model}'

        def __repr__(self):
            """ Представление обьекта класса в виде строки, по которой можно его создать """
            return f'{self.__class__.__name__}(name={self.name!r}, stepper_model={self.stepper_model!r},' \
                   f' axe_len={self.axe_len!r}, max_speed={self.max_speed!r})'

        def check_move_xy(self, value):
            if type(value) != int:
                raise TypeError('attribute move_xy bust be int')
            if not (1 <= value <= self.axe_len):
                raise ValueError('attribute move_xy is out of range')

        @property
        def move_xy(self):
            """
            Getter __move_xy method
            @return: __move_xy value
            """
            return self.__move_xy

        @move_xy.setter
        def move_xy(self, value):
            """
            Setter __move_xy value
            @param value: new __move_xy value
            @return: None
            """
            self.check_move_xy(value)
            self.__move_xy = value


    class AxesStepper(StepperDevice):
        def __init__(self, name: str, stepper_model: str, axe_len: int = 500, max_speed: int = 5000,
                     detector_num: int = 2):
            """
            Создание и подготовка к работе объекта "Устройство с ШД"
            :@param name: Название устройства
            :@param stepper_model: Модель используемого ШД, должно быть указано в перечне ШД STEPPER_MODEL_LIST
            :@param axe_len: Диапазон движения относительно нулевого положения, шаг
            :@param max_speed: Максимально допустимая скорость вращения, шаг/c
            :@param detector_num: Количество оптопар конечного положения, шт
            """
            super().__init__(name, stepper_model, axe_len, max_speed)
            self.detector_num = detector_num

        def __repr__(self):
            return f'{self.__class__.__name__}(name={self.name!r}, stepper_model={self.stepper_model!r},' \
                   f' axe_len={self.axe_len!r}, max_speed={self.max_speed!r}, detector_num={self.detector_num!r})'

        @classmethod
        def check_axe_len(cls, value):
            """ Метод для проверки значения атрибута axe_len.
            :@param value: переданное на проверку значение атрибута axe_len"""
            super().check_axe_len(value)
            if value > 500:
                raise ValueError('attribute axe_len must be less or equal 500 steps')


    class PumpStepper(StepperDevice):
        def __init__(self, name: str, stepper_model: str, axe_len: int = 500, max_speed: int = 5000,
                     detector_num: int = 2, volume_step: int = 1):
            """
            Создание и подготовка к работе объекта "Устройство с ШД"
            :@param name: Название устройства
            :@param stepper_model: Модель используемого ШД, должно быть указано в перечне ШД STEPPER_MODEL_LIST
            :@param axe_len: Диапазон движения относительно нулевого положения, шаг
            :@param max_speed: Максимально допустимая скорость вращения, шаг/c
            :@param detector_num: Количество оптопар конечного положения, шт
            :@param volume_step: шаг дозирования, 1 мкл
            """
            super().__init__(name, stepper_model, axe_len, max_speed)
            self.detector_num = detector_num
            self.volume_step = volume_step

        def __repr__(self):
            """ Представление обьекта класса в виде строки, по которой можно его создать """
            return f'{self.__class__.__name__}(name={self.name!r}, stepper_model={self.stepper_model!r},' \
                   f' axe_len={self.axe_len!r}, max_speed={self.max_speed!r}, detector_num={self.detector_num!r},' \
                   f'volume_step={self.volume_step!r})'

a1 = StepperDevice(name='X', stepper_model='FL42STH25-0404 A', axe_len=60000, max_speed=5000)
print(a1.__dict__)
a2 = AxesStepper(name='X', stepper_model='FL42STH25-0404 A', axe_len=140, max_speed=5000)
print(a2.__dict__)
a3 = PumpStepper(name='X', stepper_model='FL42STH25-0404 A', axe_len=140, max_speed=5000)
print(a3.__dict__)

a1._StepperDevice__move_xy = 100
print(a1.__dict__)

print(a2)

print(a3.__repr__())

n1 = PumpStepper(name='X', stepper_model='FL42STH25-0404 A', axe_len=140, max_speed=5000)
n2 = PumpStepper(name='X', stepper_model='FL42STH25-0404 A', axe_len=140, max_speed=5000)
n3 = PumpStepper(name='X', stepper_model='FL42STH25-0404 A', axe_len=140, max_speed=5000)
n4 = PumpStepper(name='X', stepper_model='FL42STH25-0404 A', axe_len=140, max_speed=5000)
n5 = PumpStepper(name='X', stepper_model='FL42STH25-0404 A', axe_len=140, max_speed=5000)  # class object №6, but we need <= 5
