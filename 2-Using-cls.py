class Counter:
    count = 0  # Class variable

    def __init__(self):
        Counter.count += 1  # Increment class variable

    @classmethod
    def display_count(cls):
        print(f"My total created object are: {cls.count}")

obj1 = Counter()
obj2 = Counter()
obj3 = Counter()
obj4 = Counter()
obj5 = Counter()
obj6 = Counter()

Counter.display_count()

