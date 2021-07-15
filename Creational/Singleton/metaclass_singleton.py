# Одинак — це породжувальний патерн проектування, який гарантує,
# що клас має лише один екземпляр, та надає глобальну точку доступу до нього.

class Animal(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Animal, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Cat(metaclass=Animal):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return repr(self) + self.name


class Dog(metaclass=Animal):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return repr(self) + self.name


print(id(Cat("Lolly")) == id(Cat("Susan")))
print(id(Dog("Lucky")) == id(Dog("Sam")))
