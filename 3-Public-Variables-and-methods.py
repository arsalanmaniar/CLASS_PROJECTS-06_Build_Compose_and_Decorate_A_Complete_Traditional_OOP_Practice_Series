class car:
    def __init__(self, brand):
        self.brand = brand
        
    def start(self):
        print(f"{self.brand} is starting...")    

my_car = car("Audi")
print(my_car.brand)  # Output: Audi
my_car.start()  # Output: Audi is starting...
