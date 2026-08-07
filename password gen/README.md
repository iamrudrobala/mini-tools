# 🔐 Random Password Generator

A simple Python program that generates strong, unique random passwords using letters, numbers, and special characters.

## Features

* Generate multiple passwords at once.
* Customize the password length.
* Uses:

  * Uppercase letters (`A-Z`)
  * Lowercase letters (`a-z`)
  * Numbers (`0-9`)
  * Special characters (`!@#$%^&*`, etc.)
* Ensures all generated passwords are unique.

## Requirements

* Python 3.x

No external libraries are required. The program uses Python's built-in `random` and `string` modules.

## How to Run

1. Save the code as `password_generator.py`.
2. Open a terminal or command prompt.
3. Run the program:

```bash
python password_generator.py
```

## Example

```text
How many passwords? 5
Password length? 12

Generated passwords:

1. 7@hL!mP2#QaZ
2. b9&XqW$4nRt%
3. K!8z@Lm2^YpQ
4. p#D7vX!5sHa*
5. Zq3&Nm@8Lp$T
```

## How It Works

1. The program asks how many passwords to generate.
2. It asks for the desired password length.
3. A character pool is created using:

   * Letters
   * Digits
   * Punctuation symbols
4. Random passwords are generated.
5. A Python `set` ensures that every password is unique.
6. The generated passwords are displayed in a numbered list.

## Project Structure

```text
.
├── password_generator.py
└── README.md
```

## Notes

* Passwords are generated using Python's `random` module.
* Each password is unique within a single run.
* For applications requiring cryptographically secure passwords, consider using Python's `secrets` module instead of `random`.

## Future Improvements

* Save passwords to a text file.
* Copy passwords directly to the clipboard.
* Exclude similar-looking characters (such as `O`, `0`, `I`, and `l`).
* Allow users to choose which character types to include.
* Build a graphical user interface (GUI).
* Add password strength indicators.

## License

This project is free to use for learning and personal projects.
