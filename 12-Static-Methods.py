class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9
    
print(TemperatureConverter.celsius_to_fahrenheit(0))     # Output: 32.0
print(TemperatureConverter.fahrenheit_to_celsius(98.6))  # Output: ~37.0
