class DefaultAnimal:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DefaultAnimal, cls).__new__(cls)
        return cls.instance


first = DefaultAnimal()
second = DefaultAnimal()
print(id(first) == id(second))
