def main():
    class TemperatureConversion:

        def __init__(self, temp=1):
            self._temp = temp

        def celsius_to_fahrenheit(self):
            return (self._temp * 9) / 5 + 32

        def fahrenheit_to_celsius(self):
            return (self._temp - 32) * 5 / 9

        def celsius_to_kelvin(self):
            return self._temp + 273.15

    temp_in_celsius = float(input("Enter the temperature in Celsius: "))

    conversion = TemperatureConversion(temp_in_celsius)

    print(str(conversion.celsius_to_kelvin()) + " Kelvin")

    print(str(conversion.celsius_to_fahrenheit()) + " Fahrenheit")

    temp_in_fahrenheit = float(input("Enter the temperature in Fahrenheit: "))

    conversion = TemperatureConversion(conversion.fahrenheit_to_celsius())

    print(str(conversion.celsius_to_kelvin()) + " Kelvin")

    print(str(conversion._temp) + " Celsius")

if __name__ == '__main__':
    main()