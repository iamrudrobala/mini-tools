def length_converter():
    print("\nLength Converter")
    print("1. Meters to Kilometers")
    print("2. Kilometers to Meters")
    print("3. Centimeters to Meters")
    print("4. Meters to Centimeters")

    choice = input("Choose an option: ")
    value = float(input("Enter the value: "))

    if choice == "1":
        print(f"{value} m = {value / 1000} km")
    elif choice == "2":
        print(f"{value} km = {value * 1000} m")
    elif choice == "3":
        print(f"{value} cm = {value / 100} m")
    elif choice == "4":
        print(f"{value} m = {value * 100} cm")
    else:
        print("Invalid choice!")


def weight_converter():
    print("\nWeight Converter")
    print("1. Kilograms to Grams")
    print("2. Grams to Kilograms")
    print("3. Kilograms to Pounds")
    print("4. Pounds to Kilograms")

    choice = input("Choose an option: ")
    value = float(input("Enter the value: "))

    if choice == "1":
        print(f"{value} kg = {value * 1000} g")
    elif choice == "2":
        print(f"{value} g = {value / 1000} kg")
    elif choice == "3":
        print(f"{value} kg = {value * 2.20462:.2f} lb")
    elif choice == "4":
        print(f"{value} lb = {value / 2.20462:.2f} kg")
    else:
        print("Invalid choice!")


def temperature_converter():
    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = input("Choose an option: ")
    value = float(input("Enter the temperature: "))

    if choice == "1":
        print(f"{value}°C = {(value * 9/5) + 32:.2f}°F")
    elif choice == "2":
        print(f"{value}°F = {(value - 32) * 5/9:.2f}°C")
    else:
        print("Invalid choice!")


def main():
    while True:
        print("\n===== UNIT CONVERTER =====")
        print("1. Length")
        print("2. Weight")
        print("3. Temperature")
        print("4. Exit")

        choice = input("Select a category: ")

        if choice == "1":
            length_converter()
        elif choice == "2":
            weight_converter()
        elif choice == "3":
            temperature_converter()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
