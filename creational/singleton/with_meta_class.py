"""
Pattern name - Singleton (with a meta class using type and __call__ method)
Pattern type - creational Design pattern
"""


class SingletonMeta(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super().__call__(*args, **kwargs)
        return cls.__instances[cls]


class DBConnector(metaclass=SingletonMeta):
    def __init__(self):
        self.status = "Not Connected"

    def connect(self):
        self.status = "Connected"

    def disconnect(self):
        self.status = "Disconnected"


client_one = DBConnector()
print(f"Client 1 db status : {client_one.status}")

client_two = DBConnector()
print(f"Client 2 db status : {client_two.status}")

print(f"connect from client one")
client_one.connect()
print(f"Client 1 db status after connect : {client_one.status}")
print(f"Client 2 db status after connect : {client_two.status}")

print(f"connect from client two")
client_one.disconnect()
print(f"Client 1 db status after connect : {client_one.status}")
print(f"Client 2 db status after connect : {client_two.status}")

print(
    f"checking if object are pointing to same location : {client_two == client_one}")
print(f"checking client one __dict__: {client_two.__dict__}")
print(f"checking client two __dict__: {client_two.__dict__}")
