import random
import string

def generate_password(length=12):
    chars = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    return ''.join(random.choice(chars) for _ in range(length))


def generate_unique_passwords(count=10, length=12):
    passwords = set()

    while len(passwords) < count:
        passwords.add(generate_password(length))

    return list(passwords)


amount = int(input("How many passwords? "))
length = int(input("Password length? "))

passwords = generate_unique_passwords(amount, length)

print("\nGenerated passwords:\n")
for i, p in enumerate(passwords, 1):
    print(f"{i}. {p}")