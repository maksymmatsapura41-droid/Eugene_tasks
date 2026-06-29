# class Mavpa:
#     def __init__(self):
#         self._name = "Mavpa"
#         self._version = "1.0"
#
#     @property
#     def name_xxl(self):
#         return self._name
#
#     @name_xxl.setter
#     def name_xxl(self, value):
#         self._name = value
#
#     def version(self):
#         return self._version
#
#
#
#
# x = Mavpa()
# print(x.name_xxl)
# x.name_xxl = "Mavpa1"
# print(x.name_xxl)
# print(x.version())
import os


# Завдання 1: Інкапсуляція (Система безпеки паролів)
# Контекст: Потрібно створити клас користувача, який зберігає пароль у захищеному (хэшованому) вигляді
# та не дозволяє встановити занадто простий пароль.

# class User:
#     def __init__(self, username, password):
#         self.username = username
#         self.__password = password
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, password):
#         if len(password) < 8:
#             raise ValueError("Password must be at least 8 characters")
#         else:
#             self.__password = hash(password)
#
# xyq = User("xyq", "")
# print(xyq.password)
# # xyq.password = "123"
# # print(xyq.password)
# xyq.password = "1234567890"
# print(xyq.password)


# Завдання 2: Наслідування (Система інфраструктурного моніторингу)
# Контекст: Ви пишете ядро для системи моніторингу серверів (близько до DevOps-тематики).
# Потрібно створити базовий клас для метрик та його специфічних нащадків.
# Створіть базовий клас BaseMetric. Він має приймати name: str та interval: int (секунди між опитуваннями).
# У ньому має бути метод collect_data(), який просто повертає рядок "[Base] Збір базових системних метрик".
# Створіть клас-нащадок CpuMetric. Він наслідує BaseMetric, але додатково приймає параметр core_count: int.
# Створіть клас-нащадок RamMetric. Він наслідує BaseMetric, але додатково приймає параметр total_gb: int.
# Перевизначте метод collect_data() в обох нащадках:
# Вони мають викликати батьківський метод через super().collect_data().
# Додавати до результату свою специфічну інформацію (наприклад: "[Base] ... | CPU Cores:8 " або "[Base] ... | RAM Total: 16GB").
# Напишіть функцію run_monitoring(metrics: list[BaseMetric]),
# яка в циклі проходить по списку метрик (там можуть бути як CPU, так і RAM метрики)
# і викликає для кожної метод collect_data(), виводячи результат у консоль.

# class BaseMetric:
#     def __init__(self, name:str, interval:int):
#         self.name = name
#         self.interval = interval
#
#     def collect_data(self):
#         return "[Base] Збір базових системних метрик"
#
# class CpuMetric(BaseMetric):
#     def __init__(self, core_count: int, name: str, interval: int):
#         super().__init__(name, interval)
#         self.core_count = core_count
#
#     def collect_data(self):
#         return super().collect_data() + f"| CPU Cores: {self.core_count}"
#
# class RamMetric(BaseMetric):
#     def __init__(self, total_gb: int, name: str, interval: int):
#         super().__init__(name, interval)
#         self.total_gb = total_gb
#
#     def collect_data(self):
#         return super().collect_data() + f"| RAM Total:: {self.total_gb}GB"
#
# def run_monitoring(metrics: list[BaseMetric]):
#     for metric in metrics:
#         print(metric.collect_data())
#
# x = [CpuMetric(10, "CPU", 1), RamMetric(10000, "RAM", 1)]
# run_monitoring(x)

# class ResourceCluster:
#     def __init__(self, total_memory: int):
#         self._total_memory = total_memory
#         self._used_memory = 0
#
#     @property
#     def used_memory(self):
#         return self._used_memory
#
#     @used_memory.setter
#     def used_memory(self, value):
#         if value > self._total_memory or value < 0:
#             raise ValueError(f"Некоректний обсяг використаної пам'яті, памʼятьл має бути вмежах від 0 до {self._total_memory}")
#         self._used_memory = value
#
#     @property
#     def memory_load_percentage(self):
#         return self._used_memory / self._total_memory * 100
#
#     @property
#     def is_overloaded(self):
#         return self.memory_load_percentage > 85
#
# x = ResourceCluster(100)
# x.used_memory = 60
# print(x.is_overloaded)
# print(x.memory_load_percentage)
# x.used_memory = 900
# print(x.is_overloaded)
# print(x.memory_load_percentage)


# class SSHRunner:
#     def execute_command(self, command: str):
#         if "sudo" in command:
#             return 1, "Permission denied"
#         return 0, "Success"
#
# class TelegramNotifier:
#     def send_notification(self, message: str):
#         print(f"[TG Bot]: {message}")
#
# class AutomatedDeployment(SSHRunner, TelegramNotifier):
#     def deploy(self, app_name: str, command: str):
#         status_code, output = self.execute_command(command)
#         if status_code == 0:
#             self.send_notification(f"Деплой {app_name} успішний!")
#         else:
#             self.send_notification(f"Помилка деплою {app_name}! Лог: {output}")
#
# x = AutomatedDeployment()
# x.deploy("DEr", "mal")
