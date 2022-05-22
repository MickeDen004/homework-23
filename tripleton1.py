class Tripleton(type):
    _instances = {}

    counter = 0

    def __call__(cls, *args, **kwargs):
        Tripleton.counter += 1
        while Tripleton.counter < 3:
            cls._instances[cls] = super(Tripleton, cls).__call__(*args, **kwargs)

        return cls._instances[cls]



class Tri(metaclass = Tripleton):
    def __init__(self):
        print("Initialising...")




