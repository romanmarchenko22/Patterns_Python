class AnimalLazy:
    __instance = None

    def __init__(self):
        if not AnimalLazy.__instance:
            print("Method __init__ was called...")
        else:
            print("Instance was created: {}".format(self.get_instance()))

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = AnimalLazy()
        return cls.__instance


sl = AnimalLazy()
sl2 = AnimalLazy()
print('Lazy Singleton Instances: ')
print(sl.get_instance(), sl2.get_instance())
