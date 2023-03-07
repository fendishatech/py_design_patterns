"""
Pattern name - Singleton (with a decorator class using __call__ method)
Pattern type - creational Design pattern
"""


class SingletonDecorator(object):
    def __init__(self, klass) -> None:
        self.klass = klass
        self.instance = None

    def __call__(self, *args, **kwargs):
        if self.instance == None:
            self.instance = self.klass(*args, **kwargs)
        return self.instance


@SingletonDecorator
class Logger (object):
    def __init__(self) -> None:
        self.start = None

    def write(self, message):
        if self.start:
            print(self.start, message)
        else:
            print(message)


logger_one = Logger()
logger_one.start = "# >"
print(f"Logger 1 : {logger_one}")
logger_one.write("object one created.")

logger_two = Logger()
logger_two.start = "$ >"
print(f"Logger 1 : {logger_two}")
logger_two.write("object two created, changing the prompt icon.")


print(f"checking change is shared with : {logger_two.start}")
print(
    f"checking if object are pointing to same location : {logger_two == logger_one}")
print(f"checking logger one __dict__: {logger_two.__dict__}")
print(f"checking logger two __dict__: {logger_two.__dict__}")
