def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return fahrenheit_to_celsius(f) + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return celsius_to_fahrenheit(kelvin_to_celsius(k))

def convert_temperature():
    print("=== Temperature Converter ===")
    print("Units: C = Celsius, F = Fahrenheit, K = Kelvin")
    print()

    while True:
        value = input("Enter temperature value (or 'q' to quit): ").strip()
        if value.lower() == 'q':
            break
        try:
            value = float(value)
        except ValueError:
            print("Invalid number. Try again.\n")
            continue

        unit = input("Enter unit (C/F/K): ").strip().upper()
        if unit not in ('C', 'F', 'K'):
            print("Invalid unit. Use C, F, or K.\n")
            continue

        print()
        if unit == 'C':
            print(f"  {value}°C  =  {celsius_to_fahrenheit(value):.2f}°F  =  {celsius_to_kelvin(value):.2f}K")
        elif unit == 'F':
            print(f"  {value}°F  =  {fahrenheit_to_celsius(value):.2f}°C  =  {fahrenheit_to_kelvin(value):.2f}K")
        elif unit == 'K':
            print(f"  {value}K  =  {kelvin_to_celsius(value):.2f}°C  =  {kelvin_to_fahrenheit(value):.2f}°F")
        print()

convert_temperature()