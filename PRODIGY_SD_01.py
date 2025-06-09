def convert_temperature(value, unit):
    if unit == 'C':
        celsius = value
        fahrenheit = (celsius * 9/5) + 32
        kelvin = celsius + 273.15
    elif unit == 'F':
        fahrenheit = value
        celsius = (fahrenheit - 32) * 5/9
        kelvin = celsius + 273.15
    elif unit == 'K':
        kelvin = value
        celsius = kelvin - 273.15
        fahrenheit = (celsius * 9/5) + 32
    else:
        raise ValueError("Invalid unit. Use 'C' for Celsius, 'F' for Fahrenheit, or 'K' for Kelvin.")
    
    return celsius, fahrenheit, kelvin

def main():
    print("Temperature Converter")
    try:
        temp_value = float(input("Enter the temperature value: "))
        temp_unit = input("Enter the unit (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()
        
        celsius, fahrenheit, kelvin = convert_temperature(temp_value, temp_unit)
        
        print(f"\nConverted Temperatures:")
        print(f"Celsius: {celsius:.2f} °C")
        print(f"Fahrenheit: {fahrenheit:.2f} °F")
        print(f"Kelvin: {kelvin:.2f} K")
        
    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == "__main__":
    main()
