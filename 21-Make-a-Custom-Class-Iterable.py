class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > 0:
            self.current -= 1
            return self.current + 1
        else:
            raise StopIteration

# Create an object of Countdown
countdown = Countdown(5)

# Test it in a for-loop
for num in countdown:
    print(num)
