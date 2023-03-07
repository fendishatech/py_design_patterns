"""
Pattern name - Singleton
Pattern type - creational Design pattern
"""

# With __new__() instance making method


class MySingleton():
    _instance = None

    def __new__(self):
        if not self._instance:
            self._instance = super(MySingleton, self).__new__(self)

            self.num = 10
            self.name = "Initial class value"

        return self._instance

# Made with has attributes


class MySingletonTwo():
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls, *args, **kwargs)
            # WHERE INSTANCE VARIABLES Go
            cls.num = 23
            cls.name = "Sina"
        return cls._instance
