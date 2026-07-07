# # # # # 1.Знайди баг, поясни, чому він виникає, і перепиши цей код, використовуючи dataclasses та
# # # # # строгу типізацію (Type Hints). Також додай метод для безпечного додавання предметів.
# # # #
# # # #
# # # # # class SupplyCrate:
# # # # #     def __init__(self, crate_id, destination="Mars Base", items=[]):
# # # # #         self.crate_id = crate_id
# # # # #         self.destination = destination
# # # # #         self.items = items
# # # # #         self.is_sealed = False
# # # # #
# # # # #     def seal_crate(self):
# # # # #         self.is_sealed = True
from dataclasses import dataclass, field

@dataclass
class SupplyCrate:
    crate_id: str
    destination_address: str = "Mars Base"
    items: list = field(default_factory=list)
    is_sealed: bool = field(default=False, init=False)

    def seal_crate(self):
        self.is_sealed = True

    def items_add(self, value: list):
        if not self.is_sealed:
            self.items.append(value)

# # # 2. Код написаний процедурно, без інкапсуляції, і рівень заряду батареї можна випадково зробити
# # # від'ємним або більше 100%. Треба нормально переписати + намутити спадкування і використати поліморфізм для move
# # #
# # # class Drone:
# # #     def __init__(self, model, battery):
# # #         self.model = model
# # #         self.battery = battery # Треба захистити!
# # #         self.drone_type = "Generic"
# # #
# # #     def move(self, distance):
# # #         print("Дрон летить...")
# # #         self.battery -= distance * 5
# # #         print(f"Заряд: {self.battery}")
# #
from abc import ABC, abstractmethod


class Drone(ABC):
    @abstractmethod
    def __init__(self, model, drone_type):
        self.model = model
        self._battery = 100
        self.drone_type = drone_type

    @abstractmethod
    def move(self, distance) -> None:
        pass

    @property
    def battery(self) -> int:
        return self._battery

    @battery.setter
    def battery(self, new_battery: int) -> None:
        if new_battery > 100:
            self._battery = 100
        elif new_battery < 0:
            self._battery = 0
            raise CriticalBatteryError("Critical Battery Error, go back home")
        else:
            self._battery = new_battery


class FPVDrone(Drone):
    def __init__(self, model):
        super().__init__(model, "FPV")

    def move(self, distance) -> None:
        print("Дрон летить...")
        self.battery -= distance * 5
        print(f"Заряд: {self.battery}")


class SeaDrone(Drone):
    def __init__(self, model):
        super().__init__(model, "Sea")

    def move(self, distance) -> None:
        print("Дрон буль буль...")
        self.battery -= distance * 2
        print(f"Заряд: {self.battery}")


# # Напиши контекстний менеджер AirlockProtocol.
# # При вході він повинен викликати system.depressurize() і system.open_door().
# # При виході (навіть якщо сталася помилка) він обов'язково має викликати system.close_door() і system.pressurize().
# # Якщо всередині стається виключення MinorSuitGlitch (створи його), контекстний менеджер має просто вивести попередження
# # і погасити помилку (щоб програма йшла далі). Всі інші помилки мають прокидатися вище.»
#
#
#
class AirlockSystem:
    def depressurize(self): print("Відкачування повітря...")

    def pressurize(self): print("Нагнітання повітря...")

    def open_door(self): print("Шлюз ВІДКРИТО.")

    def close_door(self): print("Шлюз ЗАКРИТО.")


class MinorSuitGlitch(Exception):
    pass


class AirlockProtocol:
    def __init__(self, system: AirlockSystem):
        self.system = system

    def __enter__(self):
        self.system.depressurize()
        self.system.open_door()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.system.close_door()
        self.system.pressurize()
        if exc_type is MinorSuitGlitch:
            print("Minor Suir Glitch")
            return True
        if exc_type is CriticalBatteryError:
            print("Critical Battery Error, go back home")
            return True
        return False






system = AirlockSystem()




def eva_mission():
    with AirlockProtocol(system):
        print("Астронавт вийшов у космос...")
        raise MinorSuitGlitch("Шлюз залишився відкритим!")


try:
    eva_mission()
except Exception as e:
    print(f"Аварія: {e}")

# 4. Зібрати попередні таски разом:
# Напиши цикл while, який бере завдання з черги.
# Використовуй контекстний менеджер з Етапу 3 для кожної операції виходу дрона з бази.
# Якщо під час виконання завдання дрон викидає CriticalBatteryError, перехопи цю помилку,
# відправ дрон на "зарядку" (віднови батарею до 100%) і поверни завдання назад у чергу для повторного виконання.
# Цикл має працювати, поки черга не спорожніє

# ШАБЛОН
tasks_queue = [
    {"id": 1, "distance": 15, "type": "scout"},
    {"id": 2, "distance": 40, "type": "mine"},
    {"id": 3, "distance": 10, "type": "scout"}
]

class CriticalBatteryError(Exception):
    pass
# Створи двох дронів (Scout та Miner) тут.
fpv_drone = FPVDrone("FPV1")
sea_drone = SeaDrone("Sea")
# Напиши логіку виконання черги завдань тут.
while True:
    task = tasks_queue.pop(0)
    current_drone = fpv_drone if task["type"] == "scout" else sea_drone
    try:
        current_drone.move(distance=task["distance"])
    except CriticalBatteryError:
        print("Critical Battery Error, go back home")
        current_drone.battery = 100
        tasks_queue.append(task)

# Пам'ятай про безпечний вихід через AirlockProtocol та обробку розрядженої батареї!


