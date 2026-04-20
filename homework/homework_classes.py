"""
Опис завдання
Уяви, що ти розробляєш просту систему моніторингу ІТ-інфраструктури.
Існують різні типи серверів — вебсервери, бази даних, файлові сервери.
Усі вони мають спільні параметри (назва, IP-адреса, статус), але водночас
кожен має свої специфічні метрики.

1. Створи базовий клас Server, який має:
Захищені атрибути: _name, _ip, _status.
Метод info(): повертає коротку інформацію про сервер.
Метод ping(): імітує перевірку зв'язку (наприклад, повертає рядок "Server <name> is online").
2. Реалізуй інкапсуляцію для _status:
Дозволені значення: "running" або "stopped".
Якщо встановлюється інше значення — вивести повідомлення про помилку.
3. Створи класи-спадкоємці:
WebServer(Server) — додає приватний атрибут __requests_per_minute.
DatabaseServer(Server) — додає приватний атрибут __active_connections.
FileServer(Server) — додає приватний атрибут __storage_usage.
4. У кожному класі-спадкоємці:
Перевизнач метод info(), щоб він відображав також і специфічні метрики конкретного типу сервера.
"""

class Server:
    def __init__(self, name: str, ip: str, status: bool):
        self._name = name
        self._ip = ip
        if status:
            self._status = "running"
        elif not status:
            self._status = "stopped"

    def info(self):
        return f"Server {self._name}, ip: {self._ip}, status:{self._status}"

    def ping(self):
        return f"Server {self._name} is {self._status}"


class WebServer(Server):
    def __init__(self, name, ip, status, requests_per_minute):
        super().__init__(name, ip, status)
        self.__requests_per_minute = requests_per_minute

    def info(self):
        return f"{super().info()}, requests per minute: {self.__requests_per_minute}"


class DatabaseServer(Server):
    def __init__(self, name, ip, status, active_connections):
        super().__init__(name, ip, status)
        self.__active_connections = active_connections

    def info(self):
        return f"{super().info()}, active connections: {self.__active_connections}"


class FileServer(Server):
    def __init__(self, name, ip, status, storage_usage):
        super().__init__(name, ip, status)
        self.__storage_usage = storage_usage

    def info(self):
        return f"{super().info()}, storage usage: {self.__storage_usage}"


ser = Server("digger", "1.2.3.4", True)
print(ser.info())
print(ser.ping())
webser = WebServer("nigger", "1.4.8.8", True, 10)
print(webser.info())
print(webser.ping())
fileser = FileServer("singer", "6.6.6", False, 1000)
print(fileser.info())
print(fileser.ping())