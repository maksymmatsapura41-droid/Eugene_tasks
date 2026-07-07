import asyncio
from dataclasses import dataclass
from enum import Enum
from typing import List


class Role(Enum):
    CAPTAIN = "CAPTAIN"
    SCIENTIST = "SCIENTIST"
    ENGINEER = "ENGINEER"

@dataclass(frozen=True)
class Astronaut:
    name: str
    role: Role
    oxygen_consumption: int = 20

    def __post_init__(self):
        if self.oxygen_consumption <= 0:
            raise ValueError("Oxygen consumption must be positive")

class AsyncAirlockChamber:
    def __init__(self, astronaut: Astronaut):
        self.astronaut = Astronaut

    async def __aenter__(self):
        await asyncio.sleep(1)

    async def __aexit__(self):
        await asyncio.sleep(1)
        print("Нагнітання тиску")

class SpaceModule:
    def __init__(self, crew: List[Astronaut], max_capacity: int):
        self._crew = crew
        self.max_capacity = max_capacity

    def add_astronaut(self, astronaut: Astronaut):
        if self.max_capacity > len(self._crew):
            self._crew.append(astronaut)
        else:
            raise ValueError("Capacity exceeded")

    def get_astronauts(self):
        return self._crew

    def remove_astronauts(self, astronaut: Astronaut):
        self._crew.remove(astronaut)

    def has_role(self, role: Role):
        return any(crew.role == role for crew in self._crew)


# Головна станція (SpaceStation): Об'єднує модулі. Має асинхронний метод start_life_support_monitor(duration),
# який кожні 1.5 секунди поліморфно збирає дані про загальне споживання кисню, не блокуючи роботу інших систем.

class ScienceModule(SpaceModule):
    def __init__(self, crew: List[Astronaut], max_capacity: int):
        super().__init__(crew, max_capacity)

    async def run_quantum_simulation(self, steps):
        try:
            await asyncio.sleep(1)
        except asyncio.CancelledError:
            raise

class CommandModule(SpaceModule):
    def __init__(self, crew: List[Astronaut], max_capacity: int):
        super().__init__(crew, max_capacity)

    async def initiate_hyperjump(self):
        if self.has_role(Role.CAPTAIN):
            await asyncio.sleep(2)
        else:
            raise ValueError("WHERE IS CAPTAIN")

class SpaceStation:
    def __init__(self):
        self._modules: List[SpaceModule] = []

    def add_module(self, module: SpaceModule):
        self._modules.append(module)
