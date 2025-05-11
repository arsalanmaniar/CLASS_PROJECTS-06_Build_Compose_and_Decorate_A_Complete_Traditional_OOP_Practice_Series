class Product:
    def __init__(self, price):
        self._price = price  # Private attribute by convention

    @property
    def price(self):
        print("Getting price...")
        return self._price

    @price.setter
    def price(self, value):
        print("Setting price...")
        if value >= 0:
            self._price = value
        else:
            print("Price cannot be negative.")

    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

p = Product(100)

print(p.price)      # Getting price... ➝ 100

p.price = 150       # Setting price...

print(p.price)      # Getting price... ➝ 150

del p.price         # Deleting price...
