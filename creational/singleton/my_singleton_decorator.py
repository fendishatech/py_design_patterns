"""
Pattern name - Singleton
Pattern type - creational Design pattern
"""


def singleton(mySingleton):
    instances = {}

    def getInstances(*args, **kwargs):
        if mySingleton not in instances:
            instances[mySingleton] = mySingleton(*args, **kwargs)

        return instances[mySingleton]

    return getInstances


@singleton
class TestSingletonDecorator():
    x = 10


a = TestSingletonDecorator()
print(f'Initial value : {a.x}')
a.x = 22
print(f'updated value : {a.x}')
b = TestSingletonDecorator()
print(f'new instance with updated value: {b.x}')
print(f'instance one is @ : {a}')
print(f'instance two is @ : {b}')
print(f'instance a and be are equal = { a == b}')
