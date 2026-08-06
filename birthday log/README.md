# 🎂 Birthday Dictionary

A simple Python program that stores birthdays in a dictionary and allows users to:

* Look up a person's birthday.
* Add a new birthday if it doesn't exist.
* Update the dictionary during runtime.

## Features

* Search for birthdays by name.
* Add new names and birthdays interactively.
* Runs continuously until the user exits.



## Example

```text
Enter the name (leave it empty to quit)
Rudro
04sep is the birthday of Rudro

Enter the name (leave it empty to quit)
Alice
I don't have info of Alice. What's the birthday?
12dec
Database updated

Enter the name (leave it empty to quit)
Alice
12dec is the birthday of Alice

Enter the name (leave it empty to quit)

```

## Requirements

* Python 3.x

## How to Run

1. Save the code in a file named `birthday.py`.
2. Open a terminal or command prompt.
3. Run:

```bash
python birthday.py
```

## Notes

* The birthday data is stored only in memory.
* Any new entries will be lost when the program exits.
* To make the data permanent, you can save the dictionary to a file (such as JSON or CSV).

