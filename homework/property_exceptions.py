# Потрібно розробити прототип системи для управління датчиками на заводі. Кожен датчик має унікальну логіку обробки даних, але всі вони повинні підпорядковуватися загальним правилам.
# Основні вимоги:
# Абстракція:
    # Створи абстрактний клас BaseSensor.
    # Він повинен містити абстрактний метод read_data(), який повертає випадкове число (імітація зчитування).
    # Додай звичайний метод log_status(), який виводить повідомлення про роботу датчика.
# Поліморфізм:
    # Реалізуй два класи-нащадки: TemperatureSensor та PressureSensor.
    # Перевизнач метод read_data(): для температури значення має бути в межах від 15 до 100, для тиску — від 1.0 до 5.0.
    # Створи функцію analyze_sensor(sensor), яка приймає будь-який датчик і викликає його методи, демонструючи однаковий інтерфейс для різних типів.
# Property:
    # У класах датчиків додай приватний атрибут _threshold (поріг спрацювання).
    # Використовуй @property для отримання значення порогу.
    # Створи @threshold.setter, який буде перевіряти, щоб поріг не був від’ємним
# (якщо значення некоректне - виводити попередження або піднімати помилку).
# Exceptions (Винятки):
    # Створи власний клас винятку SensorCriticalError.
    # Під час зчитування даних, якщо отримане значення перевищує threshold, програма повинна "викинути" (raise) цей виняток.
# Dunder methods (Магічні методи):
    # Реалізуй __str__ для гарного виводу інформації про датчик (назва та поточний поріг).
    # Реалізуй __eq__ (comparison), щоб можна було порівняти два датчики за їхнім типом та порогом.
# Files (Робота з файлами):
    # Реалізуй механізм запису логів. Щоразу, коли стається SensorCriticalError, опис помилки та час мають записуватися
# у файл sensor_log.txt.
    # Використовуй конструкцію with open(...) для безпечної роботи з файлом.
import random
from abc import ABC, abstractmethod


class SensorCriticalError(Exception):
    pass


class AbstractBaseSensor(ABC):
    @abstractmethod
    def read_data(self):
        pass

    def log_status(self):
        return "Arbeiten"


class TemperatureSensor(AbstractBaseSensor):
    def __init__(self, threshold):
        self._threshold = threshold

    def read_data(self):
        print(f"Temperature: {random.randint(15, 100)}")

    @property
    def threshold(self):
        return self._threshold

    @threshold.setter
    def threshold(self, value):
        if value < 0:
            raise ValueError("Threshold can't be negative")
        self._threshold = value


class PressureSensor(AbstractBaseSensor):
    def __init__(self, threshold):
        self._threshold = threshold

    def read_data(self):
        print(f"Pressure: {random.randint(1, 5) + random.random()}")

    @property
    def threshold(self):
        return self._threshold

    @threshold.setter
    def threshold(self, value):
        if value < 0:
            raise ValueError("Threshold can't be negative")
        self._threshold = value


def analyze_sensor(sensor):
    print(f"Data status: {sensor.log_status()}")
    print(f"Data string: {sensor.read_data()}")


temp = TemperatureSensor(threshold=70)
pressure = PressureSensor(threshold=3.5)

analyze_sensor(temp)
analyze_sensor(pressure)