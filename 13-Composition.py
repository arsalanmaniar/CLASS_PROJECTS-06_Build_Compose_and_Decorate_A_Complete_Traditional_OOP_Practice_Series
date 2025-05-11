class Engine:
    def start(self):
        print("Engine started.")

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start_car(self):
        self.engine.start()


my_engine = Engine()        # Engine ka object
my_car = Car(my_engine)     # Engine ko Car mein diya

my_car.start_car()          # Output: Engine started.
