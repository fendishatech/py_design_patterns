"""
Pattern name - Singleton (Mono (shared dict of attributes between two objects) State way)
Pattern type - creational Design pattern
"""


class Borg(object):
    _shared = {}

    def __init__(self) -> None:
        self.__dict__ = self._shared


class Singleton(Borg):
    def __init__(self, num, name) -> None:
        Borg.__init__(self)
        self.num = num
        self.name = name


a = Singleton(12, "bella")
print(f'Initial value : {a.num}')
print(f'Initial value : {a.name}')
b = Singleton(12, "newName")
print(f'new instance with updated value: {b.num}')
print(f'new instance with updated value: {b.name}')
print("# ----------------------------- after update---------------------------- #")
print(f'updated value at singleton instance one value : {a.name}')
print("# ----------------------------- objects memory ---------------------------- #")
print(f'instance one is @ : {a}')
print(f'instance two is @ : {b}')
print("# ----------------------------- objects __dict__---------------------------- #")
print(f'instance_one.__dict__ = {a.__dict__}')
print(f'instance_two.__dict__ = {b.__dict__}')
print("# ----------------------------- objects equality ---------------------------- #")
print(f'instance a and be are equal = { a == b}')
