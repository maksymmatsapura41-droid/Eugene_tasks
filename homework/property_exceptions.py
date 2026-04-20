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
import datetime
from abc import ABC, abstractmethod


class SensorCriticalError(Exception):
    pass


class BaseSensor(ABC):
    def __init__(self, threshold):
        self.threshold = threshold

    @abstractmethod
    def read_data(self):
        pass

    def log_status(self):
        return f"Status: The sensor is operating normally."

    @property
    def threshold(self):
        return self._threshold

    @threshold.setter
    def threshold(self, value):
        if value < 0:
            raise ValueError("The threshold cannot be negative!")
        self._threshold = value

    def __str__(self):
        return f"Sensor: {self.__class__.__name__} (The threshold: {self.threshold})"

    def __eq__(self, other):
        if not isinstance(other, BaseSensor):
            return False
        return self.__class__ == other.__class__ and self.threshold == other.threshold


class TemperatureSensor(BaseSensor):
    def read_data(self):
        value = random.randint(15, 100)
        if value > self.threshold:
            raise SensorCriticalError(f"Critical temperature: {value}°C (The threshold: {self.threshold})")
        return value


class PressureSensor(BaseSensor):
    def read_data(self):
        value = round(random.uniform(1.0, 5.0), 1)
        if value > self.threshold:
            raise SensorCriticalError(f"Critical pressure: {value} bar (Threshold: {self.threshold})")
        return value


def analyze_sensor(sensor):
    print(f"--- Analise: {sensor} ---")
    try:
        data = sensor.read_data()
        print(f"Current value: {data}")
        print(sensor.log_status())
    except SensorCriticalError as e:
        error_msg = f"[{datetime.datetime.now()}] CRITICAL ERROR: {e}"
        print(error_msg)

        with open("sensor_log.txt", "a", encoding="utf-8") as file:
            file.write(error_msg + "\n")
    print("-" * 30)


t_sensor = TemperatureSensor(threshold=70)
p_sensor = PressureSensor(threshold=3.5)
p_sensor_duplicate = PressureSensor(threshold=3.5)
