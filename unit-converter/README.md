# Unit Converter

A simple command-line Unit Converter written in Python. This program allows users to convert values between common units of length, weight, and temperature.

## Features

- 📏 Length conversions
  - Meters → Kilometers
  - Kilometers → Meters
  - Centimeters → Meters
  - Meters → Centimeters

- ⚖️ Weight conversions
  - Kilograms → Grams
  - Grams → Kilograms
  - Kilograms → Pounds
  - Pounds → Kilograms

- 🌡️ Temperature conversions
  - Celsius → Fahrenheit
  - Fahrenheit → Celsius

- Easy-to-use text-based menu
- Runs in the terminal
- No external libraries required

## Requirements

- Python 3.6 or later

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/unit-converter.git
```

2. Navigate to the project folder:

```bash
cd unit-converter
```

## Usage

Run the program with:

```bash
python unit_converter.py
```

or

```bash
python3 unit_converter.py
```

## Example

```text
===== UNIT CONVERTER =====
1. Length
2. Weight
3. Temperature
4. Exit

Select a category: 1

Length Converter
1. Meters to Kilometers
2. Kilometers to Meters
3. Centimeters to Meters
4. Meters to Centimeters

Choose an option: 2
Enter the value: 5

5.0 km = 5000.0 m
```

## Project Structure

```
unit-converter/
│── unit_converter.py
│── README.md
```

## Future Improvements

- Add more unit categories (Volume, Area, Speed, Time)
- Add a graphical user interface (GUI)
- Add a currency converter
- Improve input validation
- Save conversion history

## License

This project is open source and available under the MIT License.

## Author

Created by **Your Name**.
